#!/usr/bin/node
/**
* A script that prints the number of movies where the character “Wedge Antilles” is present
* Wedge Antilles is character ID 18 - the script must use this ID for filtering the result of the API
* Star wars API: https://swapi-api.alx-tools.com/api/films/
*/

const req = require('request');
const apiUrl = process.argv[2];

const charId = '18';

req(apiUrl, (error, response, body) => {
  if (error) throw error;

  const filmData = JSON.parse(body);

  let filmCount = 0;

  for (const film of filmData.results) {
    for (const characterUrl of film.characters) {
      if (characterUrl.includes(charId)) {
        filmCount++;
      }
    }
  }

  console.log(filmCount);
});
