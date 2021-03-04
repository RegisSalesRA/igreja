function deletar_Musica(id) {
  var action = confirm("Are you sure you want to delete this user?");
  if (action != false) {
    $.ajax({
        url: '{% url "deletar_musica" %}',
        data: {
            'id': id,
        },
        dataType: 'json',
        success: function (data) {
            if (data.deleted) {
              $("#musicaTable #musica-" + id).remove();
            }
        }
    });
    setTimeout(function() {
    location.reload();
}, 200);
}
}

function teste(){
  alert('funcionando!!!')
}
