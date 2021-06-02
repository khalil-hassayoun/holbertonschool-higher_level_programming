#!/usr/bin/node
function addMeMaybe (number, theFunction) {
  theFunction(++number);
}
exports.addMeMaybe = addMeMaybe;
