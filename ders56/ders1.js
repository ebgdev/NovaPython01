Every browser has what we call a JavaScript engine.

• Firefox --> Spider Monkey
• Chrome --> V8
• Safari --> JavaScriptCore (also called Nitro)
• Microsoft Edge (new, Chromium-based) --> V8 (same as Chrome)
• Microsoft Edge (old, pre-Chromium) --> Chakra
• Opera --> V8 (because Opera is now Chromium-based)
• Brave --> V8 (Chromium-based)

in 2009, Ryan Dahl embedded Chrome’s V8 engine into a C++ 
program and called it Node.js .
This was effectively the birth of JavaScript for the backend.

| Feature       | ECMAScript (ECMA)                   | JavaScript (JS)                         |
| ------------- | ----------------------------------- | --------------------------------------- |
| Type          | Specification (Standard)            | Programming Language                    |
| Maintained by | ECMA International (TC39 Committee) | Various vendors (Browsers, Node.js)     |
| Defines       | Syntax, types, control flow, etc.   | Uses ECMAScript + adds browser features |
| Examples      | ES5, ES6, ES2020                    | JavaScript in Chrome, Firefox, Node.js  |





Hello World in js 

Head over to the chrome and then right click and then inspect 
hit over the console tab

then type  console.log("Hello World!")



✅ Hello World in JavaScript
----------------------

Open Google Chrome.
Right-click anywhere on the page and select "Inspect".
Click on the "Console" tab in the Developer Tools.
Type the following and press Enter:

console.log("Hello World!");


You’ll see "Hello World!" printed in the console. 🎉

-----------------------

In the browser console, we can do a lot of things — it's like a mini playground for JavaScript.
Mathematical expressions

•
  2 + 4

•
  alert('Attention');



alert("Hello world!") --> This will show an alert message in chrome page.



// ============Logical Operators===========



true && false     // false (AND)
true || false     // true  (OR)
!true             // false (NOT)


// =============Comparison Operators===============

'5' == 5          // true   (loose equality)
'5' === 5         // false  (strict equality)
'5' != 5          // false
'5' !== 5         // true

3 < 5             // true
5 <= 5            // true
5 > 3             // true
5 >= 6            // false


// ============Truthy / Falsy Values==============


// Falsy values:
Boolean(false)    // false
Boolean(0)        // false
Boolean(-0)       // false
Boolean(0n)       // false
Boolean('')       // false
Boolean(null)     // false
Boolean(undefined)// false
Boolean(NaN)      // false

// Truthy examples:
Boolean('0')      // true
Boolean('false')  // true
Boolean([])       // true
Boolean({})       // true
Boolean(() => {}) // true



// =============Data Types=============



| Type        | Example                     | Description                                |
| ----------- | --------------------------- | ------------------------------------------ |
| `number`    | `42`, `3.14`, `-0`, `NaN`   | Double-precision floating point (no `int`) |
| `bigint`    | `123n`, `9007199254740991n` | For arbitrarily large integers             |
| `string`    | `"hello"`, `'abc'`          | Textual data                               |
| `boolean`   | `true`, `false`             | Logical values                             |
| `undefined` | `undefined`                 | Variable declared but not assigned         |
| `null`      | `null`                      | Intentional absence of any object value    |
| `symbol`    | `Symbol("id")`              | Unique, immutable identifier               |





typeof "hello"       // "string"
typeof 42            // "number"
typeof 10n           // "bigint"
typeof true          // "boolean"
typeof undefined     // "undefined"
typeof null          // "object"    ← historical quirk
typeof Symbol("x")   // "symbol"




| Property               | Value                          |
| ---------------------- | ------------------------------ |
| Is `null` a primitive? | ✅ Yes                          |
| `typeof null`          | `"object"` ❗ (bug, misleading) |
| Is `null` an object?   | ❌ No, it's not an object       |



// =============Variables=============

let name = "Ali";
let age = 25;


| Feature       | `var`             | `let`                   | `const`                 |
| ------------- | ----------------- | ----------------------- | ----------------------- |
| Scope         | Function          | Block                   | Block                   |
| Re-declarable | ✅ Yes             | ❌ No                    | ❌ No                    |
| Updatable     | ✅ Yes             | ✅ Yes                   | ❌ No                    |
| Hoisted       | ✅ Yes (undefined) | ✅ Yes (not initialized) | ✅ Yes (not initialized) |
| Use it today? | 🚫 No             | ✅ Yes                   | ✅ Yes                   |


✅ When to Use What?

Use let for values that can change (e.g. counters, input data)

Use const for values that shouldn't change (e.g. config, fixed arrays/objects)

Avoid var unless you're working with legacy code





// =============String Concatenation=============


let firstName = "John";
let lastName = "Doe";

let fullName = firstName + " " + lastName;

console.log(fullName); // Output: "John Doe"


// =============String + Number=============

let result = "Age: " + 25;
console.log(result); // Output: "Age: 25"


// =============String + Number=============

let result = "10" - 5;
console.log(result); // Output: 5


// =============String * Number=============

let result = "6" * 2;
console.log(result); // Output: 12



// =============Ternary Operator=============

let age = 20;

let message = (age >= 18) ? "You are an adult." : "You are a minor.";

console.log(message);


✅ output : You are an adult.




// =============if...else if...else=============

if (condition1) {
  // code runs if condition1 is true
} else if (condition2) {
  // code runs if condition2 is true (and condition1 is false)
} else {
  // code runs if none of the above conditions are true
}

---------ex1--------

let score = 75;

if (score >= 90) {
  console.log("Grade: A");
} else if (score >= 80) {
  console.log("Grade: B");
} else if (score >= 70) {
  console.log("Grade: C");
} else {
  console.log("Grade: F");
}

---------ex2--------


// if (hour >= 6 && hour < 12) console.log('Good Morning...');
// else if (hour > 12 && hour < 18) console.log('Good afternoon...');
// else console.log('Good evening');


// =============switch=============

// switch (new Date().getDay()) {
//   case 0:
//     day = 'Sunday';
//     break;
//   case 1:
//     day = 'Monday';
//     break;
//   case 2:
//     day = 'Tuesday';
//     break;
//   case 3:
//     day = 'Wednesday';
//     break;
//   case 4:
//     day = 'Thursday';
//     break;
//   case 5:
//     day = 'Friday';
//     break;
//   case 6:
//     day = 'Saturday';
// }


Use **break** to stop after a matching case.

Without it, code will fall through to the next case(s).

The **default** case is optional. It runs if no match is found.



// =============function=============

// function test(name) {
//   console.log(`your name is: ${name}`);
// } 

// test('erfan');

---------ex2--------

// function iteration(lst) {
//   for (let i = 0; i < lst.length; i++) {
//     for (let j = 0; j < lst[i].length; j++) {
//       console.log(lst[i][j]);
//     }
//     console.log();
//   }
// }

---------ex3--------

function checkOddOrEven(numbers) {
  for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] % 2 === 0) {
      console.log('even');
    } else {
      console.log('odd');
    }
  }
}

// Example usage:
checkOddOrEven([2, 3, 4, 5]);
