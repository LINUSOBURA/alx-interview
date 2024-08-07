#!/usr/bin/node

const { argv } = require("process");
const request = require("request");
const util = require("util");
const movie = argv[2];

const movie_url = `https://swapi-api.alx-tools.com/api/films/${movie}`;

const requestPromise = util.promisify(request);

async function fetchCharacters() {
  try {
    const { body } = await requestPromise(movie_url, { json: true });
    const characters = body.characters;

    for (const character_url of characters) {
      const { body: characterBody } = await requestPromise(character_url, {
        json: true,
      });
      console.log(characterBody.name);
    }
  } catch (error) {
    console.error("Error:", error);
  }
}

fetchCharacters();
