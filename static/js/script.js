

$("#form1").following_btn(function() {
    alert("dddd");
    var user_id = $("#following_btn").attr('data-id')
    var follow = $("#following_btn").text()
alert(user_id);
    if (follow == "Follow"){

        var url = "/accounts/follow/"
        var btn_text = "Unfollow"


    }

    else{
        var url = "/accounts/unfollow/"
        var btn_text = "Follow"

    }
    
    $.ajax({
        url : url,
        method : "POST",
        data :{
            'user_ids' :user_id,
        },
        success : function(data){
            if(data['status'] == 'ok'){
                $('#following-btn').text(btn_text)
            }
        }

    })

})