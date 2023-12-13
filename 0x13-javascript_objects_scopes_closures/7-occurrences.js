#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nuOccurrences = 0;
  for (let loop1 = 0; loop1 < list.length; loop1++) {
    if (searchElement === list[loop1]) {
      nuOccurrences++;
    }
  }
  return nuOccurrences;
};
