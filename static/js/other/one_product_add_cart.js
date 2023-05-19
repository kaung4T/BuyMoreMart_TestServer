






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
