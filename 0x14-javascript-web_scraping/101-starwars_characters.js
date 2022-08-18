#!/usr/bin/node
// TODO: https://github.com/axios/axios
// TODO: sudo npm install --save axios
// let order = [];
const axios = require('axios').default;

axios.get('https://swapi-api.hbtn.io/api/films/' + process.argv[2] + '/')
  .then(function (response) {
    const characters = response.data.characters;
    // console.log(characters);
    printCar(characters, 0);
  }).catch(error => {
    console.log(error.response.status);
  });

function printCar (characters, index) {
  // console.log(characters + ' + ' + index);
  axios.get(characters[index])
    .then(function (response) {
      console.log(response.data.name);
      if (index + 1 < characters.length) {
        printCar(characters, index + 1);
      }
    });
}
