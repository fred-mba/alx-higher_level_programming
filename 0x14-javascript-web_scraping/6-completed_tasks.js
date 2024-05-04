#!/usr/bin/node

const req = require('request');
const url = process.argv[2];

req(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const todos = JSON.parse(body);

  const tasksCompleted = {};

  todos.forEach(todo => {
    if (todo.completed) {
      const userId = todo.userId;
      if (tasksCompleted[userId]) {
        tasksCompleted[userId] +=1;
      } else {
        tasksCompleted[userId] = 1;
      }
    }
  });
  console.log(tasksCompleted);
});
