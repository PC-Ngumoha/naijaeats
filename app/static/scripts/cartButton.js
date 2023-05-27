'use strict';
/**
 * Contains the Javascript that controls the behaviour of the cart.
 */
const cartCount = document.getElementById('cart-count');

const updateCartButton = () => {
  const cartItemStr = localStorage.getItem('cart-item');
  const cartItem = cartItemStr ? JSON.parse(cartItemStr) : [];
  cartCount.textContent = `${cartItem.length}`;
};

setInterval(updateCartButton, 50);
