// 0 - 5

// for (let i = 0; i <= 5; i++)
//     if (i % 2 !== 0)
//         console.log(i);

// --------------------------

// let i = 0;
// while (i <= 5) {
//   if (i % 2 !== 0) console.log(i);
//   i++;
// }

// --------------------------

// let i = 9; // --> Sart saglanmadigina ragmen en az 1 kere calisir
// do {
//   if (i % 2 !== 0) console.log(i);
//   i++;
// } while (i <= 5);

// --------------------------

// let colros = ["red", "green", "blue"];

// for (index in colros) {
//   console.log(index, colros[index]);
// }

// for (item of colros) {
//   console.log(item);
// }

// ------------break--------------

// for (let i = 0; i <= 10; i++) {
//   if (i === 5) break;
//   console.log(i);
// }

// let i = 0;
// while (i <= 10) {
//   if (i === 5) break;
//   console.log(i);
//   i++;
// }

// ------------continue--------------

// for (let i = 0; i <= 10; i++) {
//   if (i === 5) {
//     continue;
//   }
//   console.log(i);
// }

// ---------------------

// let i = 0;
// while (i <= 10) {
//   if (i === 5) {
//     i++;
//     continue;
//   }
//   console.log(i);
//   i++;
// }

// --------------------------

// fonksiyon (a,b)
// hangisinin buyuk oldugunu soyleyecek

// function findMax(a, b) {
//   if (a >= b) return a;
//   return b;
// }

// console.log(findMax(201, 200));

// ---------

// function findMax(a, b) {
//   return a >= b ? a : b;
// }

// console.log(findMax(201, 200));

// --------------------------
// FizzBuzz Oyunu

// sayi sadece 5 --> Buzz
// sayi sadece 3 --> Fizz
// sayi hem 5 , 3 -->  FizzBuzz

// hicbirinine bolunemiyorsada sayinin kendisi donsun.
// sayi , NUMBER type degilse invalid input donucek.

// function fizzBuzz(n) {
//   if (typeof n !== "number" || isNaN(n)) {
//     return "Invalid input , input must be a number";
//   }
//   if (n % 3 === 0 && n % 5 === 0) {
//     return "FizzBuzz";
//   } else if (n % 3 === 0) {
//     return "Fizz";
//   } else if (n % 5 === 0) {
//     return "Buzz";
//   } else return n;
// }

// console.log(fizzBuzz('merhaba'));

// --------------------------

// speedLimit 80
// her 5 km hiz icin 1 puan
// 12 puan ve uzere , ehliyetimiz iptal

// ipucu: Math.floor(1.3) --> 1
//

// function speedCheck(speed) {
//   const speedLimit = 80;
//   const negPerKm = 5;
//   const limitation = 12;

//   if (speed < 80) {
//     console.log("ok");
//   } else {
//     const points = Math.floor((speed - speedLimit) / negPerKm);
//     if (points >= limitation) {
//       console.log(`your direver lisence suspended with ${points} points`);
//     } else {
//       console.log(`you have got :${points} points`);
//     }
//   }
// }

// speedCheck(90); // --> (2 neg puans)
// speedCheck(70); // --> (OK)
// speedCheck(170); // --> (dirver lisence suspended.)

// --------------------------

// const person = {
//   name: "erfan",
//   surname: "bahcivan",
//   age: 28,
//   married: false,
// };

// for (const key in person) {
//   console.log(key, person[key]);
// }

// for (const key of Object.keys(person)) {
//   console.log(key, person[key]);
// }

// for (const [key, value] of Object.entries(person)) {
//   console.log(key, value);
// }

// console.log(person.name);
// console.log(person["name"]);

// --------------------------

function isPrime(num) {
  if (num < 2) return false;
  for (let i = 2; i < Math.sqrt(num); i++) {
    if (num % i === 0) return false;
  }
  return true;
}

console.log(isPrime(12));
console.log(isPrime(13));
