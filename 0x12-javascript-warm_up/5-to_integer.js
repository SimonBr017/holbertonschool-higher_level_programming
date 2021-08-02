#!/usr/bin/node

/**
 * script that prints My number: <first argument converted in integer>
 */

const parsed = parseInt(process.argv[2]);

if (isNaN(parsed)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parsed);
}
