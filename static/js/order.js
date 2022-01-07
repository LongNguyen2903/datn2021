$( document ).ready(function() {
    $("#order_table tbody").on('click', 'tr', function(e){
        var order_id = $(this).find('td:eq(1)').text()
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

    })
});

