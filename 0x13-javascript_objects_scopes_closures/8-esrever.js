#!/usr/bin/node

exports.esrever = function (list) {
  const NewList = [];

  list.forEach(element => {
    NewList.unshift(element);
  });
  return (NewList);
};
