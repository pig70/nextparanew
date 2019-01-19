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
    if ( currentLength == maxlength ) {
        document.getElementById("count").innerHTML = "No more characters left";
    } else {
        document.getElementById("count").innerHTML = (maxlength - currentLength) + " characters left";
    }
});

// Toggle hide

document.getElementById("toggle-hide").onclick = toggleContent;
function toggleContent(){
    document.getElementById("story-para-author").style.display = 'none';
}
