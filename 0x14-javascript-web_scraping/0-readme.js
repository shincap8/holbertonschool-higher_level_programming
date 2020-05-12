#!/usr/bin/node
const myArgs = process.argv.slice(2);
const fs = require('fs');
fs.readFile(myArgs[0], 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
