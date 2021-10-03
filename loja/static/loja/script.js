$( "#form-produtos" ).submit(function( event ) {
    console.log( $( this ).serialize() );
    event.preventDefault();
  });