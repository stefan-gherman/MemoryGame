
sessionStorage.currentClicks = 0;
let cardRows = document.querySelector('.row ');

let currentCards = cardRows.childElementCount;

cardRows = document.querySelectorAll('.row ');
console.log(currentCards)
for(let card of cardRows) {
    card.addEventListener('click', function(event) {
        let pressed = event.target;
        alert(pressed);
    })
}