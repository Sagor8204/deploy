function showMsg(itemId) {
    var item = '#m' + itemId.toString();
    var id = '#' + itemId.toString();
    var msg = $(item).val();
    var par = document.getElementById("msgBody");
    par.innerHTML = msg;
    var url = $(id).val();
    var btn = document.getElementById("queryBtn");
    var site = window.location.origin;
    url = site + url;
    console.log(url);
    $(btn).attr('href', url);
}