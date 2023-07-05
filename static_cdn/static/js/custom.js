function sendArticleComment(articleId) {
    var comment = $('#commentText').val();
    $.get('/articles-list/articles-comment', {
        article_comment: comment,
        article_id: articleId,

    }).then(res => {
        console.log(res);

    });
}
