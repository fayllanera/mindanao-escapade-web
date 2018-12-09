$(document).ready(function () {
    $('#publish').click(function () {
        var content = tinymce.get("texteditor").getContent();
        var region = $(".region option:selected").val();
        var write_id = $("#writeid").val();
        $.ajax({
            url: "http://127.0.0.1:5000/api/editor/publish/region",
            contentType: 'application/json; charset=utf-8',
            data: JSON.stringify({
                'write_id': write_id,
                'content':content,
                'region': region,
            }),
            method: "POST",
            dataType: "json",
            crossDomain: true,
            success: function () {
                console.log("success");
                alert("Submitted!");
                window.location.href='/editor/submissions/1'
            },
            error: function () {
                console.log('error')
            }
        })
        return false;
    });
    $('#check').click(function () {
        var content = tinymce.get("texteditor").getContent();
        var region = $(".region option:selected").val();
        var write_id = $("#writeid").val();
        var comment = $("#comment").val();
        $.ajax({
            url: "http://127.0.0.1:5000/api/editor/edit/region",
            contentType: 'application/json; charset=utf-8',
            data: JSON.stringify({
                'write_id': write_id,
                'content':content,
                'region': region,
                'comment': comment,
            }),
            method: "POST",
            dataType: "json",
            crossDomain: true,
            success: function () {
                console.log("success");
                alert("Submitted!");
                window.location.href='/editor/submissions/1'
            },
            error: function () {
                console.log('error')
            }
        })
        return false;
    });
    $('#delete').click(function () {
        var write_id = $("#writeid").val();
        $.ajax({
            url: "http://127.0.0.1:5000/api/editor/delete/region",
            contentType: 'application/json; charset=utf-8',
            data: JSON.stringify({
                'write_id': write_id,
            }),
            method: "POST",
            dataType: "json",
            crossDomain: true,
            success: function () {
                console.log("success");
                alert("Submitted!");
                window.location.href='/editor/submissions/1'
            },
            error: function () {
                console.log('error')
            }
        })
        return false;
    });
})


