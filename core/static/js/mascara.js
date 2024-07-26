$(function(){
    $('.mask-cpf').mask('000.000.000-00', {reverse: true});
    $('#formCreateCliente').on('submit', function(){
        $('.mask-cpf').unmask();
    });
});
