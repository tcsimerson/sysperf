# syntax=docker/dockerfile:1
FROM sysperf-base:latest

WORKDIR /sar-perf
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5001
ENV FLASK_ENV=development
COPY main.py main.py
WORKDIR templates
COPY index.html index.html
COPY test.html test.html
WORKDIR /sar-perf
CMD ["flask", "run"]
