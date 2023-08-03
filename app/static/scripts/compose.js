'use strict';
/**
 * Contains the code that influences the behaviour of the compose page.
 */
const textarea = document.getElementById('description-box');

textarea.addEventListener('input', (event) => {
  const currentHeight = textarea.clientHeight;
  const scrollHeight = textarea.scrollHeight;

  if (scrollHeight > currentHeight) {
    textarea.style.height = `${scrollHeight}px`;
  }
  // textarea.style.height = `${scrollHeight}px`;
});