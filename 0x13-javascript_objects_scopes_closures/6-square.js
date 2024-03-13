#!/usr/bin/node

const Rectangle = require('./5-square');

module.exports =
class Square extends Rectangle {
  charPrint (c) {
    if (c !== undefined) {
      for (let i = 0; i < this.height; i++) {
        let ex = '';
        for (let j = 0; j < this.width; j++) {
          ex = ex + c;
        }
        console.log(ex);
      }
    } else {
      super.print();
    }
  }
};
