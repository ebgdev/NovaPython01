// script.js
const addTaskBtn = document.getElementById('addTaskBtn');
const taskInput = document.getElementById('taskInput');
const taskDateTime = document.getElementById('taskDateTime');
const taskList = document.getElementById('taskList');

let tasks = [];

addTaskBtn.addEventListener('click', addTask);
taskInput.addEventListener('keypress', function (e) {
  if (e.key === 'Enter') addTask();
});

function addTask() {
  const taskText = taskInput.value.trim();
  const taskDateTimeValue = taskDateTime.value;
  if (taskText === '' || taskDateTimeValue === '') {
    alert('Invalid Date or Time');
    return;
  }

  const timestamp = new Date(taskDateTimeValue);
  const task = {
    text: taskText,
    time: timestamp,
  };

  tasks.push(task);
  tasks.sort((a, b) => a.time - b.time);

  renderTasks();

  taskInput.value = '';
  taskDateTime.value = '';
  taskInput.focus();
}

function removeTask(button) {
  const index = button.getAttribute('data-index');
  tasks.splice(index, 1);
  renderTasks();
}

function editTask(button) {
  const index = button.getAttribute('data-index');
  const newText = prompt('Edit your task:', tasks[index].text);
  if (newText !== null && newText.trim() !== '') {
    tasks[index].text = newText.trim();
    renderTasks();
  }
}

function renderTasks() {
  taskList.innerHTML = '';

  tasks.forEach((task, index) => {
    const li = document.createElement('li');
    const timeString = task.time.toLocaleString();
    li.innerHTML = `
      <div>
        <strong>${task.text}</strong>
        <div class="timestamp">${timeString}</div>
      </div>
      <div class="buttons">
        <button data-index="${index}" onclick="editTask(this)">Edit</button>
        <button data-index="${index}" onclick="removeTask(this)">Delete</button>
      </div>
    `;
    taskList.appendChild(li);
  });
}
