'use strict';

let stringCuaca = "";
const btnSubmit = document.querySelector(".btn-submit");

async function getJson() {
  return fetch("./get_data").then( res => res.json())
}

function addPanduan() {
  fetch("./create_data/", {
        method: "POST",
        body: new FormData(document.querySelector('.form-panduan'))
    }).then(callWeatherApi);
  return false;
}

btnSubmit.addEventListener("click", addPanduan);

async function callWeatherApi() {
  const inputKota = await getJson();
  const index = Object.keys(inputKota).length - 1;

  const kotaAsal = inputKota[index].fields.kota_asal;
  const kotaDestinasi = inputKota[index].fields.kota_destinasi;
  getCitiesData(kotaAsal, kotaDestinasi);
}

async function getCitiesData(kotaAsal, kotaDestinasi) {
  const cuacaAsal = await getWeather(kotaAsal);
  const cuacaDestinasi = await getWeather(kotaDestinasi);

  const dataCuacaAsal = await cuacaAsal.json();
  const dataCuacaDestinasi = await cuacaDestinasi.json();

  console.log(dataCuacaAsal);
  console.log(dataCuacaDestinasi);
  writeCityData(dataCuacaAsal);
  writeCityData(dataCuacaDestinasi);

  updateUI();
}

async function updateUI() {
  document.querySelector(".daftar-panduan").innerHTML = "";
  stringCuaca += `
    <div class="daftar-rekomendasi">
      <ul>
        <li>1 Lorem ipsum dolor sit amet, consectetur adipisicing elit. Officiis laboriosam quibusdam optio harum perspiciatis.</li>
        <li>2</li>
      </ul>
    </div>
  `;
  document.querySelector(".daftar-panduan").innerHTML = stringCuaca;
  stringCuaca = "";
}

// Weather App
async function getWeather(city) {
  const apiKey = "2bf8699a999ba51b8a89cb7600b39312";
  return fetch(
    "https://api.openweathermap.org/data/2.5/weather?q=" +
      city +
      "&units=metric&appid=" +
      apiKey
    );
}

function writeCityData(data) {
  const { name } = data;
  const { icon, description } = data.weather[0];
  const { temp, humidity } = data.main;
  const { speed } = data.wind;
  stringCuaca += `
    <div class="kota">
      <p>Weather in ${name}</p>
      <p>${temp}°C</p>
      <div>
        <img src="https://openweathermap.org/img/wn/${icon}.png" alt="weather-logo" class="icon" />
        <p class="description">${description}</p>
      </div>
      <div>
        <div class="humidity">Humidity: ${humidity}%</div>
        <div class="wind">Wind speed: ${speed} km/h</div>
      </div>
    </div>
  `;
}

function setPanduan(weatherStatus, description) {
  /*
  * Weathers conditions from OpenWeather API, https://openweathermap.org/weather-conditions
  * 01: clear sky
  * 02: few clouds
  * 03: scattered clouds
  * 04: broken clouds
  * 10: rain
  * 11: thunderstorm
  * 13: snow
  * 50: mist 
  */

  if (weatherStatus.slice(0,2) === "01") {
    
  } else if (weatherStatus.slice(0,1) === "0") {
    
  } else if (weatherStatus.slice(0,2) === "10") {

  } else if (weatherStatus.slice(0,1) === "1" || weatherStatus.slice(0,1) === "5") {

  }
}

// event button

// document.querySelector(".btn-submit").addEventListener("click", addPanduan);

const btnHero = document.querySelector(".btn-hero");
const descriptionSection = document.querySelector(".page-description");
// const btnSubmit = document.querySelector(".btn-submit");
const secPanduan = document.querySelector(".section-container");

btnHero.addEventListener("click", function(e) {
  descriptionSection.scrollIntoView({behavior:"smooth"})
})

// btnSubmit.addEventListener("click", function(e) {
//   secPanduan.scrollIntoView({behavior:"smooth"});
// })