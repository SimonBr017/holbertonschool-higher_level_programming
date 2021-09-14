#!/usr/bin/node

/**
 * script that computes the number of elements completed by user id
 */

const request = require('request');
const url = process.argv[2];

request(url, { json: true }, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const user = {};

  body.forEach(element => {
    if (element.completed === true) {
      if (element.userId in user) {
        user[element.userId] += 1;
      } else {
        user[element.userId] = 1;
      }
    }
  });
  console.log(user);
});
