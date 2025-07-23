// ---------------Challenge3-------------
// exclude elements from array

// const numbers = [1, 2, 3, 4];
// const output = except(numbers, [1, 2]);

// console.log(output);

// function except(array, excluded) {
//   const output = [];
//   for (let element of array)
//     if (!excluded.includes(element)) output.push(element);
//   return output;
// }

// ---------

// function except(array, excluded) {
//   return array.filter((element) => !excluded.includes(element));
// }

// ---------

// function except(array, exclude) {
//   const output = [];
//   for (let item of array) {
//     if (!exclude.includes(item)) {
//       output.push(item);
//     }
//   }
//   return output;
// }

// console.log(numbers);

// ---------------Challenge4-------------

// const numbers = [1, 2, 3, 4];
// const output = move(numbers, 1, 1);

// console.log(output);

// function move(array, index, offset) {
//   const position = index + offset;

//   if (position < 0 || position >= array.length) {
//     console.error('Invalid offset.');
//     return array;
//   }

//   const output = [...array]; // make a copy
//   const poppedItem = output.splice(index, 1)[0]; // remove item at index
//   // console.log(output.splice(index, 1));
//   output.splice(position, 0, poppedItem); // insert at new position
//   return output;
// }

// ---------------Challenge5-reduce------------

// const numbers = [1, 2, 3, 4, 1];

// ✅ first way

// function countOccurrences(array, target) {
//   let count = 0;
//   array.forEach((element) => {
//     if (element === target) count++;
//   });
//   return count;
// }

// console.log(countOccurrences(numbers, 1));

// ✅ second way - reduce and ternary operation

// function countOccurrences(array, target) {
//   return array.reduce(
//     (count, element) => (element === target ? count + 1 : count),
//     0
//     // ↑ this 0 here is count initial value
//   );
// }

// console.log(countOccurrences(numbers, -1)); // Output: 0

// ---------------Challenge6-reduce------------
// getMax function

// [1,2,3,4] --> 4
// []        --> undefined

// ✅ first way
// const numbers = [1, 2, 3, 4, 1];
// const max = getMax(numbers);
// console.log(max); // Output: 4

// function getMax(array) {
//   if (array.length === 0) return undefined;

//   return array.reduce((acc, current) => {
//     if (current >= acc) {
//       return current;
//     } else {
//       return acc;
//     }
//   });
// }

// ✅ second way
// const numbers = [1, 2, 3, 4, 1];
// const max = getMax(numbers);

// function getMax(array) {
//   if (array.length === 0) return undefined;

//   return array.reduce((acc, current) => {
//     return current > acc ? current : acc;
//   });
// }

// console.log(max); // 4
