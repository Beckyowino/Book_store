function goBack() {
    //window.history.back();
    window.location.href = "flowers.html";
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