const divs = document.querySelectorAll('div');

addGlobalEventListener('click', 'div', (e) => console.log('Hi'));

function addGlobalEventListener(type, selector, callback) {
  document.addEventListener(type, (e) => {
    if (e.target.matches(selector)) callback(e); // ← call it
  });
}

const newDiv = document.createElement('div');
newDiv.style.width = '200px';
newDiv.style.height = '200px';
newDiv.style.backgroundColor = 'dodgerblue';
document.body.append(newDiv);
