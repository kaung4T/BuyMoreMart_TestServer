



let cart_delivery = document.querySelector('#cart_delivery');

let grand_price = document.querySelector('#grand_price');


$("#cart_delivery").change(function(){
    let selected_fee = $(this).val();
    let total_val = $('.total_value').val();

    let grand_total = parseInt(total_val) + parseInt(selected_fee);

    grand_price.innerHTML = `Ks${grand_total}`;

});
