#!/usr/bin/node
/*
 * Script that concats 2 files
 * 1st argument is the file path of the first source file
 * 2nd argument is the file path of the second source file
 * 3rd argument is the file path of the destination
*/
const file = process.argv;
const fs = require('fs');

const file2Content = fs.readFileSync(`${file[2]}`, 'utf8');
const file3Content = fs.readFileSync(`${file[3]}`, 'utf8');

const combinedContent = file2Content + file3Content;

fs.writeFileSync(`${file[4]}`, combinedContent, 'utf8');
