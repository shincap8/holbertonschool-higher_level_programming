#!/usr/bin/node
const myArgs = process.argv.slice(2);
function add (a, b) {
  console.log(a + b);
}
const a = parseInt(myArgs[0]);
const b = parseInt(myArgs[1]);
add(a, b);
