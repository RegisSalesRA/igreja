function teste(){
    alert('Funcionou!!!');
}

function IgrejaAjaxDeletar(igreja_id){

    token = document.getElementsByName("csrfmiddlewaretoken");

    $.ajax({
        type:'POST',
        url: 'igreja/deletar/'+ igreja_id,
        data:{
            csrfmiddlewaretoken:token
        },
    });
}