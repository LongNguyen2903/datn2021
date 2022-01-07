$( document ).ready(function() {
        $("#search_product_sold").on('click',function(e){
            var time = $("#date_sold").val()
            if (time) {
                 $.ajax({
                    type: 'GET',
                    url: "/product_sold",
                    data: {"time": time},
                    cache: false,
                    beforeSend: function(){
                        $('#div_table_sold').empty();
                    },
                    success: function(data){
                        $("#div_table_sold").html(`<table id="table_sold" style="width:100%">
                         </table>`)
                        $("#table_sold").DataTable({
                            dom: 'Bfrtip',
                            data: data['data'],
                            columns: [
                                {'title': 'Tên sản phẩm', data: 'name'},
                                {'title': 'Số lượng', data: 'quantity'},
                                {'title': 'Tổng số tiền', data: 'price'},
                            ],
                            button: ['excel', 'print'],
                        })
                    }
                })
            }
        })
         $("#search_order_date").on('click',function(e){
            var status_order = $("#pending_order").val()
            var time = $("#date_order").val()
            if (status_order) {
                 $.ajax({
                    type: 'GET',
                    url: "/order_sold",
                    data: {"status_order":status_order, "time":time},
                    cache: false,
                    beforeSend: function(){
                        $('#div_table_order').empty()
                    },
                    success: function(data){
                        $('#div_table_order').html(`<table id="table_order" style="width:100%">
                        </table>`)
                       $("#table_order").DataTable({
                            dom: 'Bfrtip',

                            data: data['data'],
                            columns: [
                                {'title': 'Mã đơn hàng', data: 'id'},
                                {'title': 'Người mua', data: 'name'},
                                {'title': 'Tổng số tiền', data: 'price'},

                            ],
                            button: ['excel', 'print'],
                        })
                    }
                })
            }
        })
         $("#search_all_product").on('click',function(e){
                 $.ajax({
                    type: 'GET',
                    url: "/all_product",
                    beforeSend: function(){
                        $('#div_table_product').empty()
                    },
                    success: function(data){
                        $('#div_table_product').html(`<table id="table_product" style="width:100%">
                        </table>`)
                       $("#table_product").DataTable({
                            dom: 'Bfrtip',
                            data: data['data'],
                            columns: [
                                {'title': 'Mã sản phẩm', data: 'id'},
                                {'title': 'Tên sản phẩm', data: 'name'},
                                {'title': 'Số lượng đang có', data: 'quantity'},
                                {'title': 'Số lượng đã bán', data: 'quantity_sold'},

                            ],
                            button: ['excel', 'print'],
                        })
                    }
                })

        })
        $("#search_product_import").on('click',function(e){
                 var time = $('#imports_date').val()
                 if(time){
                 $.ajax({
                    type: 'GET',
                    url: "/product_import",
                    data: {"time": time},
                    cache: false,
                    beforeSend: function(){
                        $('#div_table_product_import').empty()
                    },
                    success: function(data){
                        $('#div_table_product_import').html(`<table id="table_product_import" style="width:100%">
                        </table>`)
                       $("#table_product_import").DataTable({
                            dom: 'Bfrtip',
                            data: data['data'],
                            columns: [
                                {'title': 'Tên sản phẩm', data: 'name'},
                                {'title': 'Số lượng nhập', data: 'quantity'},
                                {'title': 'Giá nhập', data: 'price_import'},
                                {'title': 'Nhà cung cấp', data: 'import'},
                                {'title': 'Tổng tiền', data: 'total_money'},
                            ],
                            button: ['excel', 'print'],
                        })
                    }
                })
             }
        })
})


function openStatistic(type){
    if (type ==='1') {
        $("#statistic_1").show()
        $("#statistic_2").hide()
        $("#statistic_3").hide()
        $("#statistic_4").hide()
        $("#button_1").addClass('active')
        $("#button_2").removeClass('active')
        $("#button_3").removeClass('active')
        $("#button_4").removeClass('active')

    }else if (type ==='2') {
        $("#statistic_1").hide()
        $("#statistic_2").show()
        $("#statistic_3").hide()
        $("#statistic_4").hide()
        $("#button_1").removeClass('active')
        $("#button_2").addClass('active')
        $("#button_3").removeClass('active')
        $("#button_4").removeClass('active')
    }else if (type ==='3'){
        $("#statistic_1").hide()
        $("#statistic_2").hide()
        $("#statistic_3").show()
        $("#statistic_4").hide()
        $("#button_1").removeClass('active')
        $("#button_2").removeClass('active')
        $("#button_3").addClass('active')
        $("#button_4").removeClass('active')
    }else {
        $("#statistic_1").hide()
        $("#statistic_2").hide()
        $("#statistic_3").hide()
        $("#statistic_4").show()
        $("#button_1").removeClass('active')
        $("#button_2").removeClass('active')
        $("#button_3").removeClass('active')
        $("#button_4").addClass('active')
    }

}