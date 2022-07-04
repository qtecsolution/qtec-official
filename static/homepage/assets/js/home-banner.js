// gsap.registerPlugin(ScrollTrigger);

// // const tl = gsap.timeline({
// //   scrollTrigger: {
// //     trigger: ".homebanner",
// //     start: "top top",
// //     end: "bottom top",
// //     scrub: true
// //   }
// // });

// // gsap.utils.toArray(".parallax").forEach(layer => {
// //   const depth = layer.dataset.depth;
// //   const movement = -(layer.offsetHeight * depth)
// //   tl.to(layer, { y: movement, ease: "none" }, 0)
// // });

// function animateFrom(elem, direction) {
//   direction = direction || 1;
//   var x = 0,
//     y = direction * 100;
//   if (elem.classList.contains("homebanner-details")) {
//     x = -100;
//     y = 0;
//   } else if (elem.classList.contains("homebanner-descriptions")) {
//     x = 100;
//     y = 0;
//   }
//   elem.style.transform = "translate(" + x + "px, " + y + "px)";
//   elem.style.opacity = "0";
//   gsap.fromTo(elem, { x: x, y: y, autoAlpha: 0 }, {
//     duration: 1.25,
//     x: 0,
//     y: 0,
//     autoAlpha: 1,
//     ease: "expo",
//     overwrite: "auto"
//   });
// }

// function hide(elem) {
//   gsap.set(elem, { autoAlpha: 0 });
// }

// document.addEventListener("DOMContentLoaded", function () {
//   gsap.registerPlugin(ScrollTrigger);

//   gsap.utils.toArray(".homebanner").forEach(function (elem) {
//     hide(elem); // assure that the element is hidden when scrolled into view

//     ScrollTrigger.create({
//       trigger: elem,
//       onEnter: function () { animateFrom(elem) },
//       onEnterBack: function () { animateFrom(elem, -1) },
//       onLeave: function () { hide(elem) } // assure that the element is hidden when scrolled into view
//     });
//   });
// });
