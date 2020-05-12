#!/usr/bin/node
const myArgs = process.argv.slice(2);
const fs = require('fs');
const text1 = fs.readFileSync(myArgs[0], 'utf8');
const text2 = fs.readFileSync(myArgs[1], 'utf8');
fs.writeFileSync(myArgs[2], text1 + text2);
