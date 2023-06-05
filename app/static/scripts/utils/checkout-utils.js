'use strict';

export const postToCheckout = (data) => {
  fetch('/checkout/', {
    method: 'POST',
    body: JSON.stringify(data),
    headers: {
      'Content-type': 'application/json'
    }
  });
  localStorage.removeItem('cart-item');
};
