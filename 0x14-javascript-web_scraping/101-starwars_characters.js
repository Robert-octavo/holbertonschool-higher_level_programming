#!/usr/bin/node
// TODO: https://github.com/axios/axios
// TODO: sudo npm install --save axios

const { link } = require('fs');

// let order = [];
const axios = require('axios').default;

axios.get('https://swapi-api.hbtn.io/api/films/' + process.argv[2] + '/')
  .then(function (response) {
    // handle success
    // console.log(response.data.characters[0]);
    // console.log(response.data.title);
    // for (let i = 0; response.data.characters[i]; i++) {
    // console.log(response.data.characters[i])
    response.data.characters.forEach(link => {
      axios.get(link)
        .then(function (response) {
          // console.log(link);
          console.log(response.data.name);
        });
    });

    // }
  }).catch(error => {
    console.log(error.response.status);
  });
