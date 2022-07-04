const preloader = document.querySelector('#preloader');

window.addEventListener('load', showHidePreloader);

function showHidePreloader() {
    preloader.classList.add('d-none');
}