$(
    // function() {
    //     console.log($('input')[0]);
    // },

    $('#customRadio1').on('click',function(){
        $('.form-control').attr({ placeholder:"输入姓名", name:"name" });
    }
    ),

    $('#customRadio2').on('click',function(){
        $('.form-control').attr({ placeholder:"输入SN码", name:"sn" });
    }
    ),
)