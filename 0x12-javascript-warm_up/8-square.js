#!/usr/bin/node
const x = process.argv.slice(2);
if (parseInt(x[0])) {
  let xs = '';
  for (let j = 0; j < x; j++) {
    xs += 'X';
  }
  for (let i = 0; i < x; i++) {
    console.log(xs);
  }
} else {
  console.log('Missing size');
}
