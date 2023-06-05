'use strict';

export const clear = (body, checkoutBtn) => {
  body.innerHTML = '';
  body.appendChild(checkoutBtn);
};

export const clearCart = () => {
  if (localStorage.getItem('cart-item')) {
    localStorage.removeItem('cart-item');
    return true;
  }
};

export const getCartItems = () => {
  const cartItemStr = localStorage.getItem('cart-item');
  return cartItemStr ? JSON.parse(cartItemStr) : [];
};

export const removeCartItem = (targetId, cartItem) => {
  // Searches for the cart of interest
  for (let i = 0; i < cartItem.length; i++) {
    if (cartItem[i].id === targetId) {
      // Remove the item at that index
      cartItem.splice(i, 1);
      break;
    }
  }
  // Update local storage
  localStorage.setItem('cart-item', JSON.stringify(cartItem));
};

export const addCartItem = (data) => {
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
  return true;
};
