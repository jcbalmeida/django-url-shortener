FROM node

WORKDIR /app

COPY ./frontend/package.json /app/package.json
COPY ./frontend/yarn.lock /app/yarn.lock

RUN yarn

COPY ./frontend/. /app/
