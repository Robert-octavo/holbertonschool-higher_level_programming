#!/usr/bin/node
// TODO: Write a function that returns the number of occurrences in a list

exports.nbOccurences = function (list, searchElement) {
  list = list.filter(element => element === searchElement); // TODO: return a list exm: [3, 3, 3]
  return list.length;
};
