function sort_by_topic(topic_pk) {
    console.log(topic_pk);
    let id = 'topic' + topic_pk;
    let url = document.getElementById(id).getAttribute("action");
    let data = {};
    data.topic_pk = topic_pk;
    $.ajax({
        url: url,
        type: 'GET',
        data: data,
        success: function (response) {
            document.getElementsByTagName("body").innerHTML = data["object_list"];
        },
        error: function () {
            alert('Sorry, something went wrong!')
        }
    })
}