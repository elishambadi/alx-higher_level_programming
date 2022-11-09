#!/usr/bin/node
for (let x = 0; x < parseInt(process.argv[2]); x++) {
  console.log('C is fun');
}
if (process.argv.length === 2 || Number.isNaN(parseInt(process.argv[2]))) {
  console.log('Missing number of occurrences');
}
