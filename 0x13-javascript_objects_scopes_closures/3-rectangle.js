#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let xs = '';
    for (let j = 0; j < this.width; j++) {
      xs += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(xs);
    }
  }
};
