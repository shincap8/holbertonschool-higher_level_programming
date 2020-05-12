#!/usr/bin/node
const myArgs = process.argv.slice(2);
const request = require('request');
request(myArgs[0], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const fs = require('fs');
    fs.writeFile(myArgs[1], body, function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
