
$( document ).ready(function() {

    initial()
    $("#table_1").on('click','#arrow-button' ,function(){
       var tr = $(this).closest('tr').remove().clone()
        var order_id = $(this).closest('tr').find('#ord_id').text()
        $.ajax({
            type: 'GET',
            url: "/change_state",
            data: {"order_id": order_id},
            success: function (response) {

               if (response["status"]){

                   $(tr).find('div').hide()
                   $("#table_2 tbody").append(tr)
               }
            }
        })

    });

    $("#table_2").on('click','#arrow-button', function(){
       var tr = $(this).closest('tr').remove().clone()
        var order_id = $(this).closest('tr').find('#ord_id').text()
        $.ajax({
            type: 'GET',
            url: "/change_state",
            data: {"order_id": order_id},
            success: function (response) {

               if (response["status"]){

                   $(tr).find('div').hide()
                   $("#table_3 tbody").append(tr)
               }
            }
        })

    });

    $("#table_3").on('click','#arrow-button', function(){
        var tr = $(this).closest('tr').remove().clone()
        $(tr).find('#button-action').hide()
         var order_id = $(this).closest('tr').find('#ord_id').text()
        $.ajax({
            type: 'GET',
            url: "/change_state",
            data: {"order_id": order_id},
            success: function (response) {
               if (response["status"]){
                   $("#table_4 tbody").append(tr)
               }
            }
        })

    });

    $("#table_1").on('click','#remove-button', function(){
        var tr = $(this).closest('tr').remove().clone()
        $(tr).find('p button').remove()
         var order_id = $(this).closest('tr').find('#ord_id').text()
        $.ajax({
            type: 'GET',
            url: "/change_state_remove",
            data: {"order_id": order_id},
            success: function (response) {
               if (response["status"]){
                     $("#table_5 tbody").append(tr)
               }
            }
        })
    });
    $("#table_2").on('click','#remove-button', function(){
        var tr = $(this).closest('tr').remove().clone()
        $(tr).find('p button').remove()
         var order_id = $(this).closest('tr').find('#ord_id').text()
        $.ajax({
            type: 'GET',
            url: "/change_state_remove",
            data: {"order_id": order_id},
            success: function (response) {
               if (response["status"]){
                     $("#table_5 tbody").append(tr)
               }
            }
        })
    });
    $("#table_3").on('click','#remove-button', function(){
        var tr = $(this).closest('tr').remove().clone()
        $(tr).find('p button').remove()
         var order_id = $(this).closest('tr').find('#ord_id').text()
        $.ajax({
            type: 'GET',
            url: "/change_state_remove",
            data: {"order_id": order_id},
            success: function (response) {
               if (response["status"]){
                     $("#table_5 tbody").append(tr)
               }
            }
        })
    });


    $("#table_1 tbody").on('mouseover','tr td.td-action', function(){
                $(this).children().show()


    }).on('mouseout', 'tr td.td-action', function(){
                $(this).children().hide()

    })


       $("#table_2 tbody").on('mouseover','tr td.td-action', function(){
        $(this).children().show()

    }).on('mouseout', 'tr td.td-action', function(){
        $(this).children().hide()
    })

      $("#table_3 tbody").on('mouseover','tr td.td-action', function(){
                $(this).children().show()


    }).on('mouseout', 'tr td.td-action', function(){
                $(this).children().hide()

    })

    //detail đơn hàng
     $("#table_1 tbody").on('click','tr td.td-order', function(){
         var order_id = $(this).find('#ord_id').text()
         get_detail_order(order_id)
     })

    $("#table_2 tbody").on('click','tr td.td-order', function(){
         var order_id = $(this).find('#ord_id').text()
         get_detail_order(order_id)
     })

     $("#table_3 tbody").on('click','tr td.td-order', function(){
         var order_id = $(this).find('#ord_id').text()
         get_detail_order(order_id)
     })

     $("#table_4 tbody").on('click','tr td.td-order', function(){
         var order_id = $(this).find('#ord_id').text()
         get_detail_order(order_id)
     })

     $("#table_5 tbody").on('click','tr td.td-order', function(){
         var order_id = $(this).find('#ord_id').text()
         get_detail_order(order_id)
     })

     $('#export').on('click', function(){
        var ord_id = $("#od_id").text().split("#")[1]
        window.location.href=`/export/${ord_id}`
        $("#detail_order").modal('hide')
     })
})

function initial(){
    $.ajax({
        type: 'GET',
        url: "/get-order",
        success: function (response) {
            if (response["result"]){
                let id = 0
                for (let order of response["result"]){
                    var tr = `<tr class="tr-table" id="tr-order-${id}">
                                <td  class="td-order" id="td-order">
                                    <p style="text-align:center; font-size: 15px; margin-top:15px; color:#82b51f; 
                                    font-weight: bold;" id="ord_id">${order['ord_id']}</p>
                                    <p style="text-align:center; font-size: 15px; color: #82b51f; font-weight: bold;">${order['time']}</p>
                                </td>
                                <td  class="td-action" id="td-action-${id}">
                                    <div id="button-action">
                                    <p style="text-align:revert"><button class="arrow-button" id="arrow-button">
                                        <i class="fas fa-arrow-alt-circle-right"></i>
                                    </button></p>
                                    <p style="text-align:revert"><button class="remove-button"id="remove-button">
                                        <i class="fa fa-times"></i>
                                    </button></p>
                                    </div>
                                </td>
                            </tr>`
                    if (order["status"] === 0){

                        $("#table_1").append(tr)
                        id = id + 1
                    } else if (order["status"] === 1){
                        $("#table_2").append(tr)
                        id = id + 1
                    }
                     else if (order["status"] === 2){
                        $("#table_3").append(tr)
                        id = id + 1
                    }
                     else if (order["status"] === 3){
                        $("#table_4").append(tr)
                        id = id + 1
                    }
                     else if (order["status"] === 4){
                        $("#table_5").append(tr)
                        id = id + 1
                    }
                }
            }
        }
    })

}

function get_detail_order(order_id){
    $.ajax({
            type: 'GET',
            url: "/detailorder",
            data: {"order_id": order_id},
            success: function (response) {
                console.log(response)
                $("#od_id").text(`Mã đơn hàng: #${response["id"]}`)
                $("#od_time").text(`Thời gian: ${response["time"]}`)
                $("#od_address").text(`Địa chỉ: ${response["address"]}`)
                $("#od_name").text(`Tên: ${response["name"]}`)
                $("#od_phone").text(`Số điện thoại: ${response["phone"]}`)
                $("#total").text(response["total"])
                var detail = []
                for (let item of response["detail_order"]){
                    let dongia = item["price"] / item["quality"]
                    var product = `<div class='row'>
									<div class='col-md-3'>
										<img style='width:100px; height: 100px;' src='${item["image"]}'>
									</div>
									<div class='col-md-9'>
										<p>${item['name']}</p>
										<div style='display: flex; justify-content: space-between;'>
											 <p>Số lượng: ${item['quality']}</p>
											 <p style='margin-right:40px;'>${item['price']}</p>
										</div>
										<p>Đơn giá: ${dongia}</p>
									</div>
								</div>
								<hr style='width: 70%'>`
					detail.push(product)
                }
                $("#show_product").html(detail)
                $('#detail_order').modal('show');
            },
            error: function (response) {
                console.log(response)
            }
        })
}
