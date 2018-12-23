document.addEventListener('DOMContentLoaded', function () {
$('#article-like-heart').click(function() {
            $(this)
                .toggleClass('far fa-heart fa-lg')
                .toggleClass('fas fa-heart fa-lg');
        });
$('#article-watchers-eye-not-watched').click(function() {
            $(this)
                .toggleClass('far fa-eye fa-lg')
                .toggleClass('fas fa-eye fa-lg');
        });
    });
