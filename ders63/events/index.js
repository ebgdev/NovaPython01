// ---✅✅✅------------------- EventListeners --------------------✅✅✅---

// const grandparent = document.querySelector('.grandparent');
// const parent = document.querySelector('.parent');
// const child = document.querySelector('.child');

// -----------------------

// grandparent.addEventListener('click', (e) => {
//   console.log(e);
// });
// // MouseEvent and it's properties

// grandparent.addEventListener('click', (e) => {
//   console.log(e.target);
// });
// // so we get our grandparent element

// -----------------------

// we can set couple of eventlisteners as well
// grandparent.addEventListener('click', (e) => {
//   console.log('Grandparent 1 ');
// });

// -----------------------

// 1-Event Capturing:
// document → html → body → grandparent → parent → child

// 2-Event Bubbling:
// child --> parent --> grandparent --> body --> html --> document

// -----------------------
// 2-Event Bubbling:

// grandparent.addEventListener('click', (e) => {
//   console.log('Grandparent 1 ');
// });

// parent.addEventListener('click', (e) => {
//   console.log('Parent 1 ');
// });

// child.addEventListener('click', (e) => {
//   console.log('Child 1 ');
// });

// document.addEventListener('click', (e) => {
//   console.log('Document 1 ');
// });

// Child 1
// Parent 1
// Grandparent 1
// Document 1

// -----------------------
// 1-Event Capturing:
// Now let's see how we do capturing:

// grandparent.addEventListener(
//   'click',
//   (e) => {
//     console.log('Grandparent 1 ');
//   },
//   { capture: true }
// );

// parent.addEventListener('click', (e) => {
//   console.log('Parent 1 ');
// });

// child.addEventListener('click', (e) => {
//   console.log('Child 1 ');
// });

// document.addEventListener('click', (e) => {
//   console.log('Document 1 ');
// });

// Explanaton:

// When we click the child div, here’s what happens:
// 1. Capturing phase (top-down):
//    document → html → body → grandparent → parent → child
//    - Only grandparent has a capturing listener, so we see "Grandparent 1".

// 2. Target phase:
//    - The event is at the child element.

// 3. Bubbling phase (bottom-up):
//    child → parent → grandparent → document
//    - We see "Child 1", then "Parent 1", then "Document 1".

// -----------------------
// Q1: Why we dont get Grandparent 1 in the bubbling phase ?

// Grandparent 1
// Child 1
// Parent 1
// Document 1

// Beacuse when capture: true is set, the listener is triggered only during the capturing phase
// (while the event travels down the DOM).

// Q2: What if we want to see Grandparent 1 twice?

// grandparent.addEventListener(
//   'click',
//   () => console.log('Grandparent (capture)'),
//   { capture: true }
// );
// grandparent.addEventListener('click', () =>
//   console.log('Grandparent (bubble)')
// );

// parent.addEventListener('click', (e) => {
//   console.log('Parent 1 ');
// });

// child.addEventListener('click', (e) => {
//   console.log('Child 1 ');
// });

// document.addEventListener('click', (e) => {
//   console.log('Document 1 ');
// });

// ----------------------------------------------
// Now let's apply this to all (with funciton)

// function addBothPhases(el, name) {
//   // Capturing (top-down)
//   el.addEventListener('click', () => console.log(`${name} (capture)`), {
//     capture: true,
//   });

//   // Bubbling (bottom-up)
//   el.addEventListener('click', () => console.log(`${name} (bubble)`));
// }

// addBothPhases(document, 'Document');
// addBothPhases(grandparent, 'Grandparent');
// addBothPhases(parent, 'Parent');
// addBothPhases(child, 'Child');

// ----------------------------------------------
// // we also can use <event_name>.stopPropagation()

// // ---- Document ----
// document.addEventListener(
//   'click',
//   (e) => {
//     console.log('Document (capture)');
//   },
//   { capture: true }
// );

// document.addEventListener('click', (e) => {
//   console.log('Document (bubble)');
// });

// // ---- Grandparent ----
// grandparent.addEventListener(
//   'click',
//   (e) => {
//     console.log('Grandparent (capture)');
//   },
//   { capture: true }
// );

