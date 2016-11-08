function TestHello(url_path){
    $.ajax({
        url:url_path,
        type:'get',
        success:function(data){
            var str = '';
            for(var name in data){
                str += '<li>'+data[name]+'<li>';
            }
            $('#result').html('<ul>'+str+'</ul>');
        }
    })
    return false;
}
