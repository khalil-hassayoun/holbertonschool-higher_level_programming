#!/usr/bin/node
// Grabs the second biggest of an array
if (process.argv.length <= 3) {
  console.log(0);
  process.exit();
}
let myVar = process.argv.slice(2);
myVar.sort();
console.log(myVar.slice(-2)[0]);
