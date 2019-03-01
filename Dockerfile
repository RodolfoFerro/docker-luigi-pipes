# We will use Ubuntu for our image:
FROM ubuntu:latest

# Updating Ubuntu packages:
RUN apt-get update && yes|apt-get upgrade && \
    apt-get install -y wget && \
    apt-get install -y sudo && \
    apt-get install -y vim && \
    apt-get install -y nano && \
    apt-get install -y htop

# Set locales for encoding:
RUN apt-get update && apt-get install -y locales && rm -rf /var/lib/apt/lists/* \
    && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG en_US.utf8

# Add working directory:
WORKDIR /docker-luigi-pipes

# Copy files into our container:
COPY . /docker-luigi-pipes

# Install Anaconda:
RUN wget https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh && \
    bash Anaconda3-5.0.1-Linux-x86_64.sh -b && \
    rm Anaconda3-5.0.1-Linux-x86_64.sh

# Set path to conda:
ENV PATH /root/anaconda3/bin:$PATH

# Update Anaconda packages:
RUN conda update conda && \
    conda update anaconda && \
    conda update --all

# Install conda packages:
RUN conda install -c conda-forge luigi scipy numpy pillow tesseract && \
    conda install -c menpo opencv && \
    conda install -c jim-hart pytesseract
