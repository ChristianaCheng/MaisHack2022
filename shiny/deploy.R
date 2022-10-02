library(yaml)
library(rsconnect)

get_shinyapps_credentials <- function(secrets_yaml) {
  secrets = read_yaml(secrets_yaml)
  return(secrets$shinyapps)
}

secrets <- get_shinyapps_credentials('secrets.yaml')
cat("Logging in...\n")
do.call(rsconnect::setAccountInfo, secrets)

cat("Deploying...\n")
rsconnect::deployApp(appDir=".", appName="helpium")
