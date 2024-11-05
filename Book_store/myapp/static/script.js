document.addEventListener('DOMContentLoaded', () => {
    const monthlyBtn = document.getElementById('monthly-btn');
    const annualBtn = document.getElementById('annual-btn');
    const toggleSlider = document.getElementById('toggle-slider');

    monthlyBtn.addEventListener('click', () => {
        toggleSlider.style.transform = 'translateX(0)'; // Move to the left
        monthlyBtn.classList.add('active'); // Set Monthly as active
        annualBtn.classList.remove('active'); // Remove active from Annual
    });

    annualBtn.addEventListener('click', () => {
        toggleSlider.style.transform = 'translateX(100%)'; // Move to the right
        annualBtn.classList.add('active'); // Set Annual as active
        monthlyBtn.classList.remove('active'); // Remove active from Monthly
    });
});

