function add_like(counter, pk) {
    let id = 'button-like' + pk;
    let button_likes = document.getElementById(id);
    let data = {};
    data.likes = parseInt(button_likes.value);
    data.question_id = button_likes.dataset.question_id;
    data.pk = pk;
    let url = $(button_likes).attr("action");
    $.ajax({
        url: url,
        type: 'GET',
        data: data,
        cache: true,
        success: function (response) {
            button_likes.value = response
        },
        error: function () {
            alert('Sorry, something went wrong!')
        }
    });
}

