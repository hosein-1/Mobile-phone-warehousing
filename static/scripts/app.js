const messeageClose = document.querySelectorAll(".message-close");
const toastMessage = document.querySelectorAll(".toast-message");

messeageClose.forEach((btn,i) => {
    btn.addEventListener("click", function(){
        toastMessage[i].style.display = "none";
        
    })
})