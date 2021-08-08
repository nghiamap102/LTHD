const toggleSwitch = document.querySelector('.theme-switch input[type="checkbox"] ');
const currentTheme = localStorage.getItem('theme');

document.documentElement.setAttribute('data-theme', currentTheme);
if (currentTheme === 'dark') {
    toggleSwitch.checked = true;
}

function switchTheme(e) {
    if (e.target.checked) {
        document.documentElement.setAttribute('data-theme', 'dark');
        localStorage.setItem('theme', 'dark');
        document.getElementById('moon').style.display = 'none';
        document.getElementById('sun').style.display = 'block ';
    } else {
        document.documentElement.setAttribute('data-theme', 'light');
        localStorage.setItem('theme', 'light');
        document.getElementById('moon').style.display = 'block';
        document.getElementById('sun').style.display = 'none';
    }
}
toggleSwitch.addEventListener('change', switchTheme);