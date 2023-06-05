'use strict';

export const populateModal = (modal, data) => {
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
