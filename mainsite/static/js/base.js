document.addEventListener('DOMContentLoaded', function () {
    $('body #article-like-heart').click(function () {
        $(this)
            .toggleClass('far fa-heart fa-lg')
            .toggleClass('fas fa-heart fa-lg');
    });
    $('#article-watchers-eye-not-watched').click(function () {
        $(this)
            .toggleClass('far fa-eye fa-lg')
            .toggleClass('fas fa-eye fa-lg');
    });
});

// Character count

var textarea = document.querySelector("textarea");
var maxlength = textarea.getAttribute("maxlength");

textarea.addEventListener("input", function () {
    var currentLength = this.value.length;
    if (currentLength == maxlength) {
        document.getElementById("count").innerHTML = "No more characters left";
    } else {
        document.getElementById("count").innerHTML = (maxlength - currentLength) + " characters left";
    }
});

// Toggle hide

var hideAuthor = document.getElementsByClassName("article-paragraph-author-name");
var hideAuthorImage = document.getElementsByClassName("article-paragraph-author-image");
var hideStoryLike = document.getElementsByClassName("nextparagraph-like");
var hideAddParagraphForm = document.getElementById('add-paragraph-form');
var hideStoryDate = document.getElementById('story-date');
var hideStoryTags = document.getElementById('story-tags');
var hideStorySubhead = document.getElementsByClassName('article-sub-head');
var hideStoryWatchers = document.getElementById('story-watchers');

document.getElementById("toggle-hide").onclick = function () {
    for (var i = 0; i < hideAuthor.length; i++) {
        hideAuthor[i].classList.toggle('display-none')
    }
    for (var i = 0; i < hideAuthorImage.length; i++) {
        hideAuthorImage[i].classList.toggle('display-none')
    }
    for (var i = 0; i < hideStoryLike.length; i++) {
        hideStoryLike[i].classList.toggle('display-none')
    }
    for (var i = 0; i < hideStorySubhead.length; i++) {
        hideStorySubhead[i].classList.toggle('display-none')
    }
    hideAddParagraphForm.classList.toggle('display-none')
    hideStoryDate.classList.toggle('display-none')
    hideStoryTags.classList.toggle('display-none')
    hideStoryWatchers.classList.toggle('display-none')
}