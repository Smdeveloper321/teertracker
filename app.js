// Minimal Live Poller & Timing Helper (Under 1 KB)
document.addEventListener("DOMContentLoaded", function () {
  const now = new Date();
  const options = { weekday: 'short', year: 'numeric', month: 'short', day: 'numeric' };
  const dateEl = document.getElementById("live-date");
  if (dateEl && !dateEl.textContent.trim()) {
    dateEl.textContent = now.toLocaleDateString('en-US', options);
  }

  // Poll CDN API directly if user has page open between 3:25 PM and 4:45 PM IST
  const hours = now.getHours();
  const minutes = now.getMinutes();
  const isDrawWindow = (hours === 15 && minutes >= 25) || (hours === 16 && minutes <= 45);

  if (isDrawWindow) {
    setInterval(function () {
      fetch("https://cdn.shillongteerground.com/teer/api/results/latest/index.json", {
        headers: { "Referer": "https://shillongteerground.com/" }
      })
      .then(res => res.json())
      .then(data => {
        if (data.first_round && document.getElementById("shillong-fr")) {
          document.getElementById("shillong-fr").textContent = data.first_round;
        }
        if (data.second_round && document.getElementById("shillong-sr")) {
          document.getElementById("shillong-sr").textContent = data.second_round;
        }
      })
      .catch(() => {});
    }, 20000);
  }
});
