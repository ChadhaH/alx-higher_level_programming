#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (ch) {
    if (ch === undefined) {
      ch = 'X';
    }
    for (let loop1 = 0; loop1 < this.height; loop1++) {
      let su = '';
      for (let loop2 = 0; loop2 < this.width; loop2++) {
        su += ch;
      }
      console.log(su);
    }
  }
}

module.exports = Square;
