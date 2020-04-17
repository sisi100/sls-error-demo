function sent_msg() {
    $.ajax({
        url:'https://5kkcbmfhp2.execute-api.ap-northeast-1.amazonaws.com/dev/counter',
        type:'POST',
        data:{
            'url':location.href,
        }
    })
    .done((result) => {
        console.log(result);
        $('#bbb').text(result["visitor"]);
    })
    .fail((result) => {
        console.log(result);
        $('#bbb').text('エラー');
    })
}
sent_msg()