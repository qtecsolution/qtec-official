const loginModal = document.querySelector('#loginModal');
const registerModal = document.querySelector('#registerModal');
const forgotModal = document.querySelector('#forgotModal');
const changeModal = document.querySelector('#changeModal');

// INITIALIZING MODAL TO BOOTSTARP
const login = new bootstrap.Modal(loginModal);
const register = new bootstrap.Modal(registerModal);
const forgot = new bootstrap.Modal(forgotModal);
const change = new bootstrap.Modal(changeModal);

const signupButtons = Array.from(document.querySelectorAll('.btn-signup'));
const signInButtons = Array.from(document.querySelectorAll('.btn-signin'));
const forgotButton = document.querySelector('.btn-forgot');
const backToLogin = document.querySelector('.btn-back');
const btnOTP = document.querySelector('.btn-otp');


forgotButton.addEventListener('click', showForgotPassword);
backToLogin.addEventListener('click', backToLog);
btnOTP.addEventListener('click', showChangePassword);


// SHOW SIGNUP
function showForgotPassword() {
    register.hide();
    login.hide();
    login.show();
    forgot.show();
}

// BACK TO LOGIN FROM FORGOT PASSWORD
function backToLog() {
    forgot.hide();
    register.hide();
    change.hide();
    login.show();
}

signupButtons.forEach(button => {
    button.addEventListener('click', showSignup);
});

// SHOW SIGNUP
function showSignup() {
    forgot.hide();
    change.hide();
    login.hide();
    register.show();
}

signInButtons.forEach(button => {
    button.addEventListener('click', showSignin);
});

// SHOW SIGNUP
function showSignin() {
    forgot.hide();
    change.hide();
    register.hide();
    login.show();
}

// SHOW SIGNUP
function showChangePassword() {
    forgot.hide();
    change.hide();
    register.hide();
    login.hide();
    change.show();
}