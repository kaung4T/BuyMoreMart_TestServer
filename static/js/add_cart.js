

        let all_from 

        $('a[id=add_cart]').each(function() {
      
            $(this).click(function fun (e) {
                e.preventDefault();
                
                let product_id_element = this.querySelector('#product_id');
                let product_id = product_id_element.value;

                alert(product_id);
                
                $.ajax({
                    'type': 'POST',
                    'url': '/add_cart',
                    'data': {
                        'product_id': $('#product_id').val(),
                        'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
                    },
                    'success': function fun (data) {
                        alert(data);
                    },
                    'error': function error (data) {
                        console.log(data);
                    }

                });
        });
    });