#!/usr/bin/node
// TODO: Write a function that returns the reversed version of a list:

exports.esrever = function (list) {
  const output = [];
  while (list.length) {
    output.push(list.pop());
  }

  return output;
};
