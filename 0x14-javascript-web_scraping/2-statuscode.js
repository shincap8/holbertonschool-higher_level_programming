#!/usr/bin/node
const myArgs = process.argv.slice(2);
const request = require('request');
request.get(myArgs[0]).on('response', function (response) {
  console.log(response.statusCode);
});
