---------------------- ✅ CLASSES ✅-----------------------

classes in js is not like classes in python or java
it's just a syntatic sugar over prototypical inheritance

class Circle {
  constructor(radius) {
    this.radius = radius;
    // if we dont want a method to end up on prototoype
    this.move = function () {
      console.log('move');
    };
  }
  draw() {
    console.log('draw');
  }
}

const c = new Circle(1);
// with classes we inforced to use new keyword.
console.log(c);
console.log(typeof Circle); // function

---------------------- ✅ Hoisting ✅-----------------------

// const c = new Circle(); // Uncaught ReferenceError: Cannot access 'Circle' before initialization

// Class Declaration
class Circle {} // Tercih edilebilir cunku daha basit

// Class Expression - anonymous
const Square = class {}; // Pek bir kullanim alani yok

---------------------- ✅ Static Methods ✅-----------------------

class Circle {
  constructor(radius) {
    this.radius = radius;
  }

  // Instance Method
  draw() {
    console.log(`Drawing a circle with radius ${this.radius}`);
  }

  // Static Method
  static parse(str) {
    const radius = JSON.parse(str).radius;
    return new Circle(radius);
  }
}

// ✅ Correct static method call
const circle = Circle.parse('{ "radius": 1 }');
console.log(circle);
circle.draw();

---------------------- ✅ This Keyword ✅-----------------------

// This Keyword: global in node , windows in browser

const Circle = function () {
  this.draw = function () {
    console.log(this);
  };
};

const c = new Circle();

// Method Call
c.draw();

const draw = c.draw;

// Function Call
draw(); // this will point to the global object.

// Circle {draw: ƒ}
// Window {window: Window, self: Window, document: document, name: '', location: Location, …}

✅ Strict mode

Neden Strict Mode?
- Daha güvenli kod yazarak gizli bug’ları önler.
- this gibi davranışları daha tutarlı hale getirir.
- Gelecek ECMAScript sürümleriyle uyumlu olmanı kolaylaştırır.

'use strict';

const Circle = function () {
  this.draw = function () {
    console.log(this);
  };
};

const c = new Circle();

// Method Call
c.draw();

const draw = c.draw;

// Function Call
draw(); // this will point to the global object.

// output:
// Circle {draw: ƒ}
// undefined

------------ Classes

// JavaScript’te class yapıları, ister "use strict" yazılsın ister yazılmasın,
// her zaman strict mode altında çalışır.
// Bu yüzden class içindeki metotlarda this davranışı, strict mode’un kurallarına
// göre belirlenir:'use strict';

class Circle {
  draw() {
    console.log(this);
  }
}

const circle = new Circle();
const draw = circle.draw;
draw();

---------------------- ✅ Private Members Using Symbols ✅-----------------------

// class Circle {
//   constructor(radius) {
//     this._radius = radius;
//   }
// }

// const c = new Circle(1);
// // c._radius // <-- But as you see it's not private , it's just a convetion

// so in ES6 we have primitive type called Symbol

const _radius = Symbol();

// Symbol is not a constuctor function so there is no need for new keyword.
// _radius biz burada yazilmamis kural gibi kendimiz bu sekilde yaziyoruz.
// a symbol essentially a unique identifier.
// so we can use this id as the property name for an object.
// test this on console --> Symbol() === Symbol() --> false

const _draw = Symbol();

class Circle {
  constructor(radius) {
    this[_radius] = radius;
  }

  [_draw]() {}
}
const c = new Circle(1);
console.log(c);

// Circle {Symbol(): 1}
// so we dont have c.radius or c._radius directly anymore.

---------------------- ✅ Private Members Using WeakMaps ✅-----------------------

const _radius = new WeakMap();
const _draw = new WeakMap();
// WeakMaps are essentially a dictionary where keys are objects
// and values can be anything and the reason that we call them WeakMaps
// because the keys are weak , so if there is no refrences to these keys
// they will be garbage collected.

class Circle {
  constructor(radius) {
    _radius.set(this, radius);
    // here this is our instance object
    // and for the value we are going to use radius argument

    _draw.set(this, function () {
      console.log('draw', this);
    });
  }

  // How we get the radius then.
  getRadius() {
    console.log(_radius.get(this));
  }

  getDraw() {
    console.log(_draw.get(this));

    console.log('getDraw called.');
  }
}

const c = new Circle(1);
console.log(c);
c.getDraw();
c.getRadius();
c.getDraw();

---------------------- ✅ Inheritance ✅-----------------------

class Shape {
  move() {
    console.log('move');
  }
}

class Circle extends Shape {
  draw() {
    console.log('draw');
  }
}

const c = new Circle();
console.log(c);
// we dont have to reset consturctor
c.move();
c.draw();

-------------------

class Shape {
  constructor(color) {
    this.color = color;
  }
  move() {
    console.log('move');
  }
}

class Circle extends Shape {
  constructor(color, radius) {
    super(color);
    this.radius = radius;
  }
  draw() {
    console.log('draw');
  }
}

const c = new Circle('red', 1);
console.log(c);
// we dont have to reset consturctor
c.move();
c.draw();

---------------------- ✅ Stack ✅-----------------------

const _items = new WeakMap();

class Stack {
  constructor() {
    _items.set(this, []);
  }

  push(obj) {
    _items.get(this).push(obj);
  }

  pop() {
    const items = _items.get(this);

    if (items.length === 0) throw new Error('Stack is empty.');

    return items.pop();
  }

  peek() {
    const items = _items.get(this);

    if (items.length === 0) throw new Error('Stack is empty');

    return items[items.length - 1];
  }

  get count() {
    return _items.get(this).length;
  }
}

const stack = new Stack();
stack.push('a');
console.log(stack.peek());
console.log(stack.count);
