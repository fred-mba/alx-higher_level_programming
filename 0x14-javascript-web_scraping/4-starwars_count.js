#!/usr/bin/node

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
