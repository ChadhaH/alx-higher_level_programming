#!/usr/bin/node
const dict = require('./101-data').dict;

const totallist = Object.entries(dict);
const val = Object.values(dict);
const valUniq = [...new Set(val)];
const newDict = {};
for (const loop1 in valUniq) {
  const list = [];
  for (const loop2 in totallist) {
    if (totallist[loop2][1] === valUniq[loop1]) {
      list.unshift(totallist[loop2][0]);
    }
  }
  newDict[valUniq[loop1]] = list;
}
console.log(newDict);
