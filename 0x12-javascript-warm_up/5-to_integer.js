#!/usr/bin/node
const number = Math.floor(Number(process.argv[2]));
// console.log(number)
// console.log(typeof number == 'number' ? 'My number: ' + Math.floor(number) : 'Not a number')
console.log(!isNaN(number) ? 'My number: ' + number : 'Not a number');
