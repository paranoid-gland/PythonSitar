document.addEventListener('click', function(event) {
  const menu = document.getElementById("nav-links");
  const hamburger = document.querySelector('.hamburger');

  if (!menu.contains(event.target) && !hamburger.contains(event.target)) {
    menu.classList.remove("show");
  }
});
