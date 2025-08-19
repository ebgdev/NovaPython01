// function Circle(radius) {
//   this.radius = radius;
//   this.run = function () {
//     console.log('run');
//   };
// }

// Circle.prototype.draw = function () {
//   console.log('draw');
// };

// Circle.prototype.duplicate = function () {
//   console.log('duplicate');
// };

// // Make the constructor property enumerable
// Object.defineProperty(Circle.prototype, 'constructor', {
//   enumerable: true,
// });

// // Now check
// const descriptors1 = Object.getOwnPropertyDescriptors(Circle.prototype);
// console.log(descriptors1.constructor.enumerable); // true

// // You can iterate over prototype properties
// for (let key in Circle.prototype) {
//   console.log(key); // draw, duplicate, constructor
// }

// const circle = new Circle(10);

// const x = Object.getPrototypeOf(circle);
// const y = Object.getOwnPropertyDescriptors(circle);
// const descriptors = Object.getOwnPropertyDescriptors(x);

// console.log(x);
// console.log('---------------');
// console.log(y);
// console.log('---------------');
// console.log(descriptors);
// console.log('---------------');
// console.log(descriptors1);

// ----------------------// ✅ CREATING OUR OWN PROTOTYPICAL INHERITANCE ✅-----------------------

// // we dont want to repeat our self by writing 2 time the exact code for both Circle , Square

// function Circle(radius) {
//   this.radius = radius;
// }

// Circle.prototype.draw = function () {
//   console.log('draw');
// };

// Circle.prototype.duplicate = function () {
//   console.log('duplicate');
// };

// function Square() {
//   // code
// }

// Square.prototype.duplicate = function () {
//   console.log('duplicate');
// };

// // ----------------------------------
// // so we use inheritance

// function Shape() {}

// Shape.prototype.duplicate = function () {
//   console.log('duplicate');
// };

// // Circle.prototype = Object.create(Object.prototype); // Circle.prototype before the inheritance happens
// Circle.prototype = Object.create(Shape.prototype);

// function Circle(radius) {
//   this.radius = radius;
// }

// Circle.prototype.draw = function () {
//   console.log('draw');
// };

// const s = new Shape();
// const c = new Circle(10);

// ----------------------// ✅ RESETING THE CONSTRUCTOR ✅-----------------------

// function Shape() {}

// Shape.prototype.duplicate = function () {
//   console.log('duplicate');
// };

// function Circle(radius) {
//   this.radius = radius;
// }

// // Inherit from Shape
// Circle.prototype = Object.create(Shape.prototype);
// // --------------
// // Object.create ile miras alındığında constructor resetlenir.
// // Biz Circle.prototype.constructor = Circle; diyerek doğru referansı geri yüklüyoruz.
// Circle.prototype.constructor = Circle;
// // --------------

// Circle.prototype.draw = function () {
//   console.log('draw');
// };

// const s = new Shape();
// const c = new Circle(10);

// ----------------------// ✅ CALLING THE SUPER CONSTRUCTOR ✅-----------------------

// function Shape(color) {
//   this.color = color;
// }

// Shape.prototype.duplicate = function () {
//   console.log('duplicate');
// };

// Circle.prototype = Object.create(Shape.prototype);
// Circle.prototype.constructor = Circle;
// // call yerine apply : Shape.apply(this, [color]) da kullanabilirdik ama bind pek uygun degil
// function Circle(radius, color) {
//   Shape.call(this, color);
//   this.radius = radius;
// }

// Circle.prototype.draw = function () {
//   console.log('draw');
// };

// const s = new Shape();
// const c = new Circle(10, 'red');

// ----------------------// ✅ INTERMEDIATE FUNCTION INHERITANCE ✅-----------------------

// lets add another shape , this time lets add a square

// ❌ Kotu yontem ----------------
// function Shape(color) {
//   this.color = color;
// }

// Shape.prototype.duplicate = function () {
//   console.log('duplicate');
// };

// Circle.prototype = Object.create(Shape.prototype);
// Circle.prototype.constructor = Circle;

// function Circle(radius, color) {
//   Shape.call(this, color);
//   this.radius = radius;
// }

// Circle.prototype.draw = function () {
//   console.log('draw');
// };

// function Square(size, color) {
//   Shape.call(this, color);
//   this.size = size;
// }

// Square.prototype = Object.create(Shape.prototype);
// Square.prototype.constructor = Square;

// const s = new Shape();
// const c = new Circle(10, 'red');
// const sq = new Square(20, 'red');

// ✅ iyi yontem ----------------

// function extend(Child, Parent) {
//   Child.prototype = Object.create(Parent.prototype);
//   Child.prototype.constructor = Child;
// }

// function Shape(color) {
//   this.color = color;
// }

// Shape.prototype.duplicate = function () {
//   console.log('duplicate');
// };

// function Circle(radius, color) {
//   Shape.call(this, color);
//   this.radius = radius;
// }

// extend(Circle, Shape);

// function Square(size, color) {
//   Shape.call(this, color);
//   this.size = size;
// }

// extend(Square, Shape);

// const s = new Shape();
// const c = new Circle(10, 'red');
// const sq = new Square(20, 'blue');

// ----------------------// ✅ METHOD OVERRIDING AND POLYMORPHISM ✅-----------------------

// function extend(Child, Parent) {
//   Child.prototype = Object.create(Parent.prototype);
//   Child.prototype.constructor = Child;
// }

// function Shape(color) {
//   this.color = color;
// }

// Shape.prototype.duplicate = function () {
//   console.log('duplicate');
// };

// function Circle(radius, color) {
//   Shape.call(this, color);
//   this.radius = radius;
// }

// extend(Circle, Shape);
// // using different prototype
// Circle.prototype.duplicate = function () {
//   console.log('duplicate circle');
// };

// function Square(size, color) {
//   Shape.call(this, color);
//   this.size = size;
// }

// extend(Square, Shape);

// // using same duplicate prototype as shape
// Square.prototype.duplicate = function () {
//   Shape.prototype.duplicate.call(this);
// };

// // override should happend after extend , because we are reseting constructor

// const s = new Shape();
// const c = new Circle(10, 'red');
// const sq = new Square(20, 'blue');

// // // in console:
// // s.duplicate();
// // sq.duplicate();
// // c.duplicate();

// const shapes = [new Circle(), new Square()];

// for (const shape of shapes) {
//   shape.duplicate();
// }
