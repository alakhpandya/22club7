$('.owl-carousel').owlCarousel({
    loop:true,
    margin:10,
    nav:true,
    dots:false,
    // autoplay: true,
    autoplayTimeout: 3000,
    autoplayHoverPause: true,
    navContainer: `${'.owl-nav'}`,
    navText: ['<i class="fa-solid fa-arrow-left-long"></i>','<i class="fa-solid fa-arrow-right-long"></i>'],
    responsive:{
        0:{
            items:1 
        },
        750:{
            items:2
        },
        1000:{
            items:3
        }
    }
})

AOS.init();