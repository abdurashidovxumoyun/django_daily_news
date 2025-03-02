$(function(){
	'use-strict';

	// side nav left
	$(".side-nav-left").sideNav({

		edge: 'left',
		closeOnClick: false

	});

	// slider
	$(".slider").slider({full_width: true});

	// loader
    $("#fakeLoader").fakeLoader({
      
      zIndex: 999,
      spinner: 'spinner4',
      bgColor: '#ffffff'

    });

    $('.collapsible').collapsible({
		accordion: false
	});

   	// image-popup
    $(".image-popup").magnificPopup({
        type: "image",
        removalDelay: 300,
        mainClass: "mfp-fade"
    });


});