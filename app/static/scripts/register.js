// Contains code that controls the look and feel of the login and
// Signup pages

const firstNameField = document.getElementById('fNamefield'),
lastNameField = document.getElementById('lNamefield'),
businessNameField = document.getElementById('bNamefield'),
orTextSignup = document.getElementById('or-text-signup'),
googleSignup = document.getElementById('google-signup'),
businessRegister= document.getElementById('business-register');

// Handles click on signup page
if (businessRegister) {
  businessRegister.addEventListener('click', () => {
    if (businessRegister.checked) {
      firstNameField.parentNode.classList.add('disappear');
      lastNameField.parentNode.classList.add('disappear');
      orTextSignup.classList.add('disappear');
      googleSignup.classList.add('disappear');
      businessNameField.parentNode.classList.remove('disappear');
    } else {
      firstNameField.parentNode.classList.remove('disappear');
      lastNameField.parentNode.classList.remove('disappear');
      orTextSignup.classList.remove('disappear');
      googleSignup.classList.remove('disappear');
      businessNameField.parentNode.classList.add('disappear');
    }
  });
}

