#!/usr/bin/node
exports.esrever = function (list) {
  const auxArray = [];
  let j = 0;
  for (let i = (list.length - 1); i >= 0; i--) {
    auxArray[j] = list[i];
    j++;
  }
  return auxArray;
};
