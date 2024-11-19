
// Swiper slider for team members


var ourTeamMembers = new Swiper(".ourTeamMembers", { 
    direction: "horizontal",
    loop: true,
    speed: 3500,
    autoplay: {
      delay: 0,
      disableOnInteraction: false,
    },
    slidesPerView: "auto",
    spaceBetween: 10,
    breakpoints: {
      550: {
        slidesPerView: 2,
        spaceBetween: 20,
      },
      768: {
        slidesPerView: 3,
        spaceBetween: 20,
      },
      992: {
        slidesPerView: 4,
        spaceBetween: 20,
      },
      1024: {
        slidesPerView: 5,
        spaceBetween: 20,
      },
    },
  });
  

  // var swiper = new Swiper(".ourTeamMembers", {
  //   slidesPerView: 1,
  //       spaceBetween: 10,
  //       pagination: {
  //         el: ".swiper-pagination",
  //         clickable: true,
  //       },
  //       breakpoints: {
  //         640: {
  //           slidesPerView: 2,
  //           spaceBetween: 10,
  //         },
  //         768: {
  //           slidesPerView: 4,
  //           spaceBetween: 10,
  //         },
  //       },
  //     });


  var swiper = new Swiper(".mySwiper", {
    direction: "horizontal",
    autoplay: {
      delay: 0,
      disableOnInteraction: false,
    },
    loop: true,
    slidesPerView: 1,
    spaceBetween: 10,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    breakpoints: {
      640: {
        slidesPerView: 2,
        spaceBetween: 10,
      },
      768: {
        slidesPerView: 4,
        spaceBetween: 10,
      },
    },
  });