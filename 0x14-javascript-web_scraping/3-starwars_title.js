#!/usr/bin/node
/* A script that prints the title of a Star Wars movie where the episode number matches a given integer */

const req = require('request');
const baseUrl = 'https://swapi-api.alx-tools.com/api/films/';
const filmUrl = baseUrl + process.argv[2];

req(filmUrl, (error, response, body) => {
  if (error) throw error;

  const filmData = JSON.parse(body);

  console.log(filmData.title);
});
