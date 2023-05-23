


        $('form[id=form]').each(function() {
      
            $(this).submit(function fun (e) {
                e.preventDefault();

                // cart_noti
                let element_cart_noti = document.querySelector('#element_cart_noti');
                let cart_noti = document.querySelector('#cart_noti_value');
                let cart_noti_value = Number(cart_noti.value);

                // mobile_cart_noti also tablet
                let mobile_element_cart_noti = document.querySelector('#mobile_element_cart_noti');

                // tablet_cart_noti also mobile
                let mobile_element_cart_noti2 = document.querySelector('#mobile_element_cart_noti2');

                
                let product_id_element = this.querySelector('#product_id');
                let product_id = product_id_element.value;

                $.ajax({
                    'type': 'POST',
                    'url': '/add_cart',
                    'data': {
                        'product_id': product_id,
                        'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
                    },
                    'success': function (data) {
                        if (data.response == "added") {
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
    });
    