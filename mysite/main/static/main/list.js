var coll = document.getElementsByClassName("colla");
            var i;

            for (i = 0; i < coll.length; i++) {
            coll[i].addEventListener("click", function() {
                this.classList.toggle("active");
                var content = this.nextElementSibling;
                if (content.style.maxHeight == "500px"){
                content.style.maxHeight = "0px";
                } else {
                content.style.maxHeight = "500px";
                } 
            });
            }

document.getElementById("filter").addEventListener("click", event =>{
    for (let e of document.querySelectorAll(".exsingle")){
        e.style.display = "none"
    }
    for (let l of document.querySelectorAll("input[name=boxl]:checked")){
        var leevl = "." + l.getAttribute("value")
        for (let e of document.querySelectorAll("input[name=boxm]:checked")){
            var calss = "." + e.getAttribute("value")
            for (let r of document.querySelectorAll(leevl+calss)){
                r.style.display = "block"
    }}}
}
)