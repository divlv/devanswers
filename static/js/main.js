document.addEventListener("DOMContentLoaded", function () {
    setRandomBackgroundColor();
    handlePhraseClick();
});

function randomPastelColor() {
    const hue = Math.floor(Math.random() * 360);
    return `hsl(${hue}, 100%, 20%)`;
}

function setRandomBackgroundColor() {
    document.body.style.backgroundColor = randomPastelColor();
}

function handlePhraseClick() {
    const phraseText = document.getElementById("phrase-text");
    const phraseLink = document.getElementById("phrase-link");

    phraseText.addEventListener("click", function (event) {
        event.preventDefault();
        window.location.href = phraseLink.href;
    });
}
