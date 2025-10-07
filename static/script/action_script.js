function togglePanel( selectedCard, triggerButton ) {

  // Get cardId from variable selectedCard
  const panel = document.getElementById(selectedCard);

  // Get triggerButtonId from varible named triggerButton
  const lever = document.getElementById(triggerButton);

  if (panel.style.maxHeight && panel.style.maxHeight !== '0px') {
    panel.style.maxHeight = '0px';
    lever.style.rotate = '0deg';
  } else {
    panel.style.maxHeight = panel.scrollHeight + 'px';
    lever.style.rotate = '180deg';
  }
}