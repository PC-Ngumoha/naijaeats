'use strict';

export const displayCartCards = (dataList, body) => {
  let cards = [];
  let sumPrice = 0.0;
  dataList.forEach((data) => {
    const {divCard: card, totalPrice} = createCartCard(data);
    cards.push(card);
    sumPrice += totalPrice;
  });
  cards = cards.reverse();
  cards.forEach((card) => {
    body.prepend(card);
  });
  return sumPrice;
};

const createCartCard = (data) => {
  const divCard = document.createElement('div');
  const divRow = document.createElement('div');
  const divCol1 = document.createElement('div');
  const divCol2 = document.createElement('div');
  const divCardBody = document.createElement('div');
  let totalPrice = 0.0;

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
  return {divCard, totalPrice};
};
