// ✅ Inheritance 1 ✅

// /*
//   Prototype
//       ↑
//   objectBase
//    ↙     ↘
//   x       y

// - `x` and `y` share the same prototype object (`objectBase`).
// - `objectBase` itself is linked to a higher-level prototype (`Prototype`).
// */

// // -----

// let x = {};
// console.log(x);

// // [[Prototype]]: Object

// // -----

// let y = {};

// console.log(Object.getPrototypeOf(x) === Object.getPrototypeOf(y));

// // we also can use (__proto__) but now days it's out of use

// console.log(x.__proto__ === y.__proto__);

// ----------------------// ✅ Inheritance 2 ✅-----------------------

// let myArray = [];

// // Now if in the console i write myArray we will see bunch of methods avalible
// // length: 0
// // [[Prototype]]: Array(0) ...
// // indexOf, push , ...

// // Multi level inheritance

// //                -----> objectBase
// //               |
// //     -----> arrayBase
// //    |
// // myArray

// // How about the constructor function that we made ?

// function Circle(radius) {
//   this.radius = radius;
//   this.draw = function () {
//     console.log('draw');
//   };
// }

// const circle = new Circle(10);

// //                -----> objectBase
// //               |
// //     -----> circleBase
// //    |
// // circle

// ----------------------// ✅ Property Descriptor 3 ✅-----------------------

// // Property descriptor, bir özelliğin sadece “değerini” değil, nasıl davranacağını da tarif eder.
// // Bazı özellikler (toString gibi) enumerable: false olduğu için döngülerde görünmez.
// // Object.getOwnPropertyDescriptor ile bu meta veriyi görebilir, Object.defineProperty ile değiştirebilirsin.

// let person = { name: 'erfan' };
// console.log(person);

// // {name: 'erfan'}
// //    └── [[Prototype]]: Object.prototype
// //          ├── constructor: Object()
// //          ├── hasOwnProperty()
// //          ├── isPrototypeOf()
// //          ├── propertyIsEnumerable()
// //          ├── toLocaleString()
// //          ├── toString() ✅
// //          ├── valueOf()
// //          ├── __defineGetter__()
// //          ├── __defineSetter__()
// //          ├── __lookupGetter__()
// //          ├── __lookupSetter__()
// //          └── __proto__

// console.log(person.toString()); // [object Object] and it works.

// // However if we iterate over the members of this object
// // we are not going to see this method

// for (let key in person) console.log(key); // name
// // or
// console.log(Object.keys(person)); // [ 'name' ]

// // so how we can't iterate over all these properties and methods defined ?
// // the reason is because in javascript our properties have attributes attached to them
// // sometime these attributes prevent property from being enumerated

// let objectBase = Object.getPrototypeOf(person);
// let descrioptor = Object.getOwnPropertyDescriptor(objectBase, 'toString');
// console.log(descrioptor);

// // { writable: true, enumerable: false, configurable: true, value: ƒ }
// //    ├── writable: true     --> so we can overwrite this method
// //    ├── enumerable: false  --> so it's not iterable (so we cant see the toString method because it's in the descriptor)
// //    ├── configurable: true --> we can delete this if we want to.
// //    ├── value: function toString()
// //    │       ├── length: 0
// //    │       ├── name: "toString"
// //    │       ├── arguments: (...)
// //    │       ├── caller: (...)
// //    │       ├── [[Prototype]]: Function.prototype
// //    │       └── [[Scopes]]: Scopes[0]
// //    └── [[Prototype]]: Object.prototype
// //            ├── constructor: Object()
// //            ├── hasOwnProperty()
// //            ├── isPrototypeOf()
// //            ├── propertyIsEnumerable()
// //            ├── toLocaleString()
// //            ├── toString()
// //            ├── valueOf()
// //            ├── __defineGetter__()
// //            ├── __defineSetter__()
// //            ├── __lookupGetter__()
// //            ├── __lookupSetter__()
// //            └── __proto__

// // peki bu davranislari biz nasil istedigimiz tarzda yapabilirz ?
// // Object.defineProperty(obj, propName, descriptor)

// Object.defineProperty(person, 'name', {
//   // we do see get: and set:
//   writable: false,
//   enumerable: false,
//   configurable: false,
// });

