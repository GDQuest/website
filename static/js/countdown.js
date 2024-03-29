// Countdown showing days left until the last 2 days. Then, it shows hours
// instead.
//
// Expects datetimes as input parameters.
function countdown(endDate) {
  const hour = 60 * 60 * 1000,
    minute = 60 * 1000,
    day = hour * 24;

  const endTime = endDate.getTime();
  const timeOffsetUTC = endDate.getTimezoneOffset() * 60 * 1000;
  const endTimeUTC = endTime - timeOffsetUTC;

  const updateCountdown = () => {
    const now = new Date().getTime();
    const distance = endTimeUTC - now + timeOffsetUTC;
    const days = Math.floor(distance / day);

    const countdown = document.getElementById("countdown");
    if (days >= 3) {
      countdown.innerText = `${days} days left`;
    } else {
      let hours = Math.floor((distance % (day * 3)) / hour).toString().padStart(2, "0");
      let minutes = Math.floor(distance % hour / minute).toString().padStart(2, "0");
      let seconds = Math.floor((distance % minute / 1000)).toString().padStart(2, "0");
      countdown.innerText = `${hours}:${minutes}:${seconds}`;
    }
    if (distance < 0) {
      const banner = document.getElementById("countdown-banner");
      banner.parentNode.removeChild(banner);
      clearInterval(intervalCallback);
    }
  };
  const intervalCallback = setInterval(updateCountdown, 1000);
  updateCountdown();
}
