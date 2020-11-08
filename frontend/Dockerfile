FROM node:12.16.1-slim

WORKDIR /frontend

COPY package.json package.json
RUN npm install

COPY . .
RUN npm run build

EXPOSE 3000
ENTRYPOINT ["npm", "run", "start"]