// person.name = 'ebg';
// console.log(person); // we still get { name: 'erfan' } because we set writable to false
// console.log(Object.keys(person)); // [] , if we set enumerable: true --> ['name']
// delete person.name;

// console.log(person); // name still will be there {name: 'erfan'}

// ------

// let person = { name: 'erfan' };

// // 1️⃣ Kendi özellikleri (görünmeyenler dahil)
// console.log(Object.getOwnPropertyNames(person));
// // ["name"]

// // 2️⃣ Prototipteki tüm özellikleri almak
// let proto = Object.getPrototypeOf(person);
// console.log(Object.getOwnPropertyNames(proto));
// // ["constructor", "hasOwnProperty", "isPrototypeOf", "propertyIsEnumerable",
// //  "toLocaleString", "toString", "valueOf", "__defineGetter__", "__defineSetter__",
// //  "__lookupGetter__", "__lookupSetter__"]

// // 3️⃣ Hatta descriptor bilgileriyle beraber
// let allProtos = Object.getOwnPropertyDescriptors(proto);
// for (const [name, desc] of Object.entries(allProtos)) {
//   console.log(name, desc);
// }

// ----------------------// ✅ Constructor Prototypes 4 ✅-----------------------

// let array = [];
// console.log(array.__proto__);
// console.log(Array.prototype);

// function Circle(radius) {
//   this.radius = radius;
//   this.draw = function () {
//     console.log('draw');
//   };
// }

// const circle = new Circle(10);
// console.log(circle.__proto__);
// console.log(Circle.prototype);

// // so these are exactly the same
// // JavaScript’te her fonksiyonun bir prototype özelliği vardır ve bu özellik,
// // o fonksiyon ile oluşturulan nesnelerin miras alacağı özellikleri/methodları tanımlar.
// // Bir nesnenin __proto__ özelliği ise, o nesnenin hangi prototipten miras aldığını gösterir.
// // __proto__, aslında nesnenin internal [[Prototype]] bağlantısına erişim sağlar.

// ----------------------// ✅ Prototype vs. Instance Members 5 ✅-----------------------

// // -------- VERSION 1: Method inside the constructor --------
// function CircleV1(radius) {
//   this.radius = radius;
//   this.draw = function () {
//     console.log('draw');
//   };
// }

// const c1_v1 = new CircleV1(1);
// const c2_v1 = new CircleV1(1);

// console.log('=== VERSION 1: draw is inside each object ===');
// console.log(c1_v1); // draw appears directly on the object
// console.log(c2_v1); // draw appears directly on the object
// console.log(c1_v1.draw === c2_v1.draw); // false (different copies in memory)

// // -------- VERSION 2: Method on the prototype --------
// function CircleV2(radius) {
//   this.radius = radius;
// }

// CircleV2.prototype.draw = function () {
//   console.log('draw');
// };

// const c1_v2 = new CircleV2(1);
// const c2_v2 = new CircleV2(1);

// console.log('\n=== VERSION 2: draw is on the prototype ===');
// console.log(c1_v2); // draw is NOT inside object, found under [[Prototype]]
// console.log(c2_v2); // draw is NOT inside object, found under [[Prototype]]
// console.log(c1_v2.draw === c2_v2.draw); // true (same shared function in memory)

// // Key takeaway:
// // Inside constructor → Method belongs to each instance (more memory, method visible directly on object).
// // On prototype → Method is shared between instances (less memory, method in [[Prototype]]).

// ----------------------// ✅ Iterating Instance and Prototype Members 6 ✅-----------------------

function Circle(radius) {
  // Instance members
  this.radius = radius;
  this.move = function () {
    console.log('move');
  };
}

const c1 = new Circle(1);

// Prototype members
Circle.prototype.draw = function () {
  console.log('draw');
};

// Returns instance members only
console.log(Object.keys(c1)); // [ 'radius', 'move' ]

// Test both methods
// c1.move(); // "move"
// c1.draw(); // "draw"

// returns all members
for (let key in c1) console.log(key); // radius move draw

console.log(c1.hasOwnProperty('radius')); // true
console.log(c1.hasOwnProperty('draw')); // false
