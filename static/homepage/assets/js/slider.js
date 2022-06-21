let slider = tns({
    container: '.product-slider',
    controlsContainer: '#controls',
    navAsThumbnails: false,
    nav: false,
    items: 3,
    slideBy: 'page',
    autoplay: true,
    speed: 400,
    mouseDrag: true,
    autoplayButtonOutput: false,
    responsive: {
        0: {
            items: 1,
            gutter: 0,
        },
        480: {
            gutter: 20,
            items: 2
        },

        992: {
            items: 3,
            gutter: 30,
        }
    }
});

let reviewSlider = tns({
    container: '.review-slider',
    controlsContainer: '#slidecontrols',
    navAsThumbnails: false,
    nav: false,
    items: 1,
    slideBy: 'page',
    autoplay: true,
    speed: 600,
    mouseDrag: true,
    autoplayButtonOutput: false,
    responsive: {
        0: {
            items: 1,
            gutter: 0,
        }
    }
});