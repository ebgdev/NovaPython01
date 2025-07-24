// ---✅✅✅------------------- Functions --------------------✅✅✅---

// Function Declarations vs. Expressions

// in JavaScript, there are two main ways to define functions:
function walk() {
  console.log('walk');
}

walk();

// Anonymous Function Expression - we also can give it a name which then called Named  Function Expression

const run = function () {
  console.log('run');
};

let move = run;

walk(); // walk
run(); // run
move(); // run

// --------✅- Hoisting -✅--------
// başa taşınma

// Hoisting is the process in JavaScript where function declarations
// and variable declarations (not assignments) are moved to the top
// of their scope (not necessarily the top of the file) at runtime,
// before code execution.

walk(); // ✅

function walk() {
  console.log('walk');
}

run(); // ❌ js threat this  like a variable

const run = function () {
  console.log('run');
};

// --------✅- Arguments -✅--------
// We also can run in in the chrome console
// callee: is a property of the arguments object that refers to the currently executing function.

function sum(a, b) {
  return a + b;
}

console.log(sum(1, 2));
console.log(sum(1)); // 1 + undefined --> Nan
console.log(sum()); // Nan
console.log(sum(1, 2, 3, 4, 5, 6)); // still we'll get 3

// ------

function sum(a, b) {
  // every function in js have special object called arguments
  console.log(arguments);
  // Symbol.iterator: Lets the arguments object be iterable (e.g., usable in a for...of loop).
  sum = 0;
  for (value of arguments) sum += value;
  return sum;
}

console.log(sum(1, 2, 3, 4, 5, 6));

// --------✅- Rest Operator -✅--------
// In Chrome's console, you'll see that `args` is a real array.
// The rest operator (`...`) collects all remaining arguments passed to the function
// and packs them into an array called `args`.

// rest : turkcede geriye kalanlari alir.

function sum(...args) {
  return args;
}

console.log(sum(1, 2, 3, 4, 5, 6)); // Output: [1, 2, 3, 4, 5, 6]

// -----

function sum(...args) {
  total = 0;
  for (let arg of args) total += arg;
  return total;
}

console.log(sum(1, 2, 3, 4, 5, 6));

// ---- reduce ----

function sum(...args) {
  result = args.reduce((a, b) => a + b);
  return result;
}

console.log(sum(1, 2, 3, 4, 5, 6));

// ---- example ----
// sepet , indirim

function cart(discount, ...items) {
  const total = items.reduce((a, b) => a + b);
  return total * (1 - discount);
}

console.log(cart(0.2, 20, 30, 50));

// ----rest should be used with the last parameter
// ❌ Error
// function cart(discount, ...items,anotherItem❌) {
//   const total = items.reduce((a, b) => a + b);
//   return total * (1 - discount);
// }

// console.log(cart(0.2, 20, 30, 50));

// --------✅- Default Parameters -✅--------

function interest(principal, rate, years) {
  rate = rate || 37;
  years = years || 1;
  return ((principal * rate) / 100) * years;
}

console.log(interest(10000));

// ---- easier way

function interest(principal, rate = 37, years = 1) {
  return ((principal * rate) / 100) * years;
}

console.log(interest(10000));

// ---- what if we dont give the years default value

function interest(principal, rate = 37, years) {
  return ((principal * rate) / 100) * years;
}

console.log(interest(10000)); // ‼️ Nan
console.log(interest(10000, 40)); // Nan
console.log(interest(10000, undefined, 1));

// ‼️ so the way is to use parameters with default value at the end
// or give all of the parameters a default value

// ---- example:

function interest(principal, years, rate = 37) {
  return ((principal * rate) / 100) * years;
}

console.log(interest(10000, 1)); // 3700

// --------✅- Getters & Setters -✅--------

const person = {
  firstName: 'Erfan',
  lastName: 'Bahcivan',
  fullName() {
    return `${this.firstName} ${this.lastName}`;
  },
};

console.log(person.fullName());

// --- what if i want to access the the fullName like property not a method ?
const person = {
  firstName: 'Erfan',
  lastName: 'Bahcivan',
  get fullName() {
    return `${this.firstName} ${this.lastName}`;
  },
};

console.log(person.fullName);

// --- what if i want to set a new value to fullName

const person = {
  firstName: 'Erfan',
  lastName: 'Bahcivan',
  get fullName() {
    return `${this.firstName} ${this.lastName}`;
  },
  set fullName(value) {
    const parts = value.split(' ');
    this.firstName = parts[0];
    this.lastName = parts[1];
  },
};

person.fullName = 'erfan bahcivan';
console.log(person.fullName);
console.log(person);

// output
// {firstName: 'erfan', lastName: 'bahcivan'}
// firstName: "erfan"
// fullName: (...) ‼️ This is actual getter so get the value we should click on it.
// lastName: "bahcivan"
// get fullName: ƒ fullName()
// set fullName: ƒ fullName(value)
// [[Prototype]]: Object

// --------✅- Try & Catch -✅--------

const person = {
  firstName: 'Erfan',
  lastName: 'Bahcivan',

  set fullName(value) {
    if (typeof value !== 'string') {
      throw new Error('Value is not a string.');
    }

    const parts = value.split(' ');
    if (parts.length !== 2) {
      throw new Error('Enter a first and last name.');
    }

    this.firstName = parts[0];
    this.lastName = parts[1];
  },
};

// null
// ""
// "erfan"
try {
  person.fullName = null;
} catch (e) {
  alert(e); // Output: Value is not a string.
}

console.log(person); // Shows updated or original `firstName`, `lastName`
console.log(person.fullName); // Safely gets the full name

// --------✅- Local vs. Global Scope -✅--------

// const color = 'red'; // global scope

