'use strict';
/**
 * Contains the Javascript that controls the behaviour of the cart.
 */
import {getCartItems} from './utils/cart-utils.js';
const cartCount = document.getElementById('cart-count');

const updateCartButton = () => {
  const cartItem = getCartItems();
  cartCount.textContent = `${cartItem.length}`;
};

setInterval(updateCartButton, 50);
