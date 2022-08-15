#!/usr/bin/node
const args = process.argv.length;
// console.log(args)
// console.log(args === 2 ? 'No argument' : 'Argument found');
console.log(args === 2 ? 'No argument' : args === 3 ? 'Argument found' : 'Arguments found');
