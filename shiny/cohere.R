library(yaml)
library(httr)
library(glue)
library(rvest)
library(readr)
library(dplyr)
library(purrr)
library(stringr)
library(jsonlite)

get_api_key <- function(secrets_yaml) {

  secrets = read_yaml(secrets_yaml)
  return(secrets$cohere$api_key)

}

request_generation <- function(prompt, key, ...) {

  headers = c('Authorization' = paste('BEARER', key),
              'Content-Type' = 'application/json',
              'Cohere-Version' = '2021-11-08'
              )

  body = c(list(prompt=prompt), ...)

  api_url = "https://api.cohere.ai/generate"

  r <- POST(url=api_url,
            body=body,
            add_headers(.headers = headers),
            encode='json')

  print(content(r))
  generations = unlist(content(r)$generations)

  splits <- map(generations, function(x) str_split(x, '--'))
  splits <- map(splits, function(x) x[[1]][1])
  output <- paste(splits, collapse="\n-----------\n\n")

  return(str_trim(output))

}

generate_prompt <- function(example_csv, num_examples=15) {

  examples <- read_csv(example_csv, col_names=c("command", "email"))
  examples <- head(examples, num_examples)
  preset = "This email writing program can generate full email templates from commands. Here are some examples:\n"

  prompt <- map2(examples$command, examples$email, function(c, e) glue({"--\ncommand: {c}\nemail: {e}"}))
  prompt <- paste(prompt, collapse='\n')
  prompt <- paste0(preset, prompt)

  return(prompt)
}

get_command <- function(prompt, command) {

  command <- glue("Command: A letter to the government asking {command}\nEmail: ")
  return(paste0(prompt, command))

}

## key = get_api_key('secrets.yaml')

## prompt <- generate_prompt('examples.csv')
## command <- get_command(prompt, 'how can I apply for a benefit')

## r <- request_generation(
##   command,
##   key=key,
##   max_tokens=128,
##   temperature=0.8,
##   k=0,
##   frequency_penalty=0,
##   presence_penalty=0,
##   num_generations=3
##   )

