#!/usr/bin/node
// TODO: https://github.com/axios/axios
// TODO: sudo npm install --save axios
// TODO: script that prints the number of movies where the character “Wedge Antilles” is present

const axios = require('axios').default;

axios.get(process.argv[2])
  .then(function (response) {
    // handle success
    let count = 0;
    // console.log(response);// .data.results[0].director);
    // const actor = 'https://swapi-api.hbtn.io/api/people/' + '18' + '/';
    for (let i = 0; response.data.results[i]; i++) {
      // if (response.data.results[i].characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
      //  count++;
      // }
      const info = response.data.results[i].characters;
      // console.log(info);
      info.forEach(element => {
        if (element.search('18') !== -1) {
          count++;
        }
      });
    }
    console.log(count);
  }).catch(error => {
    console.log(error.response.status);
  });
