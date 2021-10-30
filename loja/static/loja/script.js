function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

// Função responsável por fazer o delete dos itens.
function deletarPorId(url, id) {
    var endereco = url + "/" + id;

    if (window.confirm('Deseja realmente excluir este produto?')) {
        const request = new Request(
            endereco,
            {headers: {'X-CSRFToken': csrftoken}}
        );
        fetch(request, {
            method: 'POST',
            mode: 'same-origin'  // Do not send CSRF token to another domain.
        }).then(function(response) {
            window.location.href = response.url
        }).catch((e)=>{
            console.log(e);
        });
    }
}

// Adicionando valores ao modal.
function putInModal(id, nome, preco, fabricante, categoria_id, quantidade) {
    var _id, _nome, _preco, _fabricante, _categoria_id, _quantidade;

    _id = document.getElementById('identifier').value = id;
    _nome = document.getElementById('nomem').value = nome;
    _preco = document.getElementById('precom').value = preco;
    _fabricante = document.getElementById('fabricantem').value = fabricante;
    _categoria_id = document.getElementById('sel1m').value = categoria_id;
    _quantidade = document.getElementById('quantidadem').value = quantidade;

}