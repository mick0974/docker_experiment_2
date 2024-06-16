FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN mkdir /tool

COPY tool/ /tool/

RUN apt update && \
    apt -y upgrade && \
    apt -y install openjdk-11-jdk && \
    apt -y autoremove

CMD bash -c "cd ./tool && \
java -jar resttestgen-framework-23.05-all.jar -s OperationSemanticsDecisionTreeStrategy -l DEBUG"
