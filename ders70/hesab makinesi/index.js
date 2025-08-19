// Elemanları anlamlı, açıklayıcı isimlerle seçelim
const firstInput = document.getElementById('number1');
const secondInput = document.getElementById('number2');
const resultText = document.getElementById('resultText');

// Hesaplama fonksiyonu: hangi işlemi yapacağımızı 'operation' belirler
function calculate(operation) {
  const firstNumber = parseFloat(firstInput.value);
  const secondNumber = parseFloat(secondInput.value);

  // if (Number.isNaN(firstNumber) || Number.isNaN(secondNumber)) {
  //   resultText.textContent = 'Sonuç: Lütfen iki sayı girin';
  //   return;
  // }

  // if (operation === '/' && secondNumber === 0) {
  //   resultText.textContent = "Sonuç: Tanımsız (0'a bölünmez)";
  //   return;
  // }

  // eval kullanmadan, açık bir şekilde işlem yapalım
  let result;
  switch (operation) {
    case '+':
      result = firstNumber + secondNumber;
      break;
    case '-':
      result = firstNumber - secondNumber;
      break;
    case '*':
      result = firstNumber * secondNumber;
      break;
    case '/':
      result = firstNumber / secondNumber;
      break;
    default:
      result = 'Bilinmeyen işlem';
  }

  resultText.textContent = 'Sonuç: ' + result;
}

// Tüm işlem butonlarına tıklama olayı bağlayalım
document.querySelectorAll('button[data-operation]').forEach((button) => {
  button.addEventListener('click', () => {
    const op = button.dataset.operation; // '+', '-', '*', '/'
    calculate(op);
  });
});
