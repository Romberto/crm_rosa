

function popup_contact(selector, popup_class){
    $(selector).on('click', function(e){
        e.preventDefault()
        $('main').css('filter', 'blur(5px)')
        let top = $(selector).offset()
        top.left = 0
        top.top -=200
        $(popup_class).css(top)
        $(popup_class).fadeIn()
    
        

    })
    
}

//ajax post запрос изменения адрессных данных
function ajax_address(){
    $('#address').on('submit', function(e){

         e.preventDefault();
        const case_id = $('.js_comment_ajax').attr('id')
           $.ajax({
                type : "POST",
                url: "ajax-address/",
                data: $(this).serialize() + '&case_id=' + case_id,
                success: function(data){
                    $('.more_popup').fadeOut()
                    $('main').css('filter', 'none')
                    $('.more_company_name').find('.sub_text').html(data.companyName)
                    $('.more_name').find('.sub_text').html(data.farmerName)
                    $('.more_phone').find('.sub_text').html(data.phone)
                    var email = data.mail
                    if (!email){
                        $('.more_email').html(
                             '<p class="sub_title">почта</p>'+
                             '<p class="sub_text">Это поле ещё не заполнено</p'
                        )
                    }else{
                        $('.more_email').html(
                             '<p class="sub_title">почта</p>'+
                             '<p class="sub_text">'+ email +'</p'
                        )
                    }
                    var address = data.address
                    if (!address){
                         $('.more_adress').html(
                             '<p class="sub_title">адрес</p>'+
                             '<p class="sub_text">Это поле ещё не заполнено</p'
                        )
                    }else{
                         $('.more_adress').html(
                             '<p class="sub_title">адрес</p>'+
                             '<p class="sub_text">'+ address +'</p'
                        )
                    }

                },
                error: function(response) { // Данные не отправлены
                    $('.msg').html('Ошибка. Данные не отправлены.')
                    }
            })
        })
    }


//ajax post запрос изменение тегов
function ajax_tags(){
    $('#tags').on('submit', function(e){
        e.preventDefault()
        const case_id = $('.js_comment_ajax').attr('id')
             $.ajax({
                type : "POST",
                url: "ajax-tags/",
                data: $(this).serialize() + '&case_id=' + case_id,
                success: function(data){
                $('.more_item').remove()
                        $('.more_popup_teg').fadeOut()
                        $('main').css('filter', 'none')
                        if(!data.tegName){
                            $('.more_list').append('<li class="more_item">выберете теги</li>')
                        }else{
                            $.each(data.tegName, function(index, value){
                                $('.more_list').append('<li class="more_item">' + value + '</li>')
                        })
                        }

                    },

                errors: function(){
                    $('.tag_msg').html('Ошибка. Данные не отправлены.')
                }
        })
    })
}

//ajax post запрос добавляет комментарии к сделке

function ajax_comment(){
    $('#comment').on('submit', function(e){
        e.preventDefault()
        const case_id = $('.js_comment_ajax').attr('id')
        $.ajax({
            type: "post",
            url: "ajax-comment/",
            data: $(this).serialize() + '&case_id=' + case_id,
            success:function(response){
                        $('.more_popup_comment').fadeOut()
                        $('main').css('filter', 'none')
                        $('.more_comment_item').remove()
                        $.each(response, function(index, value){
                            var date = new Date(response[index][0]['date_created'])
                            date = date.toLocaleString("ru")
                            $('.more_comment_list').prepend(
                            '<li class="more_comment_item">'+
                                '<p class="sub_text comment_date">' + date + '</p>'+
                                '<p class="sub_text">' + response[index][0]['text_comment'] + '</p>'+
                                '<div class="comment_delimetr"></div>'+
                            '</li>'
                        )
                        })

            },
            errors: function(){
                $('.comment_msg').html('Ошибка. Данные не отправлены.')
            }
        })
        $('.more_popup_comment').fadeOut()
        $('main').css('filter', 'none')

    })
}

//ajax запрос меняет статус сделки

function ajax_status(){
        const case_id = $('.js_comment_ajax').attr('id')
        $('.js_status_btn').on('click', function(e){
            const new_status_nameBtn = $(this).attr('name')
            $('.js_status_btn').removeClass('is_active')
            $(this).addClass('is_active')

            $.ajax({
                type: "post",
                url: "ajax-status/",
                data:'&case_id=' + case_id + '&nameBtn=' + new_status_nameBtn,
                success:function(response){
                    $('.more_status').find('.sub_text').text(response.description)
                    $('.status_msg').text('статус изменён')
                    $('.more_popup_status').fadeOut()
                    $('main').css('filter', 'none')
                },
                errors: function(response){
                   $('.status_msg').text(response.errors)
                }
            })
        })

}

function close_popup(){
    $('.close_popup_btn').on('click', function(){
        $('.more_popup_teg, .more_popup, .more_popup_comment, .more_popup_status').fadeOut()
        $('main').css('filter', 'none')
    })
}

    
$( document ).ready(function() {
    popup_contact('.js_more_contact', '.more_popup')
    popup_contact('.js_more_tegs', '.more_popup_teg')
    popup_contact('.js_more_comment', '.more_popup_comment' )
    popup_contact('.js_more_status', '.more_popup_status')
    close_popup()
    ajax_address()
    ajax_tags()
    ajax_status()
    ajax_comment()
});




