/* 
    Script para detectar quando o user está na página 'home'
    Autor: Matheus Wirz (UFFinance)
*/
setInterval(function(){
    var path = window.location.pathname.replace('/', '') || 'home';

    document.body.setAttribute('data-path', path)
}, 300);