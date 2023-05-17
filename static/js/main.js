const phraseText = document.getElementById("phrase-text");
const phraseLink = document.getElementById("phrase-link");
const logoLink = document.getElementById("logo-link");
const body = document.body;

function randomPastelColor() {
    const hue = Math.floor(Math.random() * 360);
    return `hsl(${hue}, 100%, 20%)`;
}

body.style.backgroundColor = randomPastelColor();

phraseLink.addEventListener("click", (event) => {
    event.preventDefault();
    window.location.href = event.target.getAttribute("href");
});

logoLink.addEventListener("click", (event) => {
    event.preventDefault();
    window.location.href = event.target.parentElement.getAttribute("href");
});
