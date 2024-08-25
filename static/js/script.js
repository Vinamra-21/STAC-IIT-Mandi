$(function () {

    $('.navbar-toggler').on('click', function() {
        $('.animated-icon').toggleClass('open');
    });

    // Back to top button
    $('.back-to-top').on('click', function() {
        $('html, body').animate({
            scrollTop: 0
        }, 1000, 'easeInOutExpo');
        return false;
    });

    // Navbar menu reduce on scroll
    $(window).on("scroll", function() {
        const pixels = $(".banner-img").innerHeight();
        if ($(window).scrollTop() > pixels) {
            $(".navbar").addClass("bg-light shadow-md");
            $(".navbar").removeClass("bg-transparent");
            $('.dropdown-menu').removeClass('hidden');
        } else {
            $(".navbar").removeClass("bg-light shadow-md");
            $(".navbar").addClass("bg-transparent");
            $('.dropdown-menu').addClass('hidden');
        }
    });

    // Venobox initialization
    $(document).ready(function(){
        $('.venobox').venobox();
        $('.venobox_custom').venobox({
            framewidth : '300px',
            frameheight: '200px',
            border     : '10px',
            bgcolor    : '#5dff5e',
            titleattr  : 'data-title',
            numeratio  : true,
            infinigall : true,
        });
    });

    // Hide icon if href is empty
    $("div.social a").each(function() {
        if ($(this).attr("href") == "") {
            $(this).hide();
        }
    });

    // Slider carousel
    $(".slider-carousel").owlCarousel({
        autoplay: true,
        dots: true,
        loop: true,
        items: 1
    });
});
