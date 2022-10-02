library(here)
library(yaml)
library(rsconnect)

get_shinyapps_credentials <- function(secrets_yaml) {
  secrets = read_yaml(here(secrets_yaml))
  return(secrets$shinyapps)
}

secrets <- get_shinyapps_credentials(here('secrets.yaml'))
cat("Logging in...\n")
do.call(rsconnect::setAccountInfo, secrets)

cat("Deploying...\n")
rsconnect::deployApp(appDir=here("shiny"), appName="helpium")
