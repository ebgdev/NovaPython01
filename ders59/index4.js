// ---------------Date-------------

// const now = new Date();
// console.log(now.toLocaleString('tr-TR'));
// const date1 = new Date('Jul 8 2025 21:00');

// new Date(year, monthIndex, day, hours, minutes)
// monthIndex: Zero-based (i.e., 0 is January, 6 is July)
// day: One-based (days start from 1, not 0)
// const date2 = new Date(2025, 6, 8, 21, 30);

// console.log(date1);
// console.log(date2);
// console.log(date2.toString());

// const now1 = now.toLocaleString();
// console.log(now1);

// console.log(now.toLocaleString('tr-TR')); // e.g. 08.07.2025 19:10:07

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

// ---------------Challenge2-------------
// Initialize an address object
// with both factory functions and constructor functions

// factory function

// // step1.2
// let address = createAddress('a', 'b', 'c');

// // step1.3
// console.log(address);

// // step1.1
// function createAddress(street, city, zipCode) {
//   return {
//     street,
//     city,
//     zipCode,
//   };
// }

// factory function

// let address = new Address('a', 'b', 'c');

// console.log(address);

// function Address(street, city, zipCode) {
//   this.street = street;
//   this.city = city;
//   this.zipCode = zipCode;
// }

// ---------------Challenge3-------------
// object equality

// let address1 = new Address('a', 'b', 'c');
// let address2 = new Address('a', 'b', 'c');

// console.log(address1);

// function Address(street, city, zipCode) {
//   this.street = street;
//   this.city = city;
//   this.zipCode = zipCode;
// }

// // only check for value , esitler mi ?
// function areEqual(address1, address2) {
//   return (
//     address1.street === address2.street &&
//     address1.city === address2.city &&
//     address1.zipCode === address2.zipCode
//   );
// }

// // check for reference, aynilar mi ?
// function areSame(address1, address2) {
//   return address1 === address2;
// }

// console.log(areEqual(address1, address2));
// console.log(areSame(address1, address2));

// let address3 = address2;
// console.log(areSame(address3, address2));

// ---------------Challenge4-------------
// Create a Blog Post Object
// which contains

// title
// body
// author
// views
// comments , each comment should have (author, body)
// isLive

// let post = {
//   title: 'a',
//   body: 'b',
//   author: 'c',
//   views: 10,
//   comments: [
//     { author: 'a', body: 'b' },
//     { author: 'a', body: 'b' },
//   ],
//   isLive: true,
// };

// console.log(post);

//--------------------------------------

// - ✅ Arrays

// -----------Adding-elements-----------

// const numbers = [3, 5];

// // end
// numbers.push(50, 60);
// // begin
// numbers.unshift(-10, -5);
// // middle
// // splice: position to add, deleted items count, inserting items
// numbers.splice(2, 0, 300);
// console.log(numbers);
// console.log(typeof numbers);

// -----------finding-elements-primitives----------

// const numbers = [1, 2, 3, 1, 4];
// console.log(numbers.indexOf('a')); // returns -1 if not found.

// console.log(numbers.indexOf(4)); // 4

// console.log(numbers.lastIndexOf(1)); // 3

// // to check for an existance of an element in array
// console.log(numbers.indexOf(1) !== -1); // true

// console.log(numbers.includes(1));

// // all these methods have the second parameter which is optional
// // which is starting index

// console.log(numbers.indexOf(1, 2)); // find the 1 element staring at index 2

// -----------finding-elements-objects----------

// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/find

// const courses = [
//   { id: 1, name: 'a' },
//   { id: 2, name: 'b' },
// ];

// // console.log(courses.includes({ id: 1, name: 'a' }));
// // here we will get false because we did see that past
// // these are 2 independent objects (the one in courses vs in includes method)
// // so this will return false

// // so we use find with callbackFn , predicate
// let found = courses.find(function (course) {
//   return course.name === 'a';
// });

// console.log(found);

// let found1 = courses.findIndex(function (course) {
//   return course.name === 'a';
// });

// console.log(found); // if item exists : index otherwise : -1

// -----------Arrow-Functions-----------

// delete the function keyword and use =>

// let found = courses.find((course) => {
//   return course.name === 'a';
// });

// we can delete the () if we got only one parameter
// let found = courses.find(course => {
//   return course.name === 'a';
// });

// we should an empty () if we dont have parameter
// let found = courses.find(() => {
//   return course.name === 'a';
// });

// make it even shorter by deleting the return and write entire code in one line
// we read it like course gose to course.name equals 'a'

// let found = courses.find((course) => course.name === 'a');

// console.log(found);

// -----------Removeing-elements-----------

// const numbers = [1, 2, 3, 4];

// // end -
// const last = numbers.pop();
// console.log(last);
// console.log();

// begin -
// first = numbers.shift();
// console.log(first);

// // middle (splice can be used for both adding and removing elements from middle)
// // start position and count of deleted items
// const middle = numbers.splice(2, 1);
// console.log(middle); // this will return the ans in an array
// console.log(numbers);

// -----------Emptying-an-array-----------

//emptying an array
// let numbers = [1, 2, 3, 4];
// let another = numbers;

// solution1: ✅
// numbers = [];

// Bu örnek, referans tipi olan dizilerin (ve nesnelerin) JavaScript’te nasıl çalıştığını
// gösterir. Bir değişkeni yeniden atamak, diğerinin işaret ettiği veriyi etkilemez.
// Eğer aynı diziyi her iki değişken için de boşaltmak istenseydi, dizinin içeriği doğrudan temizlenmeliydi

// solution2: ✅
// numbers.length = 0;

// solution3:
// numbers.splice(0, numbers.length);

// console.log(numbers);
// console.log(another);

// -----------Combining-and-Slicing-Arrays-----------

// const first = [1, 2, 3];
// const second = [4, 5, 6];

// const combined = first.concat(second);
// const combined1 = [...first, ...second];
// console.log(combined);
// console.log(combined1);

// // copy the entire array
// const clone = combined.slice();
// console.log(clone);

// // copy part of array - slice(start:include, end:exclude)
// const slice = combined.slice(1, 4);
// console.log(slice); // [ 2, 3, 4 ]

// ----------------------

// If an array contains objects, using methods like slice() or concat()
// will not create deep copies of those objects. Instead, only the references
// to the objects are copied. This means that the original and the copied arrays
// will both contain references to the same objects in memory. As a result,
// modifying an object in one array will also reflect in the other,
// since they point to the same underlying object.

// const obj = { value: 42 };
// const array1 = [obj];
// const array2 = array1.slice();

// console.log(array1[0] === array2[0]); // true

// // Modifying the object through array2
// array2[0].value = 100;

// console.log(array1[0].value); // 100

// -----------Spread-Operator-----------

// const first = [1, 2, 3];
// const second = [4, 5, 6];

// // const combined = [...first, ...second];

// // we can also add other elements
// const combined = [...first, 'a', ...second, 'b'];
// console.log(combined);

// const copy = [...combined];
// console.log(combined);

// -----------Iterating-an-Array-----------

// const numbers = [1, 2, 3];

// solution1
// for (let number of numbers) console.log(number);

// solution2
// numbers.forEach(function (number) {
//   console.log(number);
// });

// solution3
// numbers.forEach((number) => console.log(number));

// solution4
// numbers.forEach((number, index,) => console.log(index, number));
