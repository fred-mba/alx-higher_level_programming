#!/usr/bin/node
const arg = process.argv;
const number = parseInt(arg[2]);

if (isNaN(number)) {
  console.log('Missing number of occurrences');
}

let i = 0;
while (i < number) {
  console.log('C is fun');
  i++;
}
