#!/usr/bin/node
const myArgs = process.argv.slice(2);
const request = require('request');
let count = 0;
request(myArgs[0], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const list = JSON.parse(body).results;
    for (const i of list) {
      for (const j of i.characters) {
        if (j.slice(-3) === '18/') {
          count++;
        }
      }
    }
    console.log(count);
  }
});
