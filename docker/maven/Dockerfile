FROM maven:3.8.8-amazoncorretto-21-debian

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y\
	git

COPY /compile.sh
ENTRYPOINT bash compile.sh