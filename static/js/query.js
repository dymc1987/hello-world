$(
    // function() {
    //     console.log($('input')[0]);
    // },

    $('#customRadio1').on('click',function(){
        $('.form-control').attr({ placeholder:"输入姓名", name:"name" });
    }
    ),

    $('#customRadio2').on('click',function(){
        $('.form-control').attr({ placeholder:"输入部门名称", name:"department" });
    }
    ),

    $('#customRadio3').on('click',function(){
        $('.form-control').attr({ placeholder:"输入SN码", name:"sn" });
    }
    ),

    $('#customRadio4').on('click',function(){
        $('.form-control').attr({ placeholder:"输入计算机类型", name:"pc_type" });
    }
    ),
)