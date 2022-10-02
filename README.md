# MaisHack2022

Google Doc: https://docs.google.com/document/d/1V3DRD8w_lNx_R5AnYZtiTNhvH4yN3M6FbEoQXMCqs7M/edit

## How to get it running

This project runs using a docker container saved at `Dockerfile`. Before you get started, we recommend using Docker, although this is not necessary if you have your own installation of `python` and `R`.

We also make use of a Makefile as well, stored at `Makefile`. This means there are only a few handy commands that you need to know in order to build the project.

### Some useful commands

```
# build the docker container
make docker

# launches a jupyterlab instance at localhost:8888
make jupyter

# starts the shiny app at localhost:7280
make shiny

# deploys the shiny app
make deploy
```
