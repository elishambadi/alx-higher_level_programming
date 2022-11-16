#!/usr/bin/node
// Write contents to a file

const fs = require('fs');
try {
  fs.writeFileSync(process.argv[2], process.argv[3]);
} catch (err) {
  console.log(err);
}

