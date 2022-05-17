function pick(svg, check){
    const grp = document.getElementById(check)
    const id = "#" + svg + " path"
    
    if (grp.checked){
        for (const e of document.querySelectorAll(id)){
            e.setAttribute("style", "fill: grey;");
        }
        grp.setAttribute("checked", "false")
        grp.checked = false;
    }else if(!grp.checked){
        for (const e of document.querySelectorAll(id)){
            e.setAttribute("style", "fill: rgb(255, 77, 77) ;");
        }
        grp.setAttribute("checked", "true")
        grp.checked = true;
    }
}

function pick2(svg, check){
    const grp = document.getElementById(check)
    const id = "#" + svg + " path"
    
    if (!grp.checked){
        for (const e of document.querySelectorAll(id)){
            e.setAttribute("style", "fill: grey;");
        }
    }else if(grp.checked){
        for (const e of document.querySelectorAll(id)){
            e.setAttribute("style", "fill: rgb(255, 77, 77) ;");
        }
    }
}

document.querySelectorAll('.groups').forEach(item => {
    item.addEventListener('click', event => {
        pick(item.id, item.getAttribute("name"))
    })
})

document.querySelectorAll('.checks').forEach(item => {
    item.addEventListener('click', event => {
        pick2(item.getAttribute("value"), item.id)
    })
})      

var slider = document.getElementById("time")
var tim =  document.getElementById("tim")

tim.innerHTML = slider.value;

slider.oninput = function(){
    document.getElementById("tim").innerHTML = this.value;
}