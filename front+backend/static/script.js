// Generate year dropdown (2000–2025)
const yearSelect = document.getElementById("year");
const startYear = 2000;
const endYear = 2025;
for (let y = endYear; y >= startYear; y--) {
  const option = document.createElement("option");
  option.value = y;
  option.textContent = y;
  yearSelect.appendChild(option);
}

// Load country list from static JSON (通过隐藏 input 获取路径)
const jsonUrl = document.getElementById("jsonPath").value;

fetch(jsonUrl)
  .then(response => response.json())
  .then(countries => {
    const datalist = document.getElementById("countries");
    countries.forEach(country => {
      const option = document.createElement("option");
      option.value = country;
      datalist.appendChild(option);
    });
  });

// Initialize Leaflet map
const map = L.map('map', {
  maxBoundsViscosity: 1.0,
  maxBounds: [[-90, -180], [90, 180]]
}).setView([20, 0], 2);

L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors & CartoDB',
  subdomains: 'abcd',
  maxZoom: 19
}).addTo(map);

// Send prediction request when Enter key is pressed
document.getElementById("search").addEventListener("keyup", function (e) {
  if (e.key === "Enter") {
    const country = e.target.value.trim();
    const year = document.getElementById("year").value;

    if (country && year) {
      fetch("/predict/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          country: country,
          year: year
        })
      })
      .then(res => res.json())
      .then(data => {
        if (data.error) {
          alert("Backend error: " + data.error);
        } else {
          alert(
            `Prediction Result:\n` +
            `Country: ${data.country}\n` +
            `Year: ${data.year}\n` +
            `Outbreak: ${data.outbreak ? "Yes" : "No"}\n` +
            `Confidence: ${data.confidence}`
          );
        }
      })
      .catch(err => {
        console.error("Request failed:", err);
        alert("Request failed. Check the browser console for details.");
      });
    }
  }
});

// Optional: react to year change (尚未使用)
document.getElementById("year").addEventListener("change", function (e) {
  const year = e.target.value;
  console.log("Selected year:", year);
});
