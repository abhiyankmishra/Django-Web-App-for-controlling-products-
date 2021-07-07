$(document).ready(function(){

$.getJSON("/fetchprods",{compid:$('#comp').val()},function(data){
//alert(data)
$.each(data,function(index,item){
$('#prod').append($('<option>').text(item[5]).val(item[0]))

})

})
})
