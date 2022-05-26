const burger = document.getElementById("burger");
const menus =  document.getElementById("menus");

burger.addEventListener("click", () => {
    if (menus.style.display == "flex"){
        menus.style.display = "none"
    }else{
        menus.style.display = "flex"
    }
});