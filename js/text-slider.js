(function ( $ ) {

	$.fn.textSlider = function ( options ) {

		/* Default settings */
		var settings = $.extend(
			{
				timeout: 2000,
				slideTime: 600
			},
			options 
		);

		var nextItem;

		var currentItem = 0;
		var count = 0;

		this.children('.slider-item').each(
			function () 
			{

				$(this).addClass( 'slide-' + ( count ) )
					.css(
						{
							//opacity:	   0, 
							paddingTop:	'0px',
							paddingBottom: '0px'
						}
					);

				$(this).hide();

				count++;

			}
		);

		function firstSlide ()
		{

			$('.slide-' + currentItem ).show().animate({ paddingTop: '50px', paddingBottom: '50px', opacity: 1 }, settings.slideTime);

			setTimeout ( transition, settings.timeout );

		}

		function transition ()
		{

			nextItem = parseInt ( currentItem + 1 );

			if ( nextItem >= count )
				nextItem = 0;

			$('.slide-' + currentItem ).animate({ paddingTop: '100px', paddingBottom: '0px', opacity: 0 }, settings.slideTime, function () {
				$(this).hide();
				$('.slide-' + nextItem ).show().animate({ paddingTop: '50px', paddingBottom: '50px', opacity: 1 }, settings.slideTime);
			});

			currentItem = nextItem;

			setTimeout ( transition, settings.timeout );

		}

		return firstSlide ();

	};

}( jQuery ));