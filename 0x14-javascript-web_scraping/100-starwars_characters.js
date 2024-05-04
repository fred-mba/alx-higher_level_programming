#!/usr/bin/node
/**
 * A script that prints all characters of a Star Wars movie
 * The first argument is the Movie ID - example: 3 = “Return of the Jedi”
 * Display one character name by line
 * Must use Star ways api: https://swapi-api.alx-tools.com/
*/

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
