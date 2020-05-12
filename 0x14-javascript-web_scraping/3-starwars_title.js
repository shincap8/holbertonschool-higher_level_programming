#!/usr/bin/node
const myArgs = process.argv.slice(2);
const reqURL = 'https://swapi-api.hbtn.io/api/films/' + myArgs[0];
const request = require('request');
request(reqURL, function (error, response, body) {
  console.log(response.statusCode);
  if (error) {
    console.error(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
