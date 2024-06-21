function validateForm(event) {
  event.preventDefault(); // Prevent form refresh

  // Reset all previous error messages and styles
  resetErrors(["name", "email", "password", "checkbox"]);

  // Get all form values
  var name = document.getElementById("name").value;
  var email = document.getElementById("email").value;
  var password = document.getElementById("password").value;
  var checkbox = document.querySelector('input[name="checkbox"]:checked');

  var isValid = true;

  // Validate Name (must be more than 5 characters)
  if (name.length < 5) {
    showError("name", "Name must be at least 5 characters");
    isValid = false;
  }

  // Validate email
  if (!isValidEmail(email)) {
    showError("email", "Email is invalid");
    isValid = false;
  }

  // Validate password (must be alphanumeric)
  if (!isAlphanumeric(password)) {
    showError("password", "Password must contain letters and numbers");
    isValid = false;
  }

  // Validate checkbox
  if (!checkbox) {
    showError("checkbox", "You must agree to our terms and conditions");
    isValid = false;
  }

  if (!isValid) {
    return; // If form is invalid, prevent submission
  }

  // If form is valid, redirect to homepage
  window.location.href = "../Home/home.html";
}
function isAlphanumeric(password) {
  // Must contain letters and numbers, no symbols
  var hasLetter = false;
  var hasNumber = false;
  var hasSymbol = false;

  for (let i = 0; i < password.length; i++) {
      if (/[a-zA-Z]/.test(password[i])) {
          hasLetter = true;
      } else if (/[0-9]/.test(password[i])) {
          hasNumber = true;
      } else {
          hasSymbol = true;
      }
  }

  return hasLetter && hasNumber && !hasSymbol;
}

function isValidEmail(email) {
  // Basic email validation
  if (email.indexOf('@') === -1 || email.indexOf('.') === -1 || email.indexOf('@') === 0 || email.indexOf('.') === 0 || email === '') {
      return false;
  }
  return true;
}

function validateForm2(event) {
  event.preventDefault(); // Prevent form refresh

  // Reset all previous error messages and styles
  resetErrors(['emailr', 'passwordr']);

  // Get all form values
  var emailr = document.getElementById('emailr').value;
  var passwordr = document.getElementById('passwordr').value;

  var isValid = true;

  // Validate email
  if (!isValidEmail(emailr)) {
      showError('emailr', 'Email is invalid');
      isValid = false;
  }

  // Validate password (must be alphanumeric)
  if (!isAlphanumeric(passwordr)) {
      showError('passwordr', 'Password must contain letters and numbers');
      isValid = false;
  }

  if (!isValid) {
      return; // If form is invalid, prevent submission
  }

  // If form is valid, redirect to homepage
  window.location.href = "../Home/home.html";
}

function isAlphanumeric(passwordr) {
  //harus ada huruf dan angka, no symbols
  var huruf = false;
  var angka = false;
  var symbol = false;

  for (let index = 0; index < passwordr.length; index++) {
    if (passwordr[index] >= "a" && passwordr[index] <= "z") {
      huruf = true;
    } else if (passwordr[index] >= "A" && passwordr[index] <= "Z") {
      huruf = true;
    } else if (passwordr[index] >= "0" && passwordr[index] <= "9") {
      angka = true;
    } else {
      symbol = true;
    }
  }

  if (symbol == true) {
    return false;
  } else if (angka == true && huruf == true) {
    return true;
  } else {
    return false;
  }
}

function isValidEmail(emailr) {
  //harus ada simbol @
  if (emailr.indexOf("@") == -1) {
    return false;
  }
  //simbol @ tidak boleh di depan
  if (emailr.indexOf("@") == "0") {
    return false;
  }
  //harus ada titik
  if (emailr.indexOf(".") == "-1") {
    return false;
  }
  //titik tidak boleh di depan
  if (emailr.indexOf(".") == "0") {
    return false;
  }
  //email tidak boleh kosong
  if (emailr == "") {
    return false;
  }

  return true;
}

function showError(elementId, message) {
  var element = document.getElementById(elementId);
  element.style.border = '2px solid red';

  var errorElement = document.createElement('div');
  errorElement.className = 'error-message';
  errorElement.innerText = message;

  if (!element.nextElementSibling || !element.nextElementSibling.classList.contains('error-message')) {
      element.parentNode.insertBefore(errorElement, element.nextSibling);
  }
}

function resetErrors(elementIds) {
  elementIds.forEach(function(id) {
      var element = document.getElementById(id);
      element.style.border = '';

      var errorElement = element.nextElementSibling;
      if (errorElement && errorElement.classList.contains('error-message')) {
          errorElement.remove();
      }
  });
}
