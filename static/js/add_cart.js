

        let all_from 

        $('form[id=form]').each(function() {
      
            $(this).submit(function fun (e) {
                e.preventDefault();
                
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
                        alert(data.am);
                    },
                    'error': function (data) {
                        console.log(data);
                    }

                });
        });
    });