// Challenge2:

// Create a circle object using the object literal syntax
// this object should have a radius property that we can read or write to
// we should also have an area property that is read only
// so we should not be able to set the area from the outside but should be able to read it.
// so we should allow console.log(circle.area); to run.

const circle = {
  radius: 1,
  get area() {
    return Math.PI * this.radius * this.radius;
  },
};

console.log(circle.area);

// try these in console

// circle.radius = 2
// circle.area -> 12.5...
// circle.area = 20 --> this will return the 20
// but i type
// circle.area i still will get 12.5 ...

// -----------------------------------------------------

// Challenge3:

const numbers = [1, 2, 3, 4, 1];

function countOccurrences(array, target) {
  return array.reduce(
    (count, element) => (element === target ? count + 1 : count),
    0
  );
}

console.log(countOccurrences(numbers, -1)); // Output: 0

// ans:

try {
  const numbers = [1, 2, 3, 4];

  // This will throw because array is null
  const count1 = countOccurrences(null, 1);
  console.log(count1);
} catch (e) {
  console.log(e.message); // -> "Invalid array."
}

function countOccurrences(array, searchElement) {
  if (!Array.isArray(array)) throw new Error('Invalid array.');

  return array.reduce((accumulator, current) => {
    const occurrence = current === searchElement ? 1 : 0;
    return accumulator + occurrence;
  }, 0);
}

// Valid example:
const numbers = [1, 2, 1, 4];
console.log(countOccurrences(numbers, 1)); // 2

// -----------------------------------------------------
