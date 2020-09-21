#!/usr/bin/node
/*
* Task 2
*/
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
    }
  }

  print () {
    let i;
    let p = '';
    for (i = 0; i < this.width; i++) {
      p += 'X';
    }
    for (i = 0; i < this.height; i++) {
      console.log(p);
    }
  }
}
module.exports = Rectangle;
