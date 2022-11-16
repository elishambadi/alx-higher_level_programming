#!/usr/bin/node
// Query star wars API to count character

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let counter = 0;
    const films = JSON.parse(body).results;
    for (let i = 0; i < films.length; i++) {
      const chars = films[i].characters;
      const present = chars.includes('https://swapi-api.hbtn.io/api/people/18/');
      if (present) {
        counter++;
      }
    }
    console.log(counter);
  }
});
