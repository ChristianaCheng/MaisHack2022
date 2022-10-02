library(httr)
library(shiny)
library(jsonlite)
library(shinythemes)
library(shinyPagerUI)


# Load cohere API
source("cohere.R", local=TRUE)
key = get_api_key('secrets.yaml')

prompt <- generate_prompt('examples.csv')


ui <- fluidPage(
  theme=shinytheme("flatly"),
  tags$style(type='text/css', '#generated {white-space: pre-wrap;}'),
  titlePanel("Helpium"),

  sidebarPanel(
    h4("What is Helpium?"),
    p("The purpose of helpium is to help people with poor literacy or second language speakers to write emails in order access essential services. Simply tell us what you need, and we can help you write an email or letter that will help you make your request in plain english."),
    p(""),
    p("Just tell us what you want the letter to be about on the left and the text will appear below. We hope we can help you get the assistance you need :)"),
    textInput("prompt", "How can we help?", value="How can I apply for a student visa"),
    submitButton("Generate", icon("arrows-rotate"))
  ),

  mainPanel(
     verbatimTextOutput("generated")
  )

)


server <- function(input, output) {

  output$generated <- renderText({

    r <- request_generation(
      get_command(prompt, input$prompt),
      key=key,
      max_tokens=128,
      temperature=0.8,
      k=0,
      frequency_penalty=0,
      presence_penalty=0,
      num_generations=3
    )
    r
  })

}


options(shiny.port=7280, shiny.host='0.0.0.0')
shinyApp(ui, server)
