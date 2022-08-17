#!/usr/bin/node
// TODO: https://github.com/axios/axios
const axios = require('axios');
// const URL = process.argv[2];
// console.log(process.argv[2]);
axios.get(process.argv[2])
  .then(function (response) {
    // handle success
    console.log('code: ' + response.status);
  }).catch(error => {
    console.log('code: ' + error.response.status);
  });
