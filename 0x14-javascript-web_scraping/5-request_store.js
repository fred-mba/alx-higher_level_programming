#!/usr/bin/node

const fileSystem = require('fs');
const req = require('request');

const url = process.argv[2];
const fileName = process.argv[3];

req(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }

  fileSystem.writeFile(fileName, body, 'utf-8', err => {
    if (err) {
      console.error(err);
    }
  });
});
