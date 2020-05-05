#!/usr/bin/node
const myArgs = process.argv.slice(2);
function compareNum (a, b) {
  return a - b;
}
const n = myArgs.length;
if (n === 0 || n === 1) {
  console.log(0);
} else {
  console.log(myArgs.sort(compareNum)[n - 2]);
}
