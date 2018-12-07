var CLOUDINARY_URL =  'https://api.cloudinary.com/v1_1/diit9i4hz/image/upload';
var CLOUDINARY_UPLOAD_PRESET = 'irbltunb';

var imgPreview = document.getElementById('img-preview');
var fileUpload = document.getElementById('file-upload');

fileUpload.addEventListener('change', function(event) {
    var file = event.target.files[0];
    var formData = new FormData();
    formData.append('file', file);
    formData.append('upload_preset', CLOUDINARY_UPLOAD_PRESET)

    axios({
        url: CLOUDINARY_URL,
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        data: formData
    }).then(function(res) {
        $.ajax({
            url: "http://127.0.0.1:5000/api/writer/upload",
            contentType: 'application/json; charset=utf-8',
            data: JSON.stringify({
                'public_id': res.data.public_id,
                'secure_url': res.data.secure_url,
                'url': res.data.url,
            }),
            method: "POST",
            dataType: "json",
            crossDomain: true,
            success: function () {
                console.log("success");
                alert("Submitted!");
            },
            error: function () {
                console.log('error')
            }
        });
        console.log(res);
        imgPreview.src = res.data.secure_url;
        localStorage.setItem('public_id', res.data.public_id);
    }).catch(function(err) {
        console.log(err);
    });

});