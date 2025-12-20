#!/usr/bin/node
/* Creates a new list with its element multiplied by the index in the list */

const list = require('./100-data').list;
const newList = list.map((x, index) => x * index);

console.log(list);
console.log(newList);
