#!/usr/bin/node
exports.esrever = function (list) {
  let leng = list.length - 1;
  let loop = 0;
  while ((leng - loop) > 0) {
    const tmp = list[leng];
    list[leng] = list[loop];
    list[loop] = tmp;
    loop++;
    leng--;
  }
  return list;
};
