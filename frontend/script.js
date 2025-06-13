// Year dropdown 
const yearSelect = document.getElementById("year");
const startYear = 2000;
const endYear = 2025;
for (let y = endYear; y >= startYear; y--) {
  const option = document.createElement("option");
  option.value = y;
  option.textContent = y;
  yearSelect.appendChild(option);
}

// Country selection
fetch("country-names.json")
  .then(response => response.json())
  .then(countries => {
    const datalist = document.getElementById("countries");

    countries.forEach(country => {
      const option = document.createElement("option");
      option.value = country;
      datalist.appendChild(option);
    });
  });

//Full map
const map = L.map('map', {maxBoundsViscosity: 1.0, maxBounds: [[-90, -180], [90, 180]]}).setView([20, 0], 2); // Centered globally

L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors & CartoDB',
  subdomains: 'abcd',
  maxZoom: 19
}).addTo(map);

//Map Zoom
document.getElementById("search").addEventListener("keyup", function (e) {
  if (e.key === "Enter") {
    const country = e.target.value.trim();
    if (country) {
      alert("Zooming to: " + country);
      // TODO: Integrate map zoom and prediction overlay
    }
  }
});

//Map Year
document.getElementById("year").addEventListener("change", function (e) {
  const year = e.target.value;
  console.log("Selected year:", year);
  // TODO: Update map data based on selected year
});
