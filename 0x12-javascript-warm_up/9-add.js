#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const arg = process.argv;
const a = parseInt(arg[2]);
const b = parseInt(arg[3]);

const res = add(a, b);
console.log(res);
