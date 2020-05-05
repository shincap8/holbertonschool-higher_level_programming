#!/usr/bin/node
const myArgs = process.argv.slice(2);
if (parseInt(myArgs[0])) {
  console.log('My number: ' + Math.trunc(myArgs[0]));
} else {
  console.log('Not a number');
}
