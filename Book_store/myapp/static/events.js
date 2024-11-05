document.addEventListener('DOMContentLoaded', () => {
  const calendar = document.getElementById('calendar');
  const monthEl = document.getElementById('month');
  const months = [
    'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 
    'September', 'October', 'November', 'December'
  ];
  const days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];

  const STORYBLOK_URL = 'https://api-us.storyblok.com/v2/cdn/stories?starts_with=events&token=<zrWjkpOJ8544QXarJsxvTAtt>';
  let events = {};
  const today = new Date();
  let currentMonth = today.getMonth();
  let currentYear = today.getFullYear();

  const loadEvents = async () => {
    const res = await fetch(STORYBLOK_URL);
    const { stories } = await res.json();
    events = stories.reduce((accumulator, event) => {
      const eventDate = new Date(event.content.time).toISOString().split('T')[0];
      accumulator[eventDate] = event.content;
      return accumulator;
    }, {});
    updateCalendar(currentMonth, currentYear);
  };

  const drawBlankCalendar = () => {
    for (let i = 0; i < 42; i++) {  // Ensure 6 rows (42 days)
      const day = document.createElement('div');
      day.classList.add('day');

      const dayNumber = document.createElement('p');
      dayNumber.classList.add('day-number');
      const eventName = document.createElement('small');
      eventName.classList.add('event-name');

      day.appendChild(dayNumber);
      day.appendChild(eventName);
      calendar.appendChild(day);
    }
  };

  const updateCalendar = (month, year) => {
    const dayElements = document.querySelectorAll('.day');
    const firstDay = new Date(year, month, 1).getDay();
    const daysInMonth = new Date(year, month + 1, 0).getDate();

    monthEl.innerText = `${months[month]} ${year}`;
    let dayCounter = 1;
    dayElements.forEach((day, i) => {
      const dayNumber = day.querySelector('.day-number');
      const eventName = day.querySelector('.event-name');
      
      if (i >= firstDay && dayCounter <= daysInMonth) {
        const thisDate = new Date(year, month, dayCounter).toISOString().split('T')[0];
        
        dayNumber.innerText = dayCounter;
        if (events[thisDate]) {
          eventName.innerText = `* ${events[thisDate].title}`;
        } else {
          eventName.innerText = '';
        }
        dayCounter++;
      } else {
        dayNumber.innerText = '';
        eventName.innerText = '';
      }
    });
  };

  const previousMonth = () => {
    if (currentMonth === 0) {
      currentMonth = 11;
      currentYear--;
    } else {
      currentMonth--;
    }
    updateCalendar(currentMonth, currentYear);
  };

  const nextMonth = () => {
    if (currentMonth === 11) {
      currentMonth = 0;
      currentYear++;
    } else {
      currentMonth++;
    }
    updateCalendar(currentMonth, currentYear);
  };

  document.getElementById('openModalButton').addEventListener('click', openModal);
  document.getElementById('closeModalButton').addEventListener('click', closeModal);
  document.getElementById('overlay').addEventListener('click', closeModal);

  drawBlankCalendar();
  loadEvents();
});
