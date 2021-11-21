FROM node:16-alpine

WORKDIR /usr/src/lomex

ENV PATH /usr/src/lomex/node_modules/.bin:$PATH

COPY package*.json ./

RUN npm cache clean --force

RUN rm -rf node_modules && npm install
RUN npm install @vue/cli@3.7.0 -g

RUN npm update -g

COPY . .

CMD ["npm", "run", "serve"]