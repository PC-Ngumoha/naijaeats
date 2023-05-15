// Contains code that controls the look and feel of the login and
// Signup pages

const googleSignin = document.getElementById('google-signin'),
orTextSignin = document.getElementById('or-text-signin'),
businessLogin= document.getElementById('business-login');

// Handles click on signup page
if (businessLogin) {
  businessLogin.addEventListener('click', () => {
    if (businessLogin.checked) {
      orTextSignin.classList.add('disappear');
      googleSignin.classList.add('disappear');
    } else {
      orTextSignin.classList.remove('disappear');
      googleSignin.classList.remove('disappear');
    }
  });
}

