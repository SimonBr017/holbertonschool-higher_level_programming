#!/usr/bin/node

/**
 * script that gets the contents of a webpage and stores it in a file.
 */

const request = require('request');
const url = process.argv[2];
const fs = require('fs');

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  fs.appendFile(process.argv[3], body, function (err) {
    if (err) {
      console.log('append failed');
      console.error(err);
    } else {
      console.log('Done');
    }
  });
});
