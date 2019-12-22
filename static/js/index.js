$(

    $(document).ready(function(){
        $('[data-toggle="popover"]').popover();   
    }),
    // 初始化popover
    
    $('.name').mouseover(
        // 在点击class属性值为name的元素时，执行下面的函数操作
        function(){
            // console.log($(this).prev().text());
            let num = $(this).prev().text();
            // 取到被点击元素的上一个元素的文本内容，赋值给num
            $('#' + num).click();
            // modal(
            // // id为上面取到的num值的模态框弹出
            //     'toggle',
            //     {keyboard:true},
            //     // 设置按Esc键关闭模态框
            //     );
        }
    ),

    $('.name').mouseout(
        // 在点击class属性值为name的元素时，执行下面的函数操作
        function(){
            // console.log($(this).prev().text());
            let num = $(this).prev().text();
            // 取到被点击元素的上一个元素的文本内容，赋值给num
            $('#' + num).click();
            // modal(
            // // id为上面取到的num值的模态框弹出
            //     'toggle',
            //     {keyboard:true},
            //     // 设置按Esc键关闭模态框
            //     );
        }
    ),

    // $('#').mouseover(
    //     function(){
    //         console.log($(this).text());
    //         $(this).click();
    //     }
    // ),

    // $('#test').mouseout(
    //     function(){
    //         console.log($(this).text());
    //         $(this).click();
    //     }
    // ),

    

    // $('.name').mouseout(
    //     function(){
    //     console.log('good');
    //     $('.btn-secondary').click();
    //     // $('#myModal').modal(options);
    // }
    // ),


    
)