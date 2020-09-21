#!/usr/bin/node
/*
* Task 5
*/
class Square extends require('./5-square.js') {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let i;
    let p = '';
    for (i = 0; i < this.width; i++) {
      p += c;
    }
    for (i = 0; i < this.height; i++) {
      console.log(p);
    }
  }
}
module.exports = Square;
