FROM rocker/tidyverse

ARG DEBIAN_FRONTEND=noninteractive
RUN apt update

# Create rstudio 'rstudio' to create a home directory
# RUN useradd rstudio
RUN mkdir -p /home/rstudio/
RUN chown -R rstudio:rstudio /home/rstudio
ENV HOME /home/rstudio

# Install apt packages
RUN apt update
RUN apt install -y curl wget software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa

# Install python
ENV PYTHON_VERSION 3.9
ENV PYTHON python${PYTHON_VERSION}
RUN apt update
RUN apt install -y ${PYTHON}-dev ${PYTHON}-distutils
RUN rm /usr/bin/python3 && ln -s /usr/bin/${PYTHON} /usr/bin/python3
RUN curl -sS https://bootstrap.pypa.io/get-pip.py | ${PYTHON}

# Set default python version
RUN update-alternatives --install /usr/bin/python python /usr/bin/${PYTHON} 1
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/${PYTHON} 1

# Install pip
RUN curl -sS https://bootstrap.pypa.io/get-pip.py | ${PYTHON}
RUN update-alternatives --install /usr/local/bin/pip pip /usr/local/bin/pip${PYTHON_VERSION} 1
RUN update-alternatives --install /usr/local/bin/pip3 pip3 /usr/local/bin/pip${PYTHON_VERSION} 1

RUN pip3 install --upgrade pip
COPY requirements.txt /root/requirements.txt
RUN pip3 install -r /root/requirements.txt

# Install local package
COPY mais_hack /code/mais_hack
COPY setup.py /code
RUN python${PYTHON_VERSION} -m pip install -e /code
ENV PYTHONPATH="/code:${PYTHONPATH}"

# Install R packages
RUN Rscript -e 'install.packages("here")'
RUN Rscript -e 'install.packages("shiny")'
RUN Rscript -e 'install.packages("rsconnect")'
RUN Rscript -e 'install.packages("glue")'
RUN Rscript -e 'install.packages("shinythemes")'
RUN Rscript -e 'devtools::install_github("wleepang/shiny-pager-ui")'
