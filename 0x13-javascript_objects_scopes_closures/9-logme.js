#!/usr/bin/node
// TODO: Write a function that prints the number of arguments already printed and the new argument value.
let argNumber = 0;
exports.logMe = function (item) {
  console.log(argNumber++ + ': ' + item);
};
