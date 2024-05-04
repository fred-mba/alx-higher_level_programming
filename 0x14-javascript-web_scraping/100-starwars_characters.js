#!/usr/bin/node

const req = require('request');
const movieId = process.argv[2];
const movieUrl = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

req(movieUrl, (error, response, body) => {
  if (error) console.error(error);
  const movieData = JSON.parse(body);

  for (const charUrl of movieData.characters) {
    req(charUrl, (error, response, body) => {
      if (error) console.error(error);
      const characterDetails = JSON.parse(body);

      console.log(characterDetails.name);
    });
  }
});
