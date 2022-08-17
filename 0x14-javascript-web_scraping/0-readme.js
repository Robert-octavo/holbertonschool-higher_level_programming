#!/usr/bin/node
// TODO: https://nodejs.dev/en/learn/reading-files-with-nodejs
const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
