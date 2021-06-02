#!/usr/bin/node
// Tries to convert an argument to an int before printing
if (isNaN(parseInt(process.argv[2]))) { console.log('Not a number'); } else { console.log('My number: ' + parseInt(process.argv[2])); }
