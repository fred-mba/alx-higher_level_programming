#!/usr/bin/node
/* Ascript that display the status code of a GET request */

const req = require('request');

const url = process.argv[2];

req(url, (error, response) => {
  if (error) console.log(error);

  console.log('code:', response.statusCode);
});
