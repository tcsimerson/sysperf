# syntax=docker/dockerfile:1
FROM sysperf-base:latest

WORKDIR /sysperf
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY main.py main.py
CMD ["flask", "run"]
