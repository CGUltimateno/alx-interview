#!/usr/bin/node
/**
 * This script prints all characters of a Star Wars movie
 */
const request = require('request');
const { argv } = require('process');
let url = " ";

if (argv.length === 3) {
  url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}`;
  request(url, (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }

    getCharacter(JSON.parse(body).characters, 0);
  });
}

function getCharacter (characters, i) {
    if (i === characters.length) {
        return;
    }

    request(characters[i], (error, response, body) => {
        if (error) {
        console.error(error);
        return;
        }

        console.log(JSON.parse(body).name);
        getCharacter(characters, i + 1);
    });
}