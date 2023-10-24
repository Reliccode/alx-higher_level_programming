#!/usr/bin/node
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${parseInt(process.argv[2], 10) + (process.argv[2] < 4 ? 3 : -3)}/`;

request(url, (err, response, body) => {
  if (!err) {
    const characters = JSON.parse(body).characters;
    characters.forEach((characterUrl) => {
      request(characterUrl, (err, response, body) => {
        if (!err) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
