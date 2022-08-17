#!/usr/bin/node
// TODO: https://nodejs.dev/en/learn/writing-files-with-nodejs
const axios = require('axios').default;
const URL = process.argv[2];
console.log(URL);
axios.get(URL)
  .then(function (response) {
    // handle success
    console.log(response);
})
