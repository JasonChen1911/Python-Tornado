 function getCookie(name){
    var x = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return x ? x[1]:undefined;
}

$(document).ready(function(){
    $("#submitbtn").click(function(){
        var user = $("#username").val();
        var pwd = $("#password").val();
        var pd = {"username":user, "password":pwd, "_xsrf" : getCookie("_xsrf")};
        $.ajax({
            type:"post",
            url:"/SignIn",
            data:pd,
            cache:false,
            success:function(data){
                window.location.href = "/user?username="+data;
            },
            error:function(){
                alert("error!");
            },
        });
    });
    $("#registerbtn").click(function () {
        var user = $("#username").val();
        var pwd1 = $("#password1").val();
        var pwd2 = $("#password2").val();
        var email = $("#email").val();
        var pd = {"username":user, "password1":pwd1, "password2":pwd2, "email":email, "_xsrf": getCookie("_xsrf")};
        alert(pd);
        $.ajax({
            type:"post",
            url:"/SignOn",
            data:pd,
            cache:false,
            success:function (data) {
                alert(data);
            },
            error:function () {
                alert("error!");
            },
        });
    });
});


