#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];

const fInput = process.argv[3];

fs.writeFile(filePath, fInput, (err) => {
  if (err) throw err;
});
