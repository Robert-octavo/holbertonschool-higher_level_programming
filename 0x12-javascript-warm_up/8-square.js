#!/usr/bin/node
const number = Math.floor(Number(process.argv[2]));
if (!isNaN(number)) {
  for (let j = 0; j < number; j++) {
    console.log('X'.repeat(number));
  }
} else {
  console.log('Missing size');
}
