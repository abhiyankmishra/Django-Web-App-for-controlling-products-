$(document).ready(function(){

$.getJSON("/fetchcategories",function(data){
//alert(data)
$.each(data,function(index,item){
$('#categoryid').append($('<option>').text(item[2]).val(item[1]))

})

})
//
//$('#categoryid').change(function(){
//$('#subcategoryid').empty()
//$('#subcategoryid').append('<option>').text("Sub-Category")
//
//$.getJSON("/fetchsubcategories",{categoryid:$('#categoryid').val()},function(data){
//
//$.each(data,function(index,item){
//$('#subcategoryid').append($('<option>').text(item[3]).val(item[2]))
//
//})
//})
//
//
//
//})
//
//
//})

$("#categoryid").change(function(){
$('#subcategoryid').empty()
$('#subcategoryid').append($('<option>').text("Sub-Category"))

$.getJSON("/fetchsubcategories",{categoryid:$('#categoryid').val()},function(data){
//alert(data)
$.each(data,function(index,item){
$('#subcategoryid').append($('<option>').text(item[3]).val(item[2]))

})

})
})

 $('#subcategoryid').change(function () {


            $.getJSON("/fetchmodels", {subcategoryid: $('#subcategoryid').val()}, function (data) {
                $('#modelid').empty()
                $('#modelid').append($('<option>').text("-Select Model-"))
                $.each(data, function (index, item) {
                    $('#modelid').append($('<option>').text(item[4]).val(item[3]))
                })
            })
        })



    })


