// Countdown showing days left until the last 3 days of the campaign. Then, it
// shows hours instead.
function kickstarterCountdown(dateString) {
  const hour = 60 * 60 * 1000,
    day = hour * 24;

  const startTime = new Date("2021-10-15T12:00").getTime();
  const endTime = new Date(dateString).getTime();
  const now = new Date().getTime();
  const updateCountdown = () => {
    const distance = endTime - now;
    const days = Math.floor(distance / day);

    const countdown = document.getElementById("kickstarter-countdown");
    if (now < startTime) {
      const hours = Math.floor((startTime - now) / hour);
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
