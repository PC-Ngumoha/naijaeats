'use strict';
/**
 * modal.js
 *
 * Controls the transfer of data from the food card to the displayed
 * bootstrap modal
 */
import {addCartItem} from './utils/cart-utils.js';
import {populateModal} from './utils/populate-modal.js';

const modalBtns = document.querySelectorAll('.modal-btn');
const closeBtn = document.querySelector('.btn-close');
const modal = document.getElementById('modal');
let quantity, data;

//Extract the 'Add To Cart' Button and add an event handler
const addBtn = modal.children[0].children[2].children[0];

addBtn.addEventListener('click', () => {
  data.quantity = quantity.value;
  if (addCartItem(data)) {
    location.reload();
  }
});

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
