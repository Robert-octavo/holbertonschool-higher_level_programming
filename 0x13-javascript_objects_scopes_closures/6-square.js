#!/usr/bin/node
// TODO: charPrint(c) that prints the rectangle using the character c
// TODO: If c is undefined, use the character X

class Square extends require('./4-rectangle') {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
