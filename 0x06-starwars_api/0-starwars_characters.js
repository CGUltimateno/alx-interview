#!/usr/bin/node
/**
 * This script prints all characters of a Star Wars movie
 */
const request = require('request');
const { argv } = require('process');
let url = " ";

if (process.argv.length === 3){
   url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}`;
    request(url, function (error, response, body) {
        if (error) {
            console.log(error);
        } else {
            let characters = JSON.parse(body).characters;
            for (let i = 0; i < characters.length; i++) {
                request(characters[i], function (error, response, body) {
                    if (error) {
                        console.log(error);
                    } else {
                        console.log(JSON.parse(body).name);
                    }
                });
            }
        }
    }
    );
}