#!/usr/bin/node
// Query star wars API to count character

const request = require('request');
const url = process.argv[2];
const fs = require('fs');
const file = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    try {
      fs.writeFileSync(file, body, 'utf8');
    } catch (err) {
      console.log(err);
    }
  }
});
