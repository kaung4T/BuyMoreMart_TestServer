


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
                if (data.response == "added") {
                    alert("Successfully added");
                }
                else if (data.response == "duplicate") {
                    alert("Item already added");
                } 
                else if (data.response == "no_user") {
                    alert("Please register your account!");
                } 
                
            },
            'error': function (data) {
                console.log(data);
            }

        });
});
