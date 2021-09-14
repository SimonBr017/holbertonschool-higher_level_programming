#!/usr/bin/node

/**
 * script that display status code of a Get request
 */

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  console.log('code:', response && response.statusCode);
});
