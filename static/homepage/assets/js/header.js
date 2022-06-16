// HEADER SHOW HIDE ON SCROLL

// window.addEventListener('scroll', function() {
//     let lastScrollTop = 0;
//     const header = document.querySelector('.header');
//     let scrollTop = window.pageYOffset || document.scrollTop;

//     if(scrollTop > lastScrollTop) {
//         header.style.top = '-247.98px';
//     } else {
//         header.style.top = '0';
//     }

//     lastScrollTop = scrollTop;

//     console.log(scrollTop);
// });

const showAnim = gsap.from('.header', {
    yPercent: -100,
    paused: true,
    duration: 0.2
}).progress(1);

ScrollTrigger.create({
    start: "top top",
    end: 99999,
    onUpdate: (self) => {
        self.direction === -1 ? showAnim.play() : showAnim.reverse();
    }
});