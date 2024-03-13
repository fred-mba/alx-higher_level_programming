#!/usr/bin/node
module.exports =
class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let ex = '';
      for (let j = 0; j < this.width; j++) {
        ex = ex + 'X';
      }
      console.log(ex);
    }
  }

  rotate () {
    const cambio = this.height;
    this.height = this.width;
    this.width = cambio;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
};
