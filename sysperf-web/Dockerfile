# syntax=docker/dockerfile:1
FROM sysperf-base:latest

# Explicitly creating directory structure
RUN mkdir /sysperf
RUN mkdir /sysperf/fcp-logs
RUN mkdir /sysperf/fcp-uploads
RUN mkdir /sysperf/spw-logs
RUN mkdir /sysperf/spw-uploads

# Populating files 
WORKDIR /sysperf
COPY main.py main.py
WORKDIR templates
COPY fcp-index.html fcp-index.html
COPY fcp-upload.html fcp-upload.html
COPY fcp-process.html fcp-process.html
COPY spw-index.html spw-index.html
COPY spw-upload.html spw-upload.html
COPY spw-process.html spw-process.html
COPY test.html test.html

# Setting flask runtime environment variables
# and starting flask
WORKDIR /sysperf
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5001
#ENV FLASK_ENV=development
CMD ["flask", "run"]
