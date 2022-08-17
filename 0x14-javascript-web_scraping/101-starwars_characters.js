#!/usr/bin/node
// TODO: https://github.com/axios/axios
// TODO: sudo npm install --save axios
// let order = [];
const axios = require('axios').default;

axios.get('https://swapi-api.hbtn.io/api/films/' + process.argv[2] + '/')
  .then(function (response) {
    // handle success
    // console.log(response.data.characters[0]);
    // console.log(response.data.title);
    for (let i = 0; response.data.characters[i]; i++) {
      // console.log(response.data.characters[i])
      axios.get(response.data.characters[i])
        .then(function (rest) {
          // console.log(rest.data)
          // let j = 0;
          for (const [key, value] of Object.entries(rest.data)) {
            if (key === 'name') {
              console.log(value);
            }
          }
        });
    }
  }).catch(error => {
    console.log(error.response.status);
  });

