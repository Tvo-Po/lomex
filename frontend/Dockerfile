FROM node:lts-alpine

RUN npm install -g http-server

WORKDIR /usr/src/lomex

COPY package*.json ./
RUN npm install
COPY . .
RUN npm install --save axios

EXPOSE 8080
CMD [ "http-server", "dist" ]