'use strict';
/**
 * Controls the dynamic display of the
 * items ordered on the sidebar for the cart.
 */
import {
  clear,
  clearCart,
  getCartItems,
  removeCartItem
} from './utils/cart-utils.js';

import {displayCartCards} from './utils/cart-cards.js';
import {postToCheckout} from './utils/checkout-utils.js';

const cartBody = document.getElementById('cart-body');
const cartBtn = document.getElementById('btn-cart');
const checkoutBtn = document.getElementById('btn-checkout');
const clearBtn = document.getElementById('btn-clear');
let totalPrice = 0.0;

// When Clicked: Opens the cart body pane
cartBtn.addEventListener('click', () => {
  const cartItem = getCartItems();

  if (cartItem.length > 0) {
    clear(cartBody, checkoutBtn);
    totalPrice = displayCartCards(cartItem, cartBody);
  } else {
    checkoutBtn.style.display = 'none';
  }
});

// Deletes selected cart card
cartBody.addEventListener('click', (event) => {
  if (event.target.matches('.fa-trash-can')) {
    const deleteBtn = event.target;
    const targetId = deleteBtn.getAttribute('data-item-id');
    const cartItem = getCartItems();
    removeCartItem(targetId, cartItem);
    location.reload();
  }
});

// Clears all cart cards when clicked
clearBtn.addEventListener('click', () => {
  if (clearCart()) {
    location.reload();
  }
});

// Proceeds to checkout when clicked
checkoutBtn.addEventListener('click', () => {
  const cartItem = getCartItems();
  const data = {
    orderCharge: totalPrice,
    menu_items: []
  };

  data.menu_items = cartItem.map((item) => ({
    id: item.id,
    quantity: item.quantity
  }));
  postToCheckout(data);
  setTimeout(() => {
    location.href = '/checkout';
  }, 10);
});
