// Get DOM elements
const firstInput = document.querySelector('#number1');
const secondInput = document.querySelector('#number2');
const resultText = document.querySelector('#resultText');

// // 1. Focus on first input when page loads
// window.onload = () => {
//   firstInput.focus();
// };

// 2. Function to calculate and show result
function showResult() {
  const num1 = parseFloat(firstInput.value) || 0;
  const num2 = parseFloat(secondInput.value) || 0;
  // const sum = num1 + num2;

  resultText.textContent = `Sonuc: Num1:${num1} - Num2:${num2}`;
}

// 3. Add button for click option
const button = document.createElement('button');
button.textContent = 'Calculate';
button.style.marginTop = '1rem';
document.querySelector('.row.input').appendChild(button);

// Handle button click
button.addEventListener('click', showResult);

// Handle Enter key press on inputs
[firstInput, secondInput].forEach((input) => {
  input.addEventListener('keydown', (event) => {
    if (event.key === 'Enter') {
      showResult();
    }
  });
});
