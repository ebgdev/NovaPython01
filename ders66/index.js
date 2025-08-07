// ---------------Functions are object---------------

// function Circle(radius) {
//   this.radius = radius;
//   this.draw = function () {
//     console.log('darw');
//   };
// }

// // So we have multiple avalible methods for our function like objects
// // console.log(Circle.name)
// // console.log(Circle.length)
// // console.log(Circle.constructor)

// const another = new Circle(1); // Circle.call({},1)
// console.log(another);

// const obj = {};
// Circle.call(obj, 1);
// console.log(obj); // { radius: 1, draw: [Function (anonymous)] }

// ---------------Enumerating Properties---------------

// function Circle(radius) {
//   this.radius = radius;
//   this.area = Math.PI * Math.pow(radius, 2);
//   this.draw = function () {
//     console.log('darw');
//   };
// }

// const circle = new Circle(10);
// // for (let key in circle) {
// //   console.log(key, circle[key]);
// // }

// // what if we want to get he properties not the methods.
// // for (let key in circle) {
// //   if (typeof circle[key] != 'function') console.log(key, circle[key]);
// // }

// // KEYS
// const keys = Object.keys(circle);
// console.log(keys); // This will return an array.

// --------------- Abstraction 1---------------

// function Circle(radius) {
//   // 🔒 Private property (not accessible outside)
//   let defaultLocation = { x: 0, y: 0 };

//   // 🔒 Private method (hidden from outside)
//   function computeOptimumLocation(factor) {
//     console.log('Computing optimum location with factor', factor);
//   }

//   // ✅ Public properties
//   this.radius = radius;

//   // ✅ Public method (part of the interface)
//   this.draw = function () {
//     computeOptimumLocation(0.1); // can access private function
//     console.log('draw');
//     console.log('Radius:', this.radius);
//   };

//   // ✅ Public method to get private property (getter)
//   this.getDefaultLocation = function () {
//     return defaultLocation;
//   };

//   // ✅ Public method to set private property (setter with validation)
//   this.setDefaultLocation = function (value) {
//     if (!value.x || !value.y) throw new Error('Invalid location.');
//     defaultLocation = value;
//   };
// }

// const c = new Circle(10);

// c.draw(); // Can call draw

// console.log(c.getDefaultLocation()); // { x: 0, y: 0 }

// c.setDefaultLocation({ x: 5, y: 7 });

// console.log(c.getDefaultLocation()); // { x: 5, y: 7 }

// // Invalid usage (throws error)
// c.setDefaultLocation({ x: 1 }); // ❌ Error: Invalid location.

// --------------- Abstraction 2---------------

// syntax:  Object.defineProperty(obj, propertyName, descriptorObject);
// Bununla bir objeye özelleştirilmiş property (özellik) ekleyebilirsin.

// function Circle(radius) {
//   let defaultLocation = { x: 0, y: 0 };

//   this.radius = radius;

//   this.draw = function () {
//     console.log('draw');
//   };

//   Object.defineProperty(this, 'defaultLocation', {
//     get: function () {
//       return defaultLocation;
//     },
//     set: function (value) {
//       if (!value.x || !value.y) throw new Error('Invalid location.');
//       defaultLocation = value;
//     },
//   });
// }

// const c = new Circle(10);
// c.defaultLocation = { x: 5, y: 5 }; // uses setter
// console.log(c.defaultLocation); // uses getter

// --------------- Challenge 1---------------

// const sw  = new Stopwatch()
// This sw objecs will have few members
// (duration=0) - reset - start - stop

function Stopwatch() {
  let startTime = null,
    endTime = null,
    isRunning = false,
    duration = 0;

  this.start = function () {
    if (isRunning) throw new Error('Stopwatch has already started.');
    isRunning = true;
    startTime = Date.now();
  };

  this.stop = function () {
    if (!isRunning) throw new Error('Stopwatch is not running.');
    isRunning = false;
    endTime = Date.now();
    duration += (endTime - startTime) / 1000; // convert to seconds
  };

  this.reset = function () {
    duration = 0;
    isRunning = false;
    startTime = null;
    endTime = null;
  };

  Object.defineProperty(this, 'duration', {
    get: function () {
      return duration;
    },
  });
}

// console outputs:

// const sw = new Stopwatch();

// const sw = new Stopwatch();
// undefined

// sw.start();
// undefined

// sw.stop();
// undefined

// sw.duration;
// 4.108
