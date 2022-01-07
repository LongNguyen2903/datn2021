$( document ).ready(function() {

    $("#id_U_password").on('input', function(){
        if (($("#id_U_password").val()).length > 0 && ($("#id_U_password").val()).length < 8) {
            $("#password").attr('style', 'display:block')
            $("#password").text("Mật khẩu phải có ít nhất 8 ký tự")
        } else {
            $("#password").text("")
            $("#password").attr('style', 'display:none')
        }
    })

    $("#id_U_repeat_password").on('input', function(){
        var pwd = $("#id_U_password").val()
        if (pwd != "" && $(this).val().length > 0 && $(this).val() === pwd) {

            $("#repeat_password").text("")
            $("#repeat_password").attr('style', 'display:none')

        } else {
            $("#repeat_password").attr('style', 'display:block')
            $("#repeat_password").text("Mật khẩu không khớp")
        }
    })

    $("#id_U_phone").on('input', function(){

        if ($(this).val() != ""){

            if (checkPhoneNumber($(this).val())) {
                $("#message_phone").attr('style', 'display:none')
                $("#message_phone").text("")
            } else {

                 $("#message_phone").attr('style', 'display:block')
                $("#message_phone").text("Số điện thoại không hợp lệ")
            }

        }
    })


});

function checkPhoneNumber(phone_input) {
    var flag = false;
    var phone = phone_input.trim(); // ID của trường Số điện thoại
    phone = phone.replace('(+84)', '0');
    phone = phone.replace('+84', '0');
    phone = phone.replace('0084', '0');
    phone = phone.replace(/ /g, '');
    if (phone != '') {
        var firstNumber = phone.substring(0, 2);
        if ((firstNumber == '09' || firstNumber == '08') && phone.length == 10) {
            if (phone.match(/^\d{10}/)) {
                flag = true;
            }
        } else if (firstNumber == '01' && phone.length == 11) {
            if (phone.match(/^\d{11}/)) {
                flag = true;
            }
        }
    }
    return flag;
}