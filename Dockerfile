FROM alpine:latest

RUN apk update \
    && apk upgrade \
    && apk add npm \
    && apk add python3 \
    && apk add py-pip \
    && apk add git

RUN npm install -g aws-cdk

COPY entrypoint.sh /entrypoint.sh

CMD "/entrypoint.sh"