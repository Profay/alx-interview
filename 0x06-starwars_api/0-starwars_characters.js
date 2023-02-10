#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

function getMovieData(id, callback) {
  request(`https://swapi.dev/api/films/${id}/`, function(error, response, body) {
    if (error) {
      console.error("Error: Unable to retrieve data from API.");
      process.exit();
    }
    const data = JSON.parse(body);
    callback(data);
  });
}

function getCharacterData(url, callback) {
  request(url, function(error, response, body) {
    if (error) {
      console.error("Error: Unable to retrieve data from API.");
      process.exit();
    }
    const data = JSON.parse(body);
    callback(data);
  });
}

function displayCharacters(id) {
  getMovieData(id, function(movieData) {
    const characters = movieData.characters;
    for (const characterUrl of characters) {
      getCharacterData(characterUrl, function(characterData) {
        console.log(characterData.name);
      });
    }
  });
}

displayCharacters(movieId);
