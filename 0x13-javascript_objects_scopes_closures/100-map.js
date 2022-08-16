#!/usr/bin/node
// TODO: Write a script that imports an array and computes a new array.
const arr = require('./100-data').list;

const arrResult = arr.map((value, index) => value * index);
console.log(arr);
console.log(arrResult);
