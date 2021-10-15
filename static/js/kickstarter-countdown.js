// Countdown showing days left until the last 3 days of the campaign. Then, it
// shows hours instead.
function kickstarterCountdown(dateString) {
  const hour = 60 * 60 * 1000,
    day = hour * 24;

  const startDate = new Date("2021-10-15T12:00");
  const startTime = startDate.getTime();
  const timeOffsetUTC = startDate.getTimezoneOffset() * 60 * 1000;
  const startTimeUTC = startTime - timeOffsetUTC;

  // November 1st
  const endTime = Date.UTC(2021, 10, 1);

  const updateCountdown = () => {
    const now = new Date().getTime();
    const distance = endTime - now + timeOffsetUTC;
    const days = Math.floor(distance / day);
    const hours = Math.floor((distance % day) / hour);
    console.log(days, hours);

    const countdown = document.getElementById("kickstarter-countdown");
    if (now < startTimeUTC) {
      const hours = Math.floor((startTimeUTC - now) / hour);
      countdown.innerHTML = `Starting in ${hours} hours`;
    } else if (days >= 3) {
      countdown.innerText = `${days} days left`;
    } else {
      let hours = Math.floor((distance % (day * 3)) / hour);
      if (hours > 1) {
        countdown.innerText = `${hours} hours left`;
      } else {
        countdown.innerText = `${hours} hour left`;
      }
    }
    if (distance < 0) {
      const banner = document.getElementById("kickstarter-banner");
      banner.parentNode.removeChild(banner);
      clearInterval(intervalCallback);
    }
  };
  const intervalCallback = setInterval(updateCountdown, hour);
  updateCountdown();
}
