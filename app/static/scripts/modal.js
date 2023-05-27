'use strict';
/**
 * modal.js
 *
 * Controls the transfer of data from the food card to the displayed
 * bootstrap modal
 */
const modalBtns = document.querySelectorAll('.modal-btn');
const closeBtn = document.querySelector('.btn-close');
const modal = document.getElementById('modal');
let quantity, data;

//Extract the 'Add To Cart' Button and add an event handler
const addBtn = modal.children[0].children[2].children[0];

addBtn.addEventListener('click', () => {
  data.quantity = quantity.value;
  const cartItemStr = localStorage.getItem('cart-item');
  let cartItem;
  // Checks if there is any existing cart-item list
  if (cartItemStr) {
    cartItem = JSON.parse(cartItemStr);
    cartItem.push(data);
  } else {
    cartItem = [data];
  }
  localStorage.setItem('cart-item', JSON.stringify(cartItem));
  location.reload(); // Refreshes the page
  // console.log(JSON.parse(cartItemStr));
});

// Function to automate the process of populating the modal
const populateModal = (modal, data) => {
  const header = modal.children[0].children[0];
  const body = modal.children[0].children[1];

  const img = header.children[0];
  const titleSpan = header.children[1].children[0];
  const priceSpan = header.children[1].children[1];
  const restaurantSpan = header.children[1].children[2];

  const descriptionDiv = body.children[0];
  const quantityField = body.children[1].children[1];

  // Setting all the elements
  img.setAttribute('src', data.src);
  titleSpan.innerHTML = `${data.title}`;
  priceSpan.innerHTML = `NGN. ${data.price}`;
  restaurantSpan.innerHTML = `From: ${data.restaurant}`;
  descriptionDiv.innerHTML = `${data.description}`;

  return quantityField;
};

modalBtns.forEach((btn) => {
  btn.addEventListener('click', () => {
    data = {
      id: btn.getAttribute('data-id'),
      src: btn.getAttribute('data-img-src'),
      title: btn.getAttribute('data-title'),
      price: btn.getAttribute('data-price'),
      restaurant: btn.getAttribute('data-restaurant'),
      description: btn.getAttribute('data-description')
    };

    quantity = populateModal(modal, data);
    modal.style.display = 'block';
  });
});

closeBtn.addEventListener('click', () => {
  const modalElement = closeBtn.parentElement.parentElement.parentElement;
  modalElement.style.display = 'none';
});
