#!/usr/bin/node
/**
* A script that computes the number of tasks completed by user id
* The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
* Only print users with completed task
*/

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
        tasksCompleted[userId] += 1;
      } else {
        tasksCompleted[userId] = 1;
      }
    }
  });
  console.log(tasksCompleted);
});
