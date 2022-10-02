library(yaml)
library(httr)
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

  return(generations)

}