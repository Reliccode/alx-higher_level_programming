#!/usr/bin/node
const request = require('request');

const movieId = parseInt(process.argv[2], 10);
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (!error) {
    const film = JSON.parse(body);
    const characters = film.characters;

    characters.forEach((characterUrl) => {
      request(characterUrl, (err, response, charBody) => {
        if (!err) {
          console.log(JSON.parse(charBody).name);
        }
      });
    });
  }
});
