function goBack() {
    window.history.back();
}

document.querySelectorAll('.event').forEach(event => {
    event.addEventListener('mouseenter', function() {
        const imgSrc = this.getAttribute('data-img');
        const eventImage = document.getElementById('event-image');
        eventImage.innerHTML = `<img src="${imgSrc}" alt="Event Image">`;
        eventImage.style.display = 'block';
        eventImage.style.left = `${event.getBoundingClientRect().left}px`;
        eventImage.style.top = `${event.getBoundingClientRect().bottom + window.scrollY}px`;
    });

    event.addEventListener('mouseleave', function() {
        const eventImage = document.getElementById('event-image');
        eventImage.style.display = 'none';
    });
});

//this is for pricing
document.addEventListener("DOMContentLoaded", function () {
    const monthlyButton = document.getElementById("monthly-btn");
    const annualButton = document.getElementById("annual-btn");
    const prices = document.querySelectorAll(".price");

    monthlyButton.addEventListener("click", function () {
        monthlyButton.classList.add("active");
        annualButton.classList.remove("active");
        prices.forEach(price => {
            price.textContent = price.getAttribute("data-monthly");
        });
    });

    annualButton.addEventListener("click", function () {
        annualButton.classList.add("active");
        monthlyButton.classList.remove("active");
        prices.forEach(price => {
            price.textContent = price.getAttribute("data-annual");
        });
    });
});

// Initialize the carousel
$(document).ready(function() {
    $('#SimpleCarouselExample').carousel({
      interval: 5000, // change the interval to your needs
      pause: 'hover'
    });
  });

