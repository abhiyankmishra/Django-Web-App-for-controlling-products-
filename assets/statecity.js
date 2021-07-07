$(document).ready(function(){

$.getJSON("/fchstates",function(data){
//alert(data)
$.each(data,function(index,item){
$('#state').append($('<option>').text(item[1]).val(item[0]))

})

})
//
$("#state").change(function(){
$('#city').empty()
$('#city').append($('<option>').text("city"))

$.getJSON("/fchcity",{stateid:$('#state').val()},function(data){
////alert(data)
$.each(data,function(index,item){
$('#city').append($('<option>').text(item[2]).val(item[0]))

})

})
})

})