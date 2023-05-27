'use strict';
/**
 * Controls the dynamic display of the
 * items ordered on the sidebar for the cart.
 */
const cartBtn = document.getElementById('btn-cart');
const checkoutBtn = document.getElementById('btn-checkout');
const clearBtn = document.getElementById('btn-clear');

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

  const h5 = document.createElement('h5');
  const title = document.createTextNode(data.title);
  h5.appendChild(title);

  const p1 = document.createElement('p');
  const quantity = document.createTextNode(`Quantity: ${data.quantity}`);
  p1.appendChild(quantity);

  const p2 = document.createElement('p');
  const priceVal = parseFloat(Number(data.quantity) * Number(data.price));
  const price = document.createTextNode(`Price: NGN. ${priceVal.toFixed(2)}`);
  p2.appendChild(price);
  divCardBody.append(h5, p1, p2);

  const deleteBtn = document.createElement('a');
  const logo = document.createElement('i');

  deleteBtn.classList.add('btn', 'btn-trash', 'btn-trash-right');
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

// When Clicked: Opens the cart body pane
cartBtn.addEventListener('click', () => {
  const cartBody = document.getElementById('cart-body');
  const cartItemStr = localStorage.getItem('cart-item');
  const cartItem = cartItemStr ? JSON.parse(cartItemStr) : [];

  if (cartItem.length > 0) {
    displayCartCards(cartItem, cartBody);
  } else {
    checkoutBtn.style.display = 'none';
  }
});

// When Clicked: Clears the localStorage of all the cart items
clearBtn.addEventListener('click', () => {
  if (localStorage.getItem('cart-item')) {
    localStorage.removeItem('cart-item');
    location.reload();
  }
});
