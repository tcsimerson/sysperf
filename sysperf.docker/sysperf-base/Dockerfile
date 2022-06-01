FROM alpine:3.16.0

# Install additional packages
RUN apk add python3 py3-pip

# Install additional Python modules via pip
RUN pip install openpyxl flask

# Working directory for sysperf processes
RUN mkdir /sysperf
WORKDIR /sysperf
