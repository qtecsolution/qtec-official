// RECOMMENDED-COURSES SLIDER
const recomendedCourses = new Swiper(".recomended-courses", {
    loop: true,
    autoplay: {
        delay: 5000,
    },
    spaceBetween: 24,
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
    breakpoints: {
        '0': {
            slidesPerView: 1
        },
        '360': {
            slidesPerView: "auto",
            spaceBetween: 24
        },
        '499': {
            slidesPerView: 2
        },
        '500': {
            slidesPerView: 2
        },
        '768': {
            slidesPerView: 3
        },
        '1200': {
            slidesPerView: 4
        }
    }
});

// TOP-COURSES SLIDER
const topCourses = new Swiper(".top-courses", {
    loop: true,
    autoplay: {
        delay: 5000,
    },
    spaceBetween: 24,
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
    breakpoints: {
        '0': {
            slidesPerView: 1
        },
        '360': {
            slidesPerView: "auto",
            spaceBetween: 24
        },
        '499': {
            slidesPerView: 2
        },
        '500': {
            slidesPerView: 2
        },
        '768': {
            slidesPerView: 3
        },
        '1200': {
            slidesPerView: 4
        }
    }
});

// STUDENTS-TESTIMONIAL SLIDER
const studentsTestimonial = new Swiper(".students-testimonial", {
    loop: true,
    autoplay: {
        delay: 5000,
    },
        slidesPerView: 1,
    spaceBetween: 24,
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    breakpoints: {
        '768': {
            slidesPerView: 2,
            spaceBetween: 24
        },
        '1200': {
            slidesPerView: 3
        }
    }
});