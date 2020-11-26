
        function getname() {
            var inpout = $('#note').val();
            //wyqajax('/getname',type=post,inpout)
            $.ajax({
                url: '/getname/',//请求路径
                type: 'post',            //请求方式
                //(2)JSON数据请求
                async: true,
                timeout: 2000,
                dataType: 'json',
                contentType: 'application/json;charset=UTF-8',
                headers: {'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val()},//在请求头通过csrf认证，键固定
                data: JSON.stringify({rdata: inpout}),
                success: function (data) {//请求回调函数

                    if (data.error == 0) {
                        alert(data.error_msg)
                        $('#note').val(data.ages_info );

                    } else if (data.error == 4500){
                        return  alert(data.error_msg)
                    }

                    else {
                        return alert('内部失败')
                    }

                }
            })

        }

