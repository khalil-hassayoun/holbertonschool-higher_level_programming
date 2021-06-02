#!/usr/bin/node
// increments the integer value
let myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
myObject.incr = function () { this.value++; };
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
