#!/usr/bin/node
const x = process.argv.slice(2);
if (parseInt(x[0])) {
  for (var i = 0; i < x; i++) {
    console.log('c is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
