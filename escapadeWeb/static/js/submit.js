$(document).ready(function () {
    $('#submit').click(function () {
        var content = tinymce.get("texteditor").getContent();
        var region = $(".region option:selected").val();
        var username = localStorage.getItem('user');
        var photo_id = localStorage.getItem('public_id');
        $.ajax({
            url: "http://127.0.0.1:5000/api/writer/submit",
            contentType: 'application/json; charset=utf-8',
            data: JSON.stringify({
                'username': username,
                'content':content,
                'name': region,
                'public_id': photo_id,
            }),
            method: "POST",
            dataType: "json",
            crossDomain: true,
            success: function () {
                console.log("success");
                alert("Submitted!");
                localStorage.removeItem('public_id');
                window.location.href='/writer'
            },
            error: function () {
                console.log('error')
            }
        })
        return false;
    });
    $('#draft').click(function () {
        var content = tinymce.get("texteditor").getContent();
        var region = $(".region option:selected").val();
        var username = localStorage.getItem('user');
        var photo_id = localStorage.getItem('public_id');
        $.ajax({
            url: "http://127.0.0.1:5000/api/writer/draft",
            contentType: 'application/json; charset=utf-8',
            data: JSON.stringify({
                'username': username,
                'content':content,
                'name': region,
                'public_id': photo_id,
            }),
            method: "POST",
            dataType: "json",
            crossDomain: true,
            success: function () {
                console.log("success");
                alert("Submitted!");
                window.location.href='/writer'
            },
            error: function () {
                console.log('error')
            }
        })
        return false;
    });
    $('#cancel').click(function () {
        window.location.href='/writer'
        return false;
    });
})
