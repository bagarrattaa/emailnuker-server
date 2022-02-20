FROM ubuntu
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt upgrade -y && apt install python3 bash python3-pip -y && pip3 install flask flask_mail
COPY . /data
EXPOSE 5000
CMD [ "/data/cmd.sh" ]
