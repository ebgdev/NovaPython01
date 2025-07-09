// --------------OOP--------------

// const circle = {
//   radius: 1,
//   location: {
//     x: 1,
//     y: 1,
//   },
//   isVisible: true,
//   draw: function () {
//     console.log('draw');
//   },
// };

// circle.draw();

// --------------Factory-Function--------------
// Camel Notation: oneTwoThree

// step1
// function createCircle(radius, location) {
//   const circle = {
//     radius: radius,
//     location: location,
//     isVisible: true,
//     draw: function () {
//       console.log('draw');  // --> undefined
//     },
//   };
//   return circle;
// }

// const circle1 = createCircle(1, 1);
// console.log(circle1.draw());

// ---------

// step2
// function createCircle2(radius, location) {
//   const circle = {
//     radius,
//     location,
//     isVisible: true,
//     draw() {
//       console.log('draw'); // --> undefined
//     },
//   };
//   return circle;
// }

// const circle2 = createCircle2(1, 1);
// console.log(circle2.draw());

// --------------Constructor-Function--------------

// Pascal Notation : OneTwoThree

// function Circle(radius, location) {
//   this.radius = radius;
//   this.location = location;
//   this.draw = function () {
//     console.log('draw');
//   };
// }
// const circle3 = new Circle(10, 10);
// console.log(circle3);
// console.log(circle3.radius);

// --------------Dynamic-Nature-of-Objects------------

// const circle = {
//   radius: 1,
// };

// circle.color = 'yellow';
// circle.draw = function () {};

// console.log(circle); // --> { radius: 1, color: 'yellow', draw: [Function (anonymous)] }

// console.log(circle.draw); // --> [Function (anonymous)]

// delete circle.color;

// console.log(circle); // --> { radius: 1, draw: [Function (anonymous)] }

// // circle = {} // --> Error

// --------------Constructor-Property------------

// // Factory Function
// function createCircle(radius) {
//   return {
//     radius,
//     draw: function () {
//       console.log('draw');
//     },
//   };
// }

// const circle = createCircle(1);
// circle.draw(); // Output: draw

// // Constructor Function
// function Circle(radius) {
//   this.radius = radius;
//   this.draw = function () {
//     console.log('draw');
//   };
// }

// const another = new Circle(1);
// another.draw(); // Output: draw

// console.log(another.constructor); // [Function: Circle] also try this on web console

// //-------

// // console.log(another.constructor);

// //In on web console

// // ƒ Circle(radius) {
// //   this.radius = radius;
// //   this.draw = function () {
// //     console.log('draw');
// //   };
// // }

// console.log(circle.constructor); // [Function: Object]

// //-------

// // console.log(another.constructor);

// //In on web console

// // ƒ Object() { [native code] }

//--------------------------------

// let x = {};
// console.log(x.constructor);

// let y = new Object();
// console.log(y.constructor);

// // so both are the same

//--------------------------------

// using Literals are easier

// // String Literals
// let firstName = 'Erfan';
// let lastName = 'Bahcivan';
// let greeting = `Hello, ${firstName}`;

// // Boolean Literals
// let isOnline = true;
// let isMarried = false;

// // Number Literals
// let age = 28; // integer
// let height = 1.75; // float
// let hex = 0xff; // hexadecimal (255)
// let binary = 0b1010; // binary (10)
// let octal = 0o77; // octal (63)

// // Output
// console.log(firstName); // "Erfan"
// console.log(lastName); // "Bahcivan"
// console.log(greeting); // "Hello, Erfan"

// console.log(isOnline); // true
// console.log(isMarried); // false

// console.log(age); // 28
// console.log(height); // 1.75
// console.log(hex); // 255
// console.log(binary); // 10
// console.log(octal); // 63

// --------------Value-vs-Reference-Types-----------

// let x = 10;
// let y = x;

// x = 20;

// console.log(x); // --> 20
// console.log(y); // --> 10

//-----------

// let x = { value: 10 };
// let y = x;

// x.value = 20;

// console.log(x.value);

// burada x kendisi bir deger degil objenin adresini tutuyor
// ve sonra y'yi ona esitliyor bu durumda obje degistinde
// y de degisecek.

//-----challenge1------

// let number = 10;

// function increase(number) {
//   number++;
// }

// increase(number);
// console.log(number);

//-----challenge2------

let obj = { value: 10 };

function increase(obj) {
  obj.value++;
}

increase(obj);
console.log(obj);

// ---------Enumerating-Properties-of-an-Object---------

// const circle = {
//   radius: 1,
//   draw() {
//     console.log('draw');
//   },
// };

// for (let key in circle) console.log(key);

// for (let key in circle) console.log(key, circle[key]);

// for (let key of Object.keys(circle)) console.log(key);

// for (let [key, value] of Object.entries(circle)) console.log(key, value);

// ----using in----
// if ('draw' in circle) console.log('yes');
// else console.log('No');

// // 'draw' in circle;       // ✅ true (key)
// // 'draw' in circle.draw;  // ❌ false (draw is a function, doesn't have a 'draw' key)
// // 1 in circle;            // ❌ false (1 is not a key — it's a value)

// ---------Cloning-an-Object---------

// const circle = {
//   radius: 1,
//   draw() {
//     console.log('draw');
//   },
// };

// older approach
// const another = {};
// for (let key in circle) another[key] = circle[key];
// console.log(another);

// newer approach
// ‼️ syntax --> Object.assign(target object, source object);
// const another = Object.assign({}, circle);
// console.log(another);

// ‼️ our target object dosen't have to be empty
// it can have some property in it

// const another = Object.assign(
//   {
//     color: 'yellow',
//   },
//   circle
// );

// console.log(another);

// ----spread-operator----
// ✅ more simpilar and shorter
// const another = { ...circle };
// console.log(another);

// ---------Garbage-Collector---------
// JavaScript has an automatic garbage collector.
// It frees up memory by removing objects that are no longer used or referenced.
// We don't control it directly — the engine decides when to clean up.

// let circle = {};
// console.log(circle);

// ---------Math---------
// 🔗 https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math

// console.log(Math.random());
// console.log(Math.round(1.1));
// console.log(Math.max(1, 2, 3, 5, 6));
// console.log(Math.min(1, 2, 3, 5, 6));

// ---------String---------

// const message = '  Hi from js'; // primitive string
// const another = new String('Hi from js'); // String object

// console.log(message); // Output: Hi
// console.log(another); // Output: [String: 'Hi']

// console.log(typeof message); // Output: string
// console.log(typeof another); // Output: object

// // When we use dot notation on a primitive string,
// // JavaScript temporarily wraps it in a String object
// // so we can access properties and methods (like .length or .toUpperCase()).
// // This is called "autoboxing" and it's done automatically behind the scenes.

// console.log(message.length);
// console.log(message[0]);
// console.log(message[1]);

// console.log(message.includes('from'));
// console.log(message.includes('hi'));

// console.log(message.startsWith('Hi'));
// console.log(message.endsWith('js'));

// console.log(message.indexOf('js'));
// console.log(message.replace('js', 'python')); // dose not change the original one

// console.log(message);

// console.log(message.toUpperCase());
// console.log(message.toLowerCase());

// console.log(message.trim());

// ---------------Challenge1-------------

// create an address object
// which contains
// street
// city
// zipCode
// showAddress(address) function that shows the address

// let address = {
//   street: 'a',
//   city: 'b',
//   zipCode: 'c',
// };

// function showAddress(address) {
//   for (let [key, value] of Object.entries(address)) {
//     console.log(key, value);
//   }
// }

// showAddress(address);
