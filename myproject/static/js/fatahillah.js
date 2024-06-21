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