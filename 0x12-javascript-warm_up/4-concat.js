#!/usr/bin/node
const myArgs = process.argv.slice(2);
if (!myArgs[0]) {
  myArgs[0] = 'undefined';
}
if (!myArgs[1]) {
  myArgs[1] = 'undefined';
}
console.log(myArgs[0] + ' is ' + myArgs[1]);
