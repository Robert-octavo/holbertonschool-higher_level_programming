#!/usr/bin/node
// TODO: https://nodejs.dev/en/learn/writing-files-with-nodejs
const fs = require('fs');
const content = process.argv[3];

try {
fs.writeFileSync(process.argv[2], content);
  // file written successfully
} catch (err) {
  console.error(err);
}
