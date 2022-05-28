FROM ubuntu
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt upgrade -y && apt install curl wget bash python3 python3-pip -y
COPY . /data
RUN pip3 install -r /data/requirements.txt
RUN pip3 install flask
WORKDIR /data
CMD [ "/data/start.sh" ]