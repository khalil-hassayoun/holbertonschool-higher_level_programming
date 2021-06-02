#!/usr/bin/node
// Prints a square of x Xs
if (process.argv.length === 2 || isNaN(parseInt(process.argv[2]))) {
  console.log('Missing size');
} else {
  const times = parseInt(process.argv[2]);
  process.argv[2] = parseInt(process.argv[2]);
  for (process.argv[2]; process.argv[2] > 0; process.argv[2]--) {
    console.log('X'.repeat(times));
  }
}
