$(document).ready(function () {
    $('#get-data-form').submit(function () {
        var content = tinymce.get("texteditor").getContent();
        var region = $(".region option:selected").val();
        var username = localStorage.getItem('user')
        $.ajax({
            url: "http://127.0.0.1:5000/api/writer/submit",
            contentType: 'application/json; charset=utf-8',
            data: JSON.stringify({
                'username': username,
                'content':content,
                'name': region,
            }),
            method: "POST",
            dataType: "json",
            crossDomain: true,
            success: function () {
                console.log("success");
                alert("Submitted!");
                window.location.href='/writer/region'
            },
            error: function () {
                console.log('error')
            }
        })
        return false;
    });
})
