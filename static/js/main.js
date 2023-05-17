const phraseText = document.getElementById("phrase-text");
const phraseLink = document.getElementById("phrase-link");
const body = document.body;

function randomPastelColor() {
    const hue = Math.floor(Math.random() * 360);
    return `hsl(${hue}, 100%, 85%)`;
}

async function updatePhrase() {
    const response = await fetch("/random_phrase");
    const data = await response.json();
    phraseText.textContent = data.phrase;
    phraseLink.href = data.link;
    body.style.backgroundColor = randomPastelColor();
}

phraseLink.addEventListener("click", (event) => {
    event.preventDefault();
    updatePhrase();
});

updatePhrase();
