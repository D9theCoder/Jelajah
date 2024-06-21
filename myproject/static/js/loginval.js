function validateForm(event) {
  event.preventDefault(); // Prevent form refresh

  // Reset all previous error messages and styles
  resetErrors(["username", "email", "name", "password1", "password2", "checkbox"]);

  // Get all form values
  var username = document.getElementById("id_username").value;
  var email = document.getElementById("id_email").value;
  var name = document.getElementById("id_name").value;
  var password1 = document.getElementById("id_password1").value;
  var password2 = document.getElementById("id_password2").value;
  var checkbox = document.getElementById("checkbox").checked;

  var isValid = true;

  // Validate Username (must be more than 5 characters)
  if (username.length < 5) {
    showError("id_username", "Username must be at least 5 characters");
    isValid = false;
  }

  // Validate email
  if (!isValidEmail(email)) {
    showError("id_email", "Email is invalid");
    isValid = false;
  }

  // Validate Name (optional, remove if not needed)
  if (name.length < 2) {
    showError("id_name", "Name must be at least 2 characters");
    isValid = false;
  }

  // Validate password (must be alphanumeric)
  if (!isAlphanumeric(password1)) {
    showError("id_password1", "Password must contain letters and numbers");
    isValid = false;
  }

  // Validate password confirmation
  if (password1 !== password2) {
    showError("id_password2", "Passwords do not match");
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

  // If form is valid, you can submit the form here
  // For now, we'll just log a message
  console.log("Form is valid, ready to submit!");
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

document.addEventListener('DOMContentLoaded', function() {
  var messages = document.querySelectorAll('.alert');
  messages.forEach(function(message) {
      setTimeout(function() {
          message.style.display = 'none';
      }, 5000); // Disappear after 5 seconds
  });
});

// function showError(elementId, message) {
//   var element = document.getElementsByName(elementId)[0];  // Get the input element by name

//   // Add red border for error
//   element.style.border = '2px solid red';

//   var errorElement = document.createElement('div');
//   errorElement.className = 'error-message';
//   errorElement.innerText = message;

//   // Insert error message after the input field
//   if (!element.nextElementSibling || !element.nextElementSibling.classList.contains('error-message')) {
//     element.parentNode.insertBefore(errorElement, element.nextSibling);
//   }
// }

// function resetErrors(elementIds) {
//   elementIds.forEach(function(id) {
//     var element = document.getElementsByName(id)[0];  // Get the input element by name

//     // Reset border and remove error message
//     element.style.border = '';

//     var errorElement = element.nextElementSibling;
//     if (errorElement && errorElement.classList.contains('error-message')) {
//       errorElement.remove();
//     }
//   });
// }

