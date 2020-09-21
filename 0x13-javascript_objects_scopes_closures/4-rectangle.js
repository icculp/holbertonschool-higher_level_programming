#!/usr/bin/node
/*
* Task 4
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

  rotate () {
    const helper = this.width;
    this.width = this.height;
    this.height = helper;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
