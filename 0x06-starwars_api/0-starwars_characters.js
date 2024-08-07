#!/usr/bin/node

const { argv } = require('process');
const request = require('request');
const util = require('util');
const movie = argv[2];

const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movie}`;

const requestPromise = util.promisify(request);

async function fetchCharacters () {
  try {
    const { body } = await requestPromise(movieUrl, { json: true });
    const characters = body.characters;

    for (const characterUrl of characters) {
      const { body: characterBody } = await requestPromise(characterUrl, {
        json: true
      });
      console.log(characterBody.name);
    }
  } catch (error) {
    console.error('Error:', error);
  }
}

fetchCharacters();
