# syntax=docker/dockerfile:1
FROM alpine:3.16.0

# Forcing to use non-secure repsitories
COPY repositories /etc/apk/repositories

# Install additional packages
RUN apk add python3 py3-pip

# Install additional Python modules via pip
RUN pip install openpyxl flask requests

