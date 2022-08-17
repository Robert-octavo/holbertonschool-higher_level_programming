#!/usr/bin/node
// TODO: https://github.com/axios/axios
// TODO: sudo npm install --save axios

const axios = require('axios').default;

axios.get('https://swapi-api.hbtn.io/api/films/' + process.argv[2] + '/')
  .then(function (response) {
    // handle success
    console.log(response.data.title);
  }).catch(error => {
    console.log(error.response.status);
  });
