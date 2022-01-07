
$( document ).ready(function() {
  var total_cart_money = parseInt($("#total-cart-money").text())
  var ship = parseInt($("#ship").text())
  $("#total_money").text(ship + total_cart_money)
  $("#btnSubmit").on("click", function(){
    $("#checkout").submit()
  })
})