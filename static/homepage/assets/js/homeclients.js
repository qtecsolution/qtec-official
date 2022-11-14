const slider = tns({
  container: ".clientslide",
  slideBy: "1",
  autoplay: true,
  nav: false,
  controls: false,
  mouseDrag: true,
  autoplayButtonOutput: false,
  autoplayTimeout: 5000,
  responsive: {
    0: {
      items: 1,
    },
    360: {
      items: 2,
      gutter: 8,
    },
    768: {
      items: 3,
      gutter: 16,
    },
    992: {
      items: 4,
      gutter: 24,
    },
    1200: {
      items: 5,
      gutter: 40,
    },
  },
});