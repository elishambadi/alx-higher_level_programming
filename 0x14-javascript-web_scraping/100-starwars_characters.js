#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/people/';
const movId = process.argv[2];
const movUrl = 'https://swapi-api.alx-tools.com/api/films/' + movId + '/';

const sendRequest = (url) => request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const data = JSON.parse(body);
    for (let x = 0; x < data.results.length; x++) {
      if (data.results[x].films.includes(movUrl)) {
        console.log(data.results[x].name);
      }
    }
    if (data.next) {
      sendRequest(data.next);
    }
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});

sendRequest(url);
