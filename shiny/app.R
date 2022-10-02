library(httr)
library(shiny)
library(jsonlite)
library(shinythemes)
library(shinyPagerUI)


# Load cohere API
source("cohere.R", local=TRUE)
key = get_api_key('secrets.yaml')


ui <- fluidPage(
  theme=shinytheme("flatly"),

  titlePanel("Helpium"),

  sidebarPanel(
    textInput("prompt", "Prompt", value="Mary had a little lamb"),
    submitButton("Generate", icon("refresh"))
  ),

  mainPanel(
    textOutput("generated"),
    pageruiInput('pager', page_current=1, pages_total=3)
  )

)

server <- function(input, output) {

  output$generated <- renderText({
    r <- request_generation(
      input$prompt,
      key=key,
      max_tokens=256,
      temperature=0.8,
      k=0,
      frequency_penalty=0,
      presence_penalty=0,
      num_generations=3
    )
    r[input$pager$page_current]
  })

}

options(shiny.port=7280, shiny.host='0.0.0.0')
shinyApp(ui, server)
