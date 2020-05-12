#!/usr/bin/node
const myArgs = process.argv.slice(2);
const request = require('request');
let count = 0;
const character = 'https://swapi-api.hbtn.io/api/people/18/';
request(myArgs[0], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const list = JSON.parse(body).results;
    for (const i of list) {
      if (i.characters.includes(character)) {
        count++;
      }
    }
    console.log(count);
  }
});
