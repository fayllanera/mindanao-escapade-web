function markread() {
    var redmark = document.getElementById('redmark');
    var ajax = $.ajax({
    type: "POST",
    url: "http://localhost:8000/mark-read/editor",
    dataType: "json",
    contentType: "application/json; charset=UTF-8",
    success : function(data) {
                console.log(data);
                redmark.style["display"] = "none";
            },
    });
}

function markread2() {
    var redmark = document.getElementById('redmark');
    var ajax = $.ajax({
    type: "POST",
    url: "http://localhost:8000/mark-read/writer",
    dataType: "json",
    contentType: "application/json; charset=UTF-8",
    success : function(data) {
                console.log(data);
                redmark.style["display"] = "none";
            },
    });
}