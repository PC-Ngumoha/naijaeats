const carousels = document.querySelectorAll('.carousel');
// independent functionality for each carousel

//Enables mouse scrolling to work on each carousel.
carousels.forEach(carousel => {
    let isDrag, prevPageX, prevScrollLeft;
    
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
});


// Enable arrow buttons to work on each carousel.
carousels.forEach(carousel => {
    const categoryId = carousel.getAttribute('data-category-id');
    const items = carousel.querySelectorAll('.item');
    const arrows = document.querySelectorAll(`.arrow-${categoryId}`);
    const itemWidth = items[0].clientWidth + 20;
    const startPoint = 0;
    const endPoint = items[items.length - 1].getBoundingClientRect().left;

    arrows.forEach(arrow => {
        arrow.addEventListener('click', () => {
            carousel.scrollLeft += arrow.id == 'left'? -itemWidth : itemWidth;
        });
    });

    //Monitor the carousel position and disable arrow buttons accordingly
    setInterval(() => {
        arrows[0].classList.toggle('disabled', carousel.scrollLeft  == startPoint);
        arrows[1].classList.toggle('disabled', carousel.scrollLeft  + carousel.clientWidth >= endPoint);
    }, 50);
});
