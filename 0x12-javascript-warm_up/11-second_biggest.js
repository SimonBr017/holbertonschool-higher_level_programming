#!/usr/bin/node

/**
 * script that searches the second biggest integer in the list of arguments.
 */

if (process.argv.length < 4) {
  console.log('0');
} else {
  const arr = process.argv.slice(2); // select elements from an array
  const intArr = arr.map(Number); // convert into number
  const secondLargestNumber = intArr.sort((a, b) => {
    return b - a;
  })[1];
  console.log(secondLargestNumber);
}
