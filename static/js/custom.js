function sendArticleComment(articleId) {
    var comment = $('#commentText').val();
    var parentId = $('#parent_id').val();
    $.get("/articles-list/articles-comment", {
        article_comment: comment,
        article_id: articleId,
        parent_id : parentId

    }).then(res => {
        $('#comment_section').html(res) ;



    });


}

function setparentId(ParentId) {
    $('#parent_id').val(ParentId);
    document.getElementById('comment_form').scrollIntoView({behavior : "smooth"})
}