


let mini_amount = document.querySelector('#mini_amount') 
let existing_amount = document.querySelector('#existing_amount')
let input_amount = document.querySelector('#amount')
let maxi_amount = document.querySelector('#maxi_amount') 



mini_amount.addEventListener('click', mini_click);
maxi_amount.addEventListener('click', maxi_click);


function mini_click () {
    let mini_number_amount = Number(input_amount.value);
    
    if (input_amount.value != 1) {
        mini_number_amount -= 1;

        input_amount.value = mini_number_amount;
        existing_amount.innerHTML = input_amount.value;
    }
}


function maxi_click () {
    let maxi_number_amount = Number(input_amount.value);
    maxi_number_amount += 1;

    input_amount.value = maxi_number_amount;
    existing_amount.innerHTML = input_amount.value;
}





$('#one_form').submit(function one_product (e) {
        e.preventDefault();

        // cart_noti
        let element_cart_noti = document.querySelector('#element_cart_noti');
        let cart_noti = document.querySelector('#cart_noti_value');
        let cart_noti_value = Number(cart_noti.value);

        // mobile_cart_noti also tablet
        let mobile_element_cart_noti = document.querySelector('#mobile_element_cart_noti');

        // tablet_cart_noti also mobile
        let mobile_element_cart_noti2 = document.querySelector('#mobile_element_cart_noti2');
        

        let product_id_element = document.querySelector('#one_product_id');
        let product_id = product_id_element.value;


        $.ajax({
            'type': 'POST',
            'url': '/one_product_add_cart',
            'data': {
                'one_product_id': product_id,
                'amount': $('#amount').val(),
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
            },
            'success': function (data) {
                if (data.response == "updated") {
                    alert("Successfully updated");
                }
                else if (data.response == "added") {
                    cart_noti_value = cart_noti_value + 1;
                    cart_noti.value = cart_noti_value
                            
                    element_cart_noti.innerHTML = cart_noti_value;
                    mobile_element_cart_noti.innerHTML = cart_noti_value;
                    mobile_element_cart_noti2.innerHTML = cart_noti_value;

                    alert("Successfully added");
                }
                else if (data.response == "duplicate") {
                    alert("Item already added");
                } 
                else if (data.response == "no_user") {
                    // alert("Please register your account!");
                    window.location.href = `/login`;
                } 
                
            },
            'error': function (data) {
                console.log(data);
            }

        });
});
