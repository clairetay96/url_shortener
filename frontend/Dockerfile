FROM node:14-buster-slim

# Set working directory for react project
WORKDIR /code/frontend
# Install node modules
COPY package.json .
RUN npm install
EXPOSE 3000
CMD ["npm", "run", "build"]