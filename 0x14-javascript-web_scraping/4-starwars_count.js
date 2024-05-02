#!/usr/bin/node

const req = require('request');
const apiUrl = process.argv[2];

const charUrl = 'https://swapi-api.alx-tools.com/api/people/18/';

req(apiUrl, (error, response, body) => {
  if (error) throw error;

  const filmData = JSON.parse(body);

  let filmCount = 0;

  for (const film of filmData.results) {
    if (film.characters.includes(charUrl)) {
      filmCount++;
    }
  }

  console.log(filmCount);
});
