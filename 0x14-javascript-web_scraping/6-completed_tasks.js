#!/usr/bin/node
// TODO: Write a script that gets the contents of a webpage and stores it in a file.

const axios = require('axios').default;

axios.get(process.argv[2])
  .then(function (response) {
    // handle success
    // console.log(response)
    // console.log(response.data);
    const count = {};
    // const num = 0;
    for (let i = 0; response.data[i]; i++) {
      if (response.data[i].completed === true) {
        // count[response.data[i].userId] = num;
        // num++;
        if (isNaN(count[response.data[i].userId])) {
          count[response.data[i].userId] = 0;
        } else {
          count[response.data[i].userId] += 1;
        }
      }
    }
    console.log(count);
  });/* .catch(error => {
    console.log(error.response.status);
  }); */
