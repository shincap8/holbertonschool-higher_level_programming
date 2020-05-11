#!/usr/bin/node
let list = require('./100-data').list;
console.log(list);
list = list.map(function (num, index) {
  return num * index;
});
console.log(list);