// grandparent.addEventListener('click', (e) => {
//   console.log('Grandparent (bubble)');
// });

// // ---- Parent ----
// parent.addEventListener(
//   'click',
//   (e) => {
//     e.stopPropagation(); // ‼️ bundan sonraki yayilmayi keser , parent (capture)'i goruruz yani.
//     console.log('Parent (capture)');
//   },
//   { capture: true }
// );

// parent.addEventListener('click', (e) => {
//   console.log('Parent (bubble)');
// });

// // ---- Child ----
// child.addEventListener(
//   'click',
//   (e) => {
//     console.log('Child (capture)');
//   },
//   { capture: true }
// );

// child.addEventListener('click', (e) => {
//   console.log('Child (bubble)');
// });

// ----------------------------------------------
// { once: true } make an events only works once

// grandparent.addEventListener(
//   'click',
//   (e) => {
//     console.log('Grandparent 1 ');
//   },
//   { once: true }
// );

// parent.addEventListener('click', (e) => {
//   console.log('Parent 1 ');
// });

// child.addEventListener('click', (e) => {
//   console.log('Child 1 ');
// });

// so if we run the code twice

// 1️⃣ first:
// Grandparent 1
// Parent 1
// Child 1

// 2️⃣ second:
// Parent 1
// Child 1

// ----------------------------------------------

function printHi() {
  console.log('Hi');
}

grandparent.addEventListener('click', (e) => {
  console.log('Grandparent 1 ');
});

parent.addEventListener('click', printHi);

setTimeout(() => {
  parent.removeEventListener('click', printHi);
}, 2000);

// parent.addEventListener('click', (e) => {
//   console.log('Parent 1 ');
// });

child.addEventListener('click', (e) => {
  console.log('Child 1 ');
});

// if we run this code twice
// first we will get
// Child 1 - Hi - Grandparent 1
// if we wait 2 seconds for second time
// Child 1 - Grandparent 1 - ...

// ---✅✅✅------------------- Event Delegation --------------------✅✅✅---

// const divs = document.querySelectorAll('div');

// divs.forEach((div) => {
//   div.addEventListener('click', () => {
//     console.log('hi');
//   });
// });

// const newDiv = document.createElement('div');
// newDiv.style.width = '200px';
// newDiv.style.height = '200px';
// newDiv.style.backgroundColor = 'dodgerblue';
// document.body.append(newDiv);

// Now if we click on newDiv we dont get hi
// this is because while we are selection divs
// newDiv has not been created yet.

// ----------------------------
// What if we want to add event listener to it ?

// const divs = document.querySelectorAll('div');

// divs.forEach((div) => {
//   div.addEventListener('click', () => {
//     console.log('hi');
//   });
// });

// const newDiv = document.createElement('div');
// newDiv.style.width = '200px';
// newDiv.style.height = '200px';
// newDiv.style.backgroundColor = 'dodgerblue';
// document.body.append(newDiv);

// ----------------------------
// // but this is really hard to do everytime
// // so it's better to do delegation.

// const divs = document.querySelectorAll('div');

// // document.addEventListener('click', (e) => {
// //   console.log('Hi');
// // });
// // this will give Hi each time we click on anywhere but
// // this is not what we want

// // so

// document.addEventListener('click', (e) => {
//   if (e.target.matches('div')) console.log('Hi');
// });

// const newDiv = document.createElement('div');
// newDiv.style.width = '200px';
// newDiv.style.height = '200px';
// newDiv.style.backgroundColor = 'dodgerblue';
// document.body.append(newDiv);

// ----------------------------
// we also can turn this to a function.

// const divs = document.querySelectorAll('div');

// addGlobalEventListener('click', 'div', (e) => console.log('Hi'));

// function addGlobalEventListener(type, selector, callback) {
//   document.addEventListener(type, (e) => {
//     if (e.target.matches(selector)) callback(e); // ← call it
//   });
// }

// const newDiv = document.createElement('div');
// newDiv.style.width = '200px';
// newDiv.style.height = '200px';
// newDiv.style.backgroundColor = 'dodgerblue';
// document.body.append(newDiv);
