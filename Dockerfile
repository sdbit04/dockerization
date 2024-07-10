FROM ubuntu:latest
LABEL authors="sdbit"

ENTRYPOINT ["top", "-b"]