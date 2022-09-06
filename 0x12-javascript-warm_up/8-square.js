#!/usr/bin/node
const number = parseInt(process.argv[2]);
if (Number.isNaN(number)) {
  console.log('Missing size');
} else {
  for (let i = 0, i < number; i++) {
    let sqr = '';
    for (let j = 0; j < number; j++) {
      sqr += 'X';
    }
    console.log(sqr);
  }
}
