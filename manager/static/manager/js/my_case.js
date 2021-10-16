function popup_phone(selector){
    $(selector).on('click', function(e){
        e.preventDefault()
        let phone = $(this).find('.js_phone_case').text()
        $('.popup_phone_number').text(phone)
        let href_phone = "tel:"+phone
        $('.popup_phone_link').attr('href', href_phone)
        $('header, main').css('filter', 'blur(5px)')
        $('.popup_phone').fadeIn()

        $('.js_popup_phone_btn').on('click', function(){
            $('.popup_phone').fadeOut()
            $('header, main').css('filter', 'none')
        })
    })
}

function popup_adress(selector){
    $(selector).on('click', function(e){
        e.preventDefault()
        let address = $(this).find('.js_address_case').text()
        if(!address){
            $('.popup_adress_text').text('адрес пока не вносили')
        }
        else{
            $('.popup_adress_text').text(address)
        }

        $('header, main').css('filter', 'blur(5px)')
        $('.popup_adress').fadeIn()
        $('.js_popup_phone_btn').on('click', function(){
            $('.popup_adress').fadeOut()
            $('header, main').css('filter', 'none')
        })
    })
}

function ajax_phone(){

}

$( document ).ready(function() {
    popup_phone('.cartlinkPhone')
    popup_adress('.cartlinkAdress')

});


