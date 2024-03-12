#!/usr/bin/node

const input = process.argv;
const args = parseInt(input[2]);

if (isNaN(args)) {
    console.log('Missing size')
}
else {
    for (let x = 0; x < args; x++) {
            console.log('X'.repeat(args))
    }
}
