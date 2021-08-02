#!/usr/bin/node

/**
 * script that prints the addition of 2 integers
 */

function factorial (x) {
  if (isNaN(x) || x === 0) {
    return (1);
  }
  return (x * factorial(x - 1));
}
console.log(factorial(parseInt(process.argv[2])));
