FROM node:16.13-alpine3.13

ENV PROJECT_DIR /usr/local/src/app

WORKDIR ${PROJECT_DIR}

COPY package* ${PROJECT_DIR}/

RUN npm install
RUN npm run watch
