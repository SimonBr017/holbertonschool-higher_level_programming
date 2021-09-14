#!/usr/bin/node

/**
 * script that prints the title of a Star Wars movie
 * where the episode number matches a given integer
 */

const request = require('request');
const api = process.argv[2];
const url = api;
let counter = 0;

request(url, { json: true }, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  for (const film of body.results) {
    for (const charac of film.characters) {
      if (charac.indexOf('people/18') >= 0) {
        counter++;
      }
    }
  }
  console.log(counter);
});
