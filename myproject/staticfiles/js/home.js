document.addEventListener('DOMContentLoaded', function () {
    const toggleBtn = document.querySelector('.toggle_btn');
    const toggleBtnIcon = toggleBtn.querySelector('i');
    const dropDownMenu = toggleBtn.querySelector('.dropdown_menu');
    
    dropDownMenu.style.display = 'none';
    
    toggleBtn.addEventListener('click', function () {
        dropDownMenu.classList.toggle('open');
        toggleBtnIcon.classList.toggle('fa-bars');
        toggleBtnIcon.classList.toggle('fa-xmark');

        if (toggleBtnIcon.classList.contains('fa-xmark')) {
            dropDownMenu.style.display = 'block';
        } else {
            dropDownMenu.style.display = 'none';
        }
    });
});


// Moving Image (Click)
var btn = document.getElementsByClassName("btn")
var banner = document.getElementById("banner")

function animation(){
    banner.classList.add('fadeinout');
    setTimeout(function () {
        banner.classList.remove('fadeinout');
    },500)

    for(b of btn){
        b.classList.remove('active');
    }
}

btn[0].onclick = function () {
    banner.src = '../Image/Background_Fatahillah1.png';
    animation();
    this.classList.add('active');
}
btn[1].onclick = function () {
    banner.src = '../Image/Background_Mandiri1.png';
    animation();
    this.classList.add('active');
}
btn[2].onclick = function () {
    banner.src = '../Image/Background_BankIndonesia1.png';
    animation();
    this.classList.add('active');
}

