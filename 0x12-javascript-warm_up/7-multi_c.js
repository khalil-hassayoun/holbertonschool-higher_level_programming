#!/usr/bin/node
// Prints  a number x amount of times
if (process.argv.length === 2) {
  console.log('Missing number of occurrences');
} else if (parseInt(process.argv[2]) > 0) {
  console.log('C is fun\n'.repeat(parseInt(process.argv[2])).slice(0, -1));
}
while (1) { process.exit(); }
