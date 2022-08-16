#!/usr/bin/node
// TODO: If w or h is equal to 0 or not a positive integer, create an empty object
// TODO: Create an instance method called print() that prints the rectangle using the character
// TODO: Create an instance method called rotate() that exchanges the width and the height of the rectangle
// TODO: Create an instance method called double() that multiples the width and the height of the rectangle by 2

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }
};
