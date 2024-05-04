#!/usr/bin/node
// A script that reads and prints the content of a file

const filesystem = require('fs');

const filePath = process.argv[2];

filesystem.readFile(filePath, 'utf-8', (err, data) => {
  if (err) throw err;

  console.log(data);
});
