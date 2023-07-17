function sendArticleComment(articleId) {
    var comment = $('#commentText').val();
    var parentId = $('#parent_id').val();
    $.get("/articles-list/articles-comment", {
        article_comment: comment,
        article_id: articleId,
        parent_id: parentId
    }).then(res => {
        if (res.status === "success"){
            $('#comment_section').html(res.response)
            $('#commentText').val('');
            $('#parent_id').val('');

}
        if (parentId !== null && parentId !== '') {
            document.getElementById('single_comment_box_' + parentId).scrollIntoView({behavior: "smooth"});
        } else {
            document.getElementById('comment_section').scrollIntoView({behavior: "smooth"});
        }
    });
}

function setparentId(ParentId) {
    $('#parent_id').val(ParentId);
    document.getElementById('comment_form').scrollIntoView({behavior : "smooth"})
}
function ChangeImage(Image){


    $('#main_image').attr('src',Image);
    $('#bigger_picture').attr('href',Image);
}

function ChangePriceFilter(){
    const FilterPrice = $('#sl2').val()
    const min_price = FilterPrice.split(',')[0]
    const max_price = FilterPrice.split(',')[1]
    $('#min_price').val(min_price);
    $('#max_price').val(max_price);
    $('#FilterPrice').submit()
}

function PageNumber(page){
    $('#page').val(page);
     $('#FilterPrice').submit();



}


function AddtoOrder(productId){
    const count = $('#count_input').val()
    $.get('/order/add-to-order?product_id='+ productId + '&count=' + count ).then(res => {
    if (res.status === 'success') {
            Swal.fire({
                title: "محصول مورد نظر با موفقیت به سبد خرید شما اضافه شد",

                icon: 'success',
                showCancelButton: false,
                confirmButtonColor: '#3085d6',
                confirmButtonText: 'باشه ممنون'
            });
        } else if (res.response === 'please login') {
            Swal.fire({
                title: "ابتدا باید به حساب کاربری خود وارد شوید",
                icon: 'warning',
                showCancelButton: false,
                confirmButtonColor: '#ffbb00',
                confirmButtonText: 'باشه'
            });

}
});
}


function DeleteOrder(orderDetailId){
    $.get('/order/delete-user-cart/?order_detail_id='+ orderDetailId).then(res=>{
        if(res.status === 'success' ) {
        console.log($('#delete-cart-response').html(res.response))
        }

    });
}
function changeCount(detailId,state){
    $.get('/order/change-user-cart/?order_detail_id='+ detailId + '&state=' + state).then(res=>{
        if(res.status === 'success' ) {
        console.log($('#delete-cart-response').html(res.response))
        }

    });
}
