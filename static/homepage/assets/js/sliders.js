/**
 * 01. DORIES DIAMONDS SLIDER (3)
 *
**/

// SLIDER START
const swiper = new Swiper('.swiper', {
    spaceBetween: 24,
    slidesPerGroup: 1,
    loop: true,
    autoplay: {
        delay: 4000,
        disableOnInteraction: false,
    },

    // Navigation arrows
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
    breakpoints: {
        575: {
            slidesPerView: 2
        },

        768: {
            slidesPerView: 2
        },

        991: {
            slidesPerView: 3
        },
    },
});