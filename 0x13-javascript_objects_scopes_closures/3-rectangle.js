#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let loop1 = 0; loop1 < this.height; loop1++) {
      let su = '';
      for (let loop2 = 0; loop2 < this.width; loop2++) {
        su += 'X';
      }
      console.log(su);
    }
  }
}

module.exports = Rectangle;
