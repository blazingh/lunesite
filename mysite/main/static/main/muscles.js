window.addEventListener("load", (event) => {
    document.querySelectorAll('.checks').forEach(item => {
        if (item.checked){
            pick2(item.getAttribute("value"), item.id)
        }})
    });

function pick(svg, check) {
    const grp = document.getElementById(check)
    const id = "#" + svg + " path"

    if (grp.checked) {
        for (const e of document.querySelectorAll(id)) {
            e.setAttribute("style", "fill: var(--color5);");
        }
        grp.setAttribute("checked", "false")
        grp.checked = false;
    } else if (!grp.checked) {
        for (const e of document.querySelectorAll(id)) {
            e.setAttribute("style", "fill: var(--color4);");
        }
        grp.setAttribute("checked", "true")
        grp.checked = true;
    }
}


function pick2(svg, check) {
    const grp = document.getElementById(check)
    const id = "#" + svg + " path"

    if (!grp.checked) {
        for (const e of document.querySelectorAll(id)) {
            e.setAttribute("style", "fill: var(--color5);");
        }
    } else if (grp.checked) {
        for (const e of document.querySelectorAll(id)) {
            e.setAttribute("style", "fill: var(--color4);");
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
var tim = document.getElementById("tim")

tim.innerHTML = slider.value;

slider.oninput = function() {
    document.getElementById("tim").innerHTML = this.value;
}

for (const e of document.querySelectorAll(".equip")) {
    e.addEventListener("click", event => {
        document.getElementById("eno").setAttribute("checked", "false");
        document.getElementById("eno").checked = false;
    })
}

document.getElementById("noe").addEventListener("click", event => {
    for (const e of document.querySelectorAll(".equip")) {
        e.setAttribute("checked", "false");
        e.checked = false;
    }
    document.getElementById("eno").checked = false
    document.getElementById("eno").setAttribute("checked","false")
})

for (const e of document.querySelectorAll(".risks")) {
    e.addEventListener("click", event => {
        document.getElementById("rno").setAttribute("checked", "false");
        document.getElementById("rno").checked = false;
    })
}

document.getElementById("nor").addEventListener("click", event => {
    for (const e of document.querySelectorAll(".risks")) {
        e.setAttribute("checked", "false");
        e.checked = false;
    }
    document.getElementById("rno").checked = false
    document.getElementById("rno").setAttribute("checked","false") 

})

document.addEventListener('click', function(event) {
    for (const e of document.querySelectorAll('.infocheck:checked ~ .hoverinfo')) {
        if (e !== event.target && !e.contains(event.target)) {
            for (const i of document.querySelectorAll(".infocheck")) {
                    if (i !== event.target && !i.contains(event.target)) {
                        i.checked = false
                        i.setAttribute("checked", "fasle")
                        console.log("outside click")
                    }
                }
            
        }
    }
})

function quickselect(part){
    if (part=="full"){
        for (const m of document.querySelectorAll(".checks")){
            m.checked = true
            m.setAttribute("checked", "true")
            pick2(m.getAttribute("value"), m.id)
        }
        return
    }
    if (part=="upper"){
        var section = ["tra", "del", "bic", "tri", "for", "che", "lat", "nec"]
        for (const m of document.querySelectorAll(".checks")){
            m.checked = false
            m.setAttribute("checked", "false")
            pick2(m.getAttribute("value"), m.id)
            if (section.includes(m.id)){
                m.checked = true
                m.setAttribute("checked", "true")
                pick2(m.getAttribute("value"), m.id)
            }
        }
        return
    }
    if (part=="lower"){
        var section = ["qua", "glu", "ham", "cal", "shi"]
        for (const m of document.querySelectorAll(".checks")){
            m.checked = false
            m.setAttribute("checked", "false")
            pick2(m.getAttribute("value"), m.id)
            if (section.includes(m.id)){
                m.checked = true
                m.setAttribute("checked", "true")
                pick2(m.getAttribute("value"), m.id)
            }
        }
        return
    }
    if (part=="clear"){
        for (const m of document.querySelectorAll(".checks")){
            m.checked = false
            m.setAttribute("checked", "false")
            pick2(m.getAttribute("value"), m.id)
        }

    }
}