'use strict';
/**
 * Controls the dynamic display of the
 * items ordered on the sidebar for the cart.
 */
const cartBody = document.getElementById('cart-body');
const cartBtn = document.getElementById('btn-cart');
const checkoutBtn = document.getElementById('btn-checkout');
const checkoutForm = document.getElementById('checkout-form');
const clearBtn = document.getElementById('btn-clear');
let totalPrice = 0.0;

// Dynamically create a single cart card
const createCartCard = (data) => {
  const divCard = document.createElement('div');
  const divRow = document.createElement('div');
  const divCol1 = document.createElement('div');
  const divCol2 = document.createElement('div');
  const divCardBody = document.createElement('div');

  divCard.classList.add('card', 'mt-5', 'mb-5', 'cart-item');
  divRow.classList.add('row', 'g-0');
  divCol1.classList.add('col-4');
  divCol2.classList.add('col-8');

  const img = document.createElement('img');
  img.setAttribute('src', data.src);
  img.setAttribute('alt', '...');
  img.classList.add('img-fluid', 'rounded-start');
  divCol1.appendChild(img);

  const p1 = document.createElement('p');
  p1.classList.add('cart-details');
  const title = document.createTextNode(data.title);
  p1.appendChild(title);
  const p2 = document.createElement('p');
  p2.classList.add('cart-details');
  const quantity = document.createTextNode(`Quantity: ${data.quantity}`);
  p2.appendChild(quantity);

  const p3 = document.createElement('p');
  p3.classList.add('cart-details');
  const priceVal = parseFloat(Number(data.quantity) * Number(data.price));
  totalPrice += priceVal;
  const price = document.createTextNode(`Price: NGN. ${priceVal.toFixed(2)}`);
  p3.appendChild(price);
  divCardBody.append(p1, p2, p3);

  const deleteBtn = document.createElement('a');
  const logo = document.createElement('i');

  deleteBtn.classList.add('btn', 'btn-trash', 'btn-trash-right');
  logo.setAttribute('data-item-id', data.id);
  logo.classList.add('fa-solid', 'fa-trash-can');
  deleteBtn.appendChild(logo);

  divCol2.append(divCardBody, deleteBtn);

  divRow.append(divCol1, divCol2);
  divCard.appendChild(divRow);
  return divCard;
};

// Displays each created card
const displayCartCards = (dataList, body) => {
  let cards = [];
  dataList.forEach((data) => {
    const card = createCartCard(data);
    cards.push(card);
  });
  cards = cards.reverse();
  cards.forEach((card) => {
    body.prepend(card);
  });
};

const clear = (body) => {
  body.innerHTML = '';
  body.appendChild(checkoutBtn);
};

// When Clicked: Opens the cart body pane
cartBtn.addEventListener('click', () => {
  const cartItemStr = localStorage.getItem('cart-item');
  const cartItem = cartItemStr ? JSON.parse(cartItemStr) : [];

  if (cartItem.length > 0) {
    clear(cartBody);
    displayCartCards(cartItem, cartBody);
  } else {
    checkoutBtn.style.display = 'none';
  }
});

// Tries to determine if any of the cart delete buttons have
// been clicked
cartBody.addEventListener('click', (event) => {
  if (event.target.matches('.fa-trash-can')) {
    const deleteBtn = event.target;
    const targetId = deleteBtn.getAttribute('data-item-id');
    const cartItemStr = localStorage.getItem('cart-item');
    const cartItem = cartItemStr ? JSON.parse(cartItemStr) : [];
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
    location.reload(); // Reload page
  }
  // console.log(event.target);
});

// When Clicked: Clears the localStorage of all the cart items
clearBtn.addEventListener('click', () => {
  if (localStorage.getItem('cart-item')) {
    localStorage.removeItem('cart-item');
    location.reload();
  }
});

checkoutBtn.addEventListener('click', () => {
  const customer_id = checkoutBtn.getAttribute('data-customer');
  const cartItemStr = localStorage.getItem('cart-item');
  const cartItem = JSON.parse(cartItemStr);
  const data = {
    customerId: customer_id,
    orderCharge: totalPrice,
    menu_items: []
  };

  data.menu_items = cartItem.map((item) => ({
    id: item.id,
    quantity: item.quantity
  }));

  fetch('/checkout/', {
    method: 'POST',
    body: JSON.stringify(data),
    headers: {
      'Content-type': 'application/json'
    }
  });
  localStorage.removeItem('cart-item');
  // Waits a bit, then redirect to the checkout page.
  setTimeout(() => {
    location.href = '/checkout';
  }, 10);
});

// checkoutForm.addEventListener('submit', () => {
//   console.log('Submitted');
// });

// checkoutBtn.addEventListener('click', () => {
//   console.log('submitted');
// });
