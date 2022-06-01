# syntax=docker/dockerfile:1
FROM sysperf-base

WORKDIR /flexperf
COPY hello.py hello.py
ENV FLASK_APP=hello.py
ENV FLASK_RUN_HOST=0.0.0.0
CMD ["flask", "run"]
