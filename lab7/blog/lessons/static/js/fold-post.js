var foldBtns = document.getElementsByClassName("fold-button");

for (var i = 0; i < foldBtns.length; i++) {
    foldBtns[i].addEventListener("click", function(e) {
        var post = e.target.parentElement;

        if (post.classList.contains("folded")) {
            post.classList.remove("folded");
            e.target.innerHTML = "свернуть";
        } else {
            post.classList.add("folded");
            e.target.innerHTML = "развернуть";
        }
    });
}