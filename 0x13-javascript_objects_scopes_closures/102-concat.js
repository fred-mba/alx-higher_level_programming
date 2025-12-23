#!/usr/bin/node

const file = process.argv;
const fs = require('fs');

const file2Content = fs.readFileSync(`${file[2]}`, 'utf8');
const file3Content = fs.readFileSync(`${file[3]}`, 'utf8');

const combinedContent = file2Content + file3Content;

fs.writeFileSync(`${file[4]}`, combinedContent, 'utf8');
