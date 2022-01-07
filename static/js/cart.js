var pr_id

$( document ).ready(function() {
    $("#btn_add_cart").on('click', function (){

    $.post('../addtocart/',{'id':pr_id, 'quantity':$("#quantity").val(), 'csrfmiddlewaretoken': '{{ csrf_token }}'})
        .done(function(data){
            if (data["status"]){
                $('#myModal').modal('hide').scrollTop(0)
                var current_number = parseInt($("#cart_number").text())
                $("#cart_number").text(current_number + parseInt(data["quantity"]))
            }
        })
        .fail(function(message){
            $("#message_cart").text(message.responseJSON["message"])
        })

    })

    calculate_money(0, 0)
    
});

function showModal(id) {
     $.ajax({
        type: 'GET',
        url: "/check_login",
        success: function (response) {
            if (response["login"]){
                $("#quantity").val(1)
                $('#myModal').modal('show')
                pr_id = id
            }else {
                 window.location.href="/login"
            }
        }
    })

}

function deleteProduct(pr_id){
    $.post('../removecart/',{'id':pr_id, 'csrfmiddlewaretoken': '{{ csrf_token }}'})
     .done(function(data){
          $(pr_id).parent().parent().remove()
          calculate_money(0, 0)
        })
    .fail(function(message){
    })
}


function addcartfromdetail(pr_id){
    $.post('/addtocart/',{'id':pr_id, 'quantity':$("#quantity-detail").val(), 'csrfmiddlewaretoken': '{{ csrf_token }}'})
        .done(function(data){
            if (data["status"]){
                var current_number = parseInt($("#cart_number").text())
                $("#cart_number").text(current_number + parseInt(data["quantity"]))
            }
        })
        .fail(function(message){
            $("#message_cart").text(message.responseJSON["message"])
        })

    }



function calculate_money(total_money, total){
    $("#cart-list").find("tr").each(function(){
        total_money += parseInt($(this).find('td.total').text()) || 0
    }).promise().done(function(){
     if ($("#cart-list tbody").find("tr").length === 0){
         $("#total-cart-money").text(0);
         $("#total_money").text(0);
     } else{
        total = total_money + (parseInt($("#ship").text()) || 0);
        $("#total-cart-money").text(total_money);
        $("#total_money").text(total)
     }
     });
}
