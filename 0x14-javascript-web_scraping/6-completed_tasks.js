#!/usr/bin/node
const myArgs = process.argv.slice(2);
const request = require('request');
const completed = {};
request(myArgs[0], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const list = JSON.parse(body);
    for (const i of list) {
      if (i.completed === true) {
        if (!(i.userId in completed)) {
          completed[i.userId] = 1;
        } else {
          completed[i.userId]++;
        }
      }
    }
    console.log(completed);
  }
});
