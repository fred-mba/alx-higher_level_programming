#!/usr/bin/node
/**
 * A script that prints all characters of a Star Wars movie
 * The first argument is the Movie ID - example: 3 = “Return of the Jedi”
 * Displays one character name by line in the same order of the list “characters” in the /films/ response
 */

const req = require('request');
const movieId = process.argv[2];
const movieUrl = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

const fetchCharacterDetails = async (charUrl) => {
  return new Promise((resolve, reject) => {
    req(charUrl, (error, response, body) => {
      if (error) reject(error);
      const characterDetails = JSON.parse(body);
      resolve(characterDetails.name);
    });
  });
};

const displayCharNames = async () => {
  try {
    const movieData = JSON.parse(await makeRequest(movieUrl));

    for (const charUrl of movieData.characters) {
      const characterName = await fetchCharacterDetails(charUrl);
      console.log(characterName);
    }
  } catch (error) {
    console.error(error);
  }
};

const makeRequest = (url) => {
  return new Promise((resolve, reject) => {
    req(url, (error, response, body) => {
      if (error) reject(error);
      resolve(body);
    });
  });
};

displayCharNames();
