const carousel = document.querySelector('.carousel'),
items = carousel.querySelectorAll('.item'),
arrows = document.querySelectorAll('.carousel-btns i');

const firstItem = items[0];
const lastItem = items[items.length - 1];

//Enabling scroll based movements.
let isDrag = false, prevPageX, prevScrollLeft,
itemWidth = firstItem.clientWidth + 20,
startPoint = 0,
endPoint = lastItem.getBoundingClientRect().left;

arrows.forEach(arrow => {
    arrow.addEventListener('click', (e) => {
        carousel.scrollLeft += arrow.id == 'left'? -itemWidth : itemWidth;
    });
});


const dragStart = (e) => {
    isDrag = true;
    prevPageX = e.pageX;
    prevScrollLeft = carousel.scrollLeft;
}

const dragStop = () => {
    isDrag = false;
}

const dragging = (e) => {
    if (!isDrag) return;
    e.preventDefault();
    let posDiff = e.pageX - prevPageX;
    carousel.scrollLeft = prevScrollLeft - posDiff;
}


carousel.addEventListener('mousemove', dragging);
carousel.addEventListener('mousedown', dragStart);
carousel.addEventListener('mouseup', dragStop);


// Determines when and which buttons to disable depending on whether the end of carousel
// has been reached.
setInterval(() => {
    arrows[0].classList.toggle('disabled', carousel.scrollLeft  == startPoint);
    arrows[1].classList.toggle('disabled', carousel.scrollLeft  + carousel.clientWidth >= endPoint);
}, 200);
