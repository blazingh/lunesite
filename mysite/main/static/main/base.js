const burger = document.getElementById("burger");
const menus =  document.getElementById("menus");

burger.addEventListener("click", () => {
    if (menus.style.display == "flex"){
        menus.style.display = "none"
    }else{
        menus.style.display = "flex"
    }
});

function endAlert(){
    document.getElementById("alertback").style = "display: none"
}

function startAlert(backmessage){
    document.getElementById("labelmessage").innerHTML = backmessage
    document.getElementById("alertback").style = "display: block"
}

function validateForm(form){
    if (form=="generatorform"){
        let musclcount = 0
        for (let e of document.querySelectorAll('input[name=muscle]')){
            if (e.checked){
                musclcount += 1
            }
        }
        if (musclcount >= 2){
            document.forms[form].submit();
            return 
        }
        if (musclcount == 1 ){
            startAlert("Please select at least two muscles")
            return
        }
        startAlert("oops! You haven't selected any muscles")
    }
    if (form=="adderform"){
        if (document.getElementById('exercisename').value < 1){
            startAlert("You forgot to name the exercise")
            return
        }
        if (document.getElementById('ex_info_text').value < 10){
            startAlert("Please give more details about the exercise")
            return
        }
        for (let e of document.querySelectorAll('input[name=muscle]')){
            if (e.checked){
                document.forms[form].submit();
                return
            }
        }
        startAlert("oops! You haven't selected any muscles")
        return
    }
}