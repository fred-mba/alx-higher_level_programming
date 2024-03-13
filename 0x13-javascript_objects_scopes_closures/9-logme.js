#!/usr/bin/node

const arr = [];
exports.logMe = function (item) {
  arr.push(item);
  console.log(arr.length - 1 + ' ' + item);
};
