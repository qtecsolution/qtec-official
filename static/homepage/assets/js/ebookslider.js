const bookslider = new Swiper(".bookslider", {
  autoplay: {
    delay: 5000,
    disableOnInteraction: false,
  },
  slidesPerView: "auto",
  centeredSlides: false,
  pagination: false,
  spaceBetween: 16,
  grabCursor: true,
  loop: true,
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  breakpoints: {
    // when window width is >= 320px
    0: {
      slidesPerView: 1
    },
    // when window width is >= 576px
    576: {
      slidesPerView: 2,
    },
    // when window width is >= 768px
    768: {
      slidesPerView: 3
    },
    // when window width is >= 768px
    992: {
      slidesPerView: 4
    }
  }
});

const reviewslider = new Swiper(".reviewslider", {
  autoplay: {
    delay: 5000,
    disableOnInteraction: false,
  },
  // slidesPerView: "auto",
  centeredSlides: false,
  pagination: false,
  spaceBetween: 16,
  grabCursor: true,
  loop: true,
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  breakpoints: {
    // when window width is >= 320px
    0: {
      slidesPerView: 1
    },
    // when window width is >= 576px
    576: {
      slidesPerView: 2,
    },
    // when window width is >= 768px
    768: {
      slidesPerView: 3
    },
    // when window width is >= 768px
    992: {
      slidesPerView: 4
    }
  }
});