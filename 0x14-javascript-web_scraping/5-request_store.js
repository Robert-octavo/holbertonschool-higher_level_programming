#!/usr/bin/node
// TODO: Write a script that gets the contents of a webpage and stores it in a file.

const fs = require('fs');
const axios = require('axios').default;

axios.get(process.argv[2])
  .then(function (response) {
    // handle success
    // console.log(response)
    // console.log(response.data);
    try {
      fs.writeFileSync(process.argv[3], response.data, { encoding: 'utf-8', flag: 'w+' });
    } catch (err) {
      console.log(err);
    }
  });/* .catch(error => {
    console.log(error.response.status);
  }); */
