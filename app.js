// Minimal Live Poller & Calculator Engine (Under 2 KB)
document.addEventListener("DOMContentLoaded", function () {
  // Mobile nav: auto-scroll active pill into view only when overflowing
  const navScroll = document.querySelector('.nav-scroll');
  const activePill = document.querySelector('.nav-pills a.active');
  if (navScroll && activePill && navScroll.scrollWidth > navScroll.clientWidth) {
    activePill.scrollIntoView({ inline: 'center', block: 'nearest' });
  }

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

// Club Chart & Arrow Formula Calculator
function calculateTeerFormula() {
  const frInput = document.getElementById("calc-fr");
  const srInput = document.getElementById("calc-sr");
  if (!frInput || !srInput) return;

  const fr = parseInt(frInput.value.trim(), 10);
  const sr = parseInt(srInput.value.trim(), 10);

  if (isNaN(fr) || isNaN(sr) || fr < 0 || fr > 99 || sr < 0 || sr > 99) {
    alert("Please enter valid two-digit numbers (00 to 99) for both rounds.");
    return;
  }

  // 1. Sum Formula (House Extraction)
  const sum = fr + sr;
  const sumDigits = String(sum).split('').map(Number);
  const houseTargets = Array.from(new Set(sumDigits));

  // 2. Difference & Variance Formula (Ending Extraction)
  const diff = Math.abs(fr - sr);
  const diffDigits = String(diff).split('').map(Number);
  const endingTargets = Array.from(new Set(diffDigits));

  // 3. Direct Combinations (House + Ending)
  const directPairs = [];
  for (let i = 0; i < houseTargets.length; i++) {
    for (let j = 0; j < endingTargets.length; j++) {
      directPairs.push(String(houseTargets[i]) + String(endingTargets[j]));
    }
  }

  // 4. Update UI
  const resBox = document.getElementById("calc-results");
  if (resBox) {
    document.getElementById("calc-houses").textContent = houseTargets.join(", ");
    document.getElementById("calc-endings").textContent = endingTargets.join(", ");
    document.getElementById("calc-direct").textContent = directPairs.join(", ");
    document.getElementById("calc-sum").textContent = `${fr} + ${sr} = ${sum}`;
    document.getElementById("calc-diff").textContent = `|${fr} - ${sr}| = ${diff}`;
    resBox.style.display = "block";
  }
}
