#!/usr/bin/node
const myArgs = process.argv.slice(2);
function factorial (a) {
  if (isNaN(a)) {
    return 1;
  } else if (a === 1) {
    return 1;
  } else {
    const b = a - 1;
    return (a * factorial(b));
  }
}
const a = parseInt(myArgs[0]);
console.log(factorial(a));
