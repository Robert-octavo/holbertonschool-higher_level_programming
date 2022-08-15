#!/usr/bin/node
const number = Math.floor(Number(process.argv[2]));
if (!isNaN(number)) {
  for (let j = 0; j < number; j++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
