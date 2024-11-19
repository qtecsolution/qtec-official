const slider = tns({
  container: ".clientslide",
  items: 5, // Default items shown
  slideBy: "page", // Scroll by visible slides (not fractions)
  autoplay: true,
  autoplayTimeout: 5000,
  autoplayButtonOutput: false,
  nav: false,
  controls: false,
  mouseDrag: true,
  speed: 700, // Smooth scrolling speed
  easing: "ease-in-out", // Smooth easing
  responsive: {
    0: {
      items: 1,
      gutter: 8,
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


// const slider = tns({
//   container: ".clientslide",
//   slideBy: "1",
//   autoplay: true,
//   nav: false,
//   controls: false,
//   mouseDrag: true,
//   autoplayButtonOutput: false,
//   autoplayTimeout: 5000,
//   responsive: {
//     0: {
//       items: 1,
//     },
//     360: {
//       items: 2,
//       gutter: 8,
//     },
//     768: {
//       items: 3,
//       gutter: 16,
//     },
//     992: {
//       items: 4,
//       gutter: 24,
//     },
//     1200: {
//       items: 5,
//       gutter: 40,
//     },
//   },
// });