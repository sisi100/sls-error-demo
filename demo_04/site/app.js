function sent_msg() {
    $.ajax({
        url:'https://xxxxxxxxxx/dev/counter', // ←←← デプロイしたAPIのエンドポイントを入力してね！
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