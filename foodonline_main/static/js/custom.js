$(document).ready(function() {
  // Add to cart
  $('.add_to_cart').on('click', function(e) {
    e.preventDefault();

    let food_id = $(this).attr('data-id');
    let url = $(this).attr('data-url');

    $.ajax({
      type: 'GET',
      url: url,
      success: function(response) {
        console.log(response);
        if (response.status == 'login_required') {
          swal(response.message, '', 'info').then(function() {
            window.location = '/login';
          });
        } else if (response.status == 'Failed') {
          swal(response.message, '', 'error');
        } else {
          $('#cart_counter').html(response.cart_counter['cart_count']);
          $('#qty-' + food_id).html(response.qty);
          // Subtotal, tax, and grand total
          applyCartAmounts(
            response.cart_amount['subtotal'],
            response.cart_amount['tax_dict'],
            response.cart_amount['grand_total']
          );
        }
      }
    });
  });
});

// decrease cart
$('.decrease_cart').on('click', function(e){
  e.preventDefault();
  
  food_id = $(this).attr('data-id');
  url = $(this).attr('data-url');
  cart_id = $(this).attr('id');
  
  
  $.ajax({
      type: 'GET',
      url: url,
      success: function(response){
          console.log(response)
          if(response.status == 'login_required'){
              swal(response.message, '', 'info').then(function(){
                  window.location = '/login';
              })
          }else if(response.status == 'Failed'){
              swal(response.message, '', 'error')
          }else{
              $('#cart_counter').html(response.cart_counter['cart_count']);
              $('#qty-'+food_id).html(response.qty);

              applyCartAmounts(
                  response.cart_amount['subtotal'],
                  response.cart_amount['tax_dict'],
                  response.cart_amount['grand_total']
              )

              if(window.location.pathname == '/cart/'){
                  removeCartItem(response.qty, cart_id);
                  checkEmptyCart();
              }
              
          } 
      }
  })
})
