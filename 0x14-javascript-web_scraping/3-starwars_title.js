#!/usr/bin/node

/**
 * script that prints the title of a Star Wars movie
 * where the episode number matches a given integer
 */

const request = require('request');
const api = 'https://swapi-api.hbtn.io/api/films/';
const id = process.argv[2];
const url = api + id;

request(url, { json: true }, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  console.log(body.title);
});