function start() {
  // block level variable
  const message = 'hi';
  const color = 'blue';
  console.log(color);
}

function stop() {
  const message = 'bye';
  console.log(message);
}
start(); // call the start function

stop(); // call stop from within start

// --------✅- Let vs Var -✅--------

function start() {
  for (let i = 0; i < 5; i += 1) console.log(i);

  // console.log(i); // out of scope
}

start();

// ------

// var => function-scoped
// ES6 (ES2015): let, const => block-scoped
// ‼️ We will see the i = 4 and then i = 5 because at the last iteration i actually did update to the 5.

function start() {
  for (var i = 0; i < 5; i += 1) console.log(i);

  console.log(i); // out of scope
}

start();

// ------

function start() {
  for (var i = 0; i < 5; i += 1) {
    if (true) {
      var color = 'red';
    }
  }
  console.log(color);
}

start();

// console.log(color); // ❌ Not accessible.

// ------
// // windows object

var color = 'red';
let age = 28;

// now in console if we type window.color = 'red'
// window.age = undefined

// --------✅- This Keyword -✅--------

// // this in object methods → refers to the object 1️⃣ itself .

// // this in regular functions:
// // In the browser, it refers to the window 2️⃣1️⃣ object.
// // In Node.js, it refers to the global 2️⃣2️⃣ object.

const video = {
  title: 'a',
  play() {
    console.log(this);
  },
};

video.play(); // so we get our video object --> { title: 'a', play: [Function: play] }
// in this example because the video is a method in this object so it refers to the video object itself.

// ----

// Even in here the stop is a method
// so we will get the video object itself.

const video = {
  title: 'a',
  play() {
    console.log(this);
  },
};

video.stop = function () {
  console.log(this);
};

video.stop();

----

const video = {
  title: 'a',
  play() {
    console.log(this);
  },
};

// In normal function we should get the windows for the browser so ...
function playVideo() {
  console.log(this);
}

playVideo();

// Window {window: Window, self: Window, document: document, name: '', location: Location, …}
// $_ad_EL: ƒ (e)
// adl_CheckScroll: ƒ ({el:t,fun:e})
// adl_CheckURL: ƒ (t,e)
// adl_Load: ƒ (t)
// adl_Mutation: ƒ (t,e,n="body")
// adl_Open: ƒ (t=!1)
// ...

// ----

// How about the 3️⃣ constructor functions
// here will return the object

function VideoPlay(title) {
  this.title = title;
  console.log(this); // this refers to the new object created by `new`
}

const vp = new VideoPlay('a');
console.log(vp); // Output: { title: 'a' }

// -----

const video = {
  title: 'a',
  tags: ['a', 'b', 'c'],
  showTags() {
    this.tags.forEach(function (tag) {
      console.log(this.title, tag);
    });
  },
};

video.showTags();

// undefined 'a'
// undefined 'b'
// undefined 'c'

// ----
// Lets see the what is "this" ?
// we will get the windows

const video = {
  title: 'a',
  tags: ['a', 'b', 'c'],
  showTags() {
    this.tags.forEach(function (tag) {
      // here the `this` is in the obj, so we should get the object
      // not the window — why is this happening?
      // because `this` here is actually in a normal function
      console.log(this, tag);
    });
  },
};

video.showTags();

// ----

const video = {
  title: 'a',
  tags: ['a', 'b', 'c'],
  showTags() {
    this.tags.forEach(function (tag) {
      console.log(this.title, tag);
      // if we push our object here , can be anything like ✅{firstName:"erfan"} but we use ✅"this".
    }, this);
    // now here this is a part of the showTags execution.
  },
};

video.showTags();

// --------✅- Changing The `value of  This -✅--------

// Approach1: (❌Not recommended)
// lets imagine that the our forEach method dosent have second parameter.
// Here is the solution:
// Notice : Some people also use that instead of self
const video = {
  title: 'a',
  tags: ['a', 'b', 'c'],
  showTags() {
    // we reference self to this
    // so in our callback function we can use self instead of "this"
    // because the value of this changes when a new function is called.
    const self = this;
    this.tags.forEach(function (tag) {
      console.log(this.title, tag);
    });
  },
};

// -----

// Approach2:
// We do know that functions are objects in javascript

function playVideo(a, b) {
  console.log(this);
}

// So this function is technically is an object so it has properties and methods
// that we can access using the dot(.) notation.
// apply - bind - call methods.

// call(thisArg: any, ...argArray: any[]): any
// thisArg: means it gets an object.
playVideo.call({ name: 'erfan' }, 1, 2); // will return : { name: 'erfan' }
playVideo.apply({ name: 'erfan' }, [1, 2]); // will return : { name: 'erfan' }

// --

// this dose not call our playVideo function
// it returns a new function and sets "this" to point to the { name: 'erfan' } object permenatly.
// so no matter how we call the function "this" will always point to the object we set -> { name: 'erfan' }
const fn = playVideo.bind({ name: 'erfan' });
fn(); // will return { name: 'erfan' }

// or

// const fn = playVideo.bind({ name: 'erfan' })(); // will return { name: 'erfan' }

// --

// playVideo(); // will return the windows object.

// // ----
// Now Back to our code:

const video = {
  title: 'a',
  tags: ['a', 'b', 'c'],
  showTags() {
    this.tags.forEach(
      function (tag) {
        console.log(this.title, tag);
      }.bind(this)
    );
  },
};

video.showTags();

// -----

// Approach3:
// Arrow functions inherite "this" from container function
// so in this function this will reference to video object

const video = {
  title: 'a',
  tags: ['a', 'b', 'c'],
  showTags() {
    this.tags.forEach((tag) => {
      console.log(this.title, tag);
    });
  },
};

video.showTags();
