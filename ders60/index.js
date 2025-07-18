// -----------Joining-Arrays-----------

// const numbers = [1, 2, 3];

// const joined = numbers.join(',');
// console.log(joined);
// console.log(typeof joined);

// const message = 'This is my first message';
// const splitted = message.split(' ');
// console.log(splitted);

// We can also rejoin the array, but in a different way
// const combined = splitted.join('-');
// console.log(combined);

// Where is this useful?
// Converting a question title into a URL slug
// Example:
// Title: "How to delete container in MapR cluster"
// Slug: "how-to-delete-container-in-mapr-cluster"
// URL: https://stackoverflow.com/questions/79696793/how-to-delete-container-in-mapr-cluster

// -----------Joining-Arrays-----------

// const numbers = [3, 1, 2];
// // numbers.sort();

// const sorted = [...numbers].sort();
// const reversed = [...numbers].reverse();
// console.log(numbers);
// console.log(sorted);
// console.log(reversed);

// ---------------

// const courses = [
//   { id: 1, name: 'Node.js' },
//   { id: 3, name: 'Python' },
//   { id: 2, name: 'JavaScript' },
// ];

// courses.sort();
// console.log(courses);

// So as i showed above we can not use
// sort like that on the objects

// this will run in nlogn time
// courses.sort((a, b) => {
//   if (a.name < b.name) return -1;
//   if (a.name > b.name) return 1;
//   return 0;
// });

// -----------

// console.log(courses);

// courses.sort((a, b) => {
//   const nameA = a.name.toLocaleLowerCase();
//   const nameB = b.name.toLocaleLowerCase();
//   if (nameA < nameB) return -1;
//   if (nameA > nameB) return 1;
//   return 0;
// });

// console.log(courses);

// -----------Testing-the-Elements-of-an-Arrays-----------

// const numbers = [-11, -2, 3];

// every - without arrow function - will return bool

// const allPositive = numbers.every(function (value) {
//   return value >= 0;
// });

// console.log(allPositive);

// every - with arrow function
// const allPositive = numbers.every((value) => value >= 0);
// console.log(allPositive);

// some - without arrow function
// const atLeastOnePositive = numbers.some(function (value) {
//   return value >= 0;
// });

// console.log(atLeastOnePositive);

// some - with arrow function
// const atLeastOnePositive = numbers.some((value) => value >= 0);
// console.log(atLeastOnePositive);

// -----------Filtering-an-Arrays-----------

// const numbers = [1, -1, 2, 3];

// filter - without arrow function
// const filterPositive = numbers.filter(function (value) {
//   return value >= 0;
// });

// console.log(filterPositive);

// filter - with arrow function
// const filterPositive = numbers.filter((value) => value >= 0);
// console.log(filterPositive);

//---------- filter ----------

// const numbers = [1, -1, 2, 3];

// const filteredNums = numbers.filter((num) => num >= 0);

// console.log(filteredNums);

//---------- map ----------

// we can use web console here as well

// const numbers = [1, -1, 2, 3];

// const filteredNums = numbers.filter((num) => num >= 0);

// ----------------
// map to string

// const items = filteredNums.map((num) => '<li>' + num + '</li>');

// const html1 = items.join();

// const html2 = items.join(''); // so we perfer this to ignore the ' , '

// const html3 = '<ul>' + items.join('') + '</ul>';

// console.log(items);
// console.log(html1);
// console.log(html2);
// console.log(html3);

// ----------------
// map to an object

// first way:
// const items = filteredNums.map((n) => {
//   const obj = { value: n };
//   return obj;
// });

// console.log(items);

// ------

// second way:
// const items = filteredNums.map((n) => {
//   return { value: n };
// });

// console.log(items);

// ------

// ❌ third way: JavaScript thinks the {} is a code block, not an object. So nothing gets returned.

// const items = filteredNums.map((n) => {
//   value: n;
// });

// console.log(items);
// output: [ undefined, undefined, undefined ]
// ------

// ✅ third way:
// Wrapping the object in () tells JavaScript: "This is an object, not a code block."
// const items = filteredNums.map((n) => ({ value: n }));
// console.log(items);
// output: [ { value: 1 }, { value: 2 }, { value: 3 } ]

// ------
// these methods are chainable
// const numbers = [1, -1, 2, 3];

// const items = numbers.filter((num) => num >= 0).map((n) => ({ value: n }));
// console.log(items);

// example
// const numbers = [1, -1, 2, 3];

// const items = numbers
//   .filter((n) => n >= 0)
//   .map((n) => ({ value: n }))
//   .filter((obj) => obj.value > 1)
//   .map((obj) => obj.value);

// console.log(items); // Output: [2, 3]

//---------- reduce ----------

// const numbers = [1, -1, 2, 3];

// let sum = 0;

// numbers.forEach((element) => {
//   sum += element;
// });

// console.log(sum);

// // version 1
// const total = numbers.reduce((accumulator, currentValue) => {
//   return accumulator + currentValue;
// });

// // ❗ Will throw an error if the array is empty.
// console.log(total);

// -------------

// version 2
// const total = numbers.reduce((accumulator, currentValue) => {
//   return accumulator + currentValue;
// }, 0);

// // ❗ output will be 0 if the array is empty.
// console.log(total);

// ---------------Challenge1-------------
// range element in js
// expected output: [1,2,3,4]
// const numbers = arrayFromRange(1, 4);

// console.log(numbers);

// function arrayFromRange(min, max) {
//   let arr = [];
//   for (let i = min; i <= max; i++) {
//     arr.push(i);
//   }
//   return arr;
// }
