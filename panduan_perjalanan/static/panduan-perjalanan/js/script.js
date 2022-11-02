"use strict";

let stringCuaca = "";

async function getJson() {
  return fetch("./get_data").then((res) => res.json());
}

function addPanduan() {
  fetch("./create_data/", {
    method: "POST",
    body: new FormData(document.querySelector(".form-panduan")),
  }).then(callWeatherApi);
  return false;
}

async function callWeatherApi() {
  const inputKota = await getJson();
  const index = Object.keys(inputKota).length - 1;
  console.log(index);

  const kotaAsal = inputKota[index].fields.kota_asal;
  const kotaDestinasi = inputKota[index].fields.kota_destinasi;
  getCitiesData(kotaAsal, kotaDestinasi);
}

async function getCitiesData(kotaAsal, kotaDestinasi) {
  const cuacaAsal = await getWeather(kotaAsal);
  const cuacaDestinasi = await getWeather(kotaDestinasi);
  if (cuacaAsal.ok && cuacaDestinasi.ok) {
    const dataCuacaAsal = await cuacaAsal.json();
    const dataCuacaDestinasi = await cuacaDestinasi.json();
    console.log(dataCuacaAsal);
    console.log(dataCuacaDestinasi);

    const kondisiKotaAsal = writeCityData(dataCuacaAsal);
    const kondisiKotaDestinasi = writeCityData(dataCuacaDestinasi);
    setPanduan(kondisiKotaAsal, kondisiKotaDestinasi);

    updateUI();
  } else {
    let error = "";
    if (!cuacaAsal.ok) {
      error = kotaAsal;
    } else {
      error = kotaDestinasi;
    }
    alert(`${error} not found`);
  }
}

async function updateUI() {
  document.querySelector(".daftar-panduan").innerHTML = "";
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
      <p class="subheading">Weather in ${name}</p>
      <p class="temp">${temp}°C</p>
      <div class="condition">
        <img src="https://openweathermap.org/img/wn/${icon}.png" alt="weather-logo" class="icon" />
        <p class="description">${description}</p>
      </div>
      <div class="other-condition">
        <div class="humidity">Humidity: ${humidity}%</div>
        <div class="wind">Wind speed: ${speed} km/h</div>
      </div>
    </div>
  `;
  return [icon, temp];
}

function setPanduan(cuacaAsal, cuacaDestinasi) {
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

  let penerbangan = "";
  let kondisiAsal = "";

  if (cuacaAsal[0].slice(0, 2) === "01") {
    penerbangan = "Cuaca yang bagus untuk berangkat";
  } else if (cuacaAsal[0].slice(0, 1) === "0") {
    penerbangan = "Cuaca berawan, tetapi tidak akan mengganggu perjalanan";
  } else {
    const status = cuacaAsal[0].slice(0, 2);
    if (status == 10) {
      kondisiAsal = "hujan";
    } else if (status == 11) {
      kondisiAsal = "badai";
    } else if (status == 13) {
      kondisiAsal = "bersalju";
    } else {
      kondisiAsal = "berkabut";
    }
    penerbangan = `Karena cuaca ${kondisiAsal}, kemungkinan jadwal penerbangan ditunda`;
  }

  let kondisiDestinasi = "";
  let suhuDestinasi = "";

  if (cuacaDestinasi[1] >= 27) {
    suhuDestinasi = `
    <li class="item-list">
      <img
        src="/static/panduan_perjalanan/svg/thermometer-outline.svg"
        class = "list-icon"
      />
      <span>Cuaca di kota destinasi cukup panas</span>
    </li>
    <li class="item-list">
      <img
        src="/static/panduan_perjalanan/svg/shirt-outline.svg"
        class = "list-icon"
      />
      <span>Pakai pakaian yang mudah menyerap keringat, seperti baju kaus</span>
    </li>
    <li class="item-list">
      <img
        src="/static/panduan_perjalanan/svg/water-outline.svg"
        class = "list-icon"
      />
      <span>Jangan lupa membawa wadah minum!</span>
    </li>
    <li class="item-list">
      <img
        src="/static/panduan_perjalanan/svg/umbrella-outline.svg"
        class = "list-icon"
      />
      <span>Membawa payung anti sinar UV atau topi</span>
    </li>
    `;
  } else {
    suhuDestinasi = `
    <li class="item-list">
      <img
        src="/static/panduan_perjalanan/svg/thermometer-outline.svg"
        class = "list-icon"
      />
      <span>Cuaca di kota destinasi cukup dingin</span>
    </li>
    <li class="item-list">
      <img
        src="/static/panduan_perjalanan/svg/shirt-outline.svg"
        class = "list-icon"
      />
      <span>Membawa jaket, sweater, atau baju lengan panjang</span>
    </li>
    `;
  }

  let kondisi = "";
  let iconKondisi = "";
  if (cuacaDestinasi[0].slice(0, 2) === "01") {
    kondisi = "Cuaca yang bagus untuk pergi wisata!";
    iconKondisi = "sunny";
  } else if (cuacaDestinasi[0].slice(0, 1) === "0") {
    kondisi = "Cuaca berawan, tetapi tidak akan mengganggu perjalanan!";
    iconKondisi = "cloudy";
  } else {
    const status = cuacaDestinasi[0].slice(0, 2);
    let deskripsiCuaca = "";
    if (status == 10) {
      deskripsiCuaca = "hujan";
      iconKondisi = "rainy";
    } else if (status == 11) {
      deskripsiCuaca = "badai";
      iconKondisi = "thunderstorm";
    } else if (status == 13) {
      deskripsiCuaca = "bersalju";
      iconKondisi = "snow";
    } else {
      deskripsiCuaca = "berkabut";
      iconKondisi = "wind";
    }
    kondisi = `Cuaca ${deskripsiCuaca} tunda jalan-jalan dahulu, mungkin di lain hari akan kembali cerah`;
  }

  kondisiDestinasi += `
    <li class="item-list">
      <img
        src="/static/panduan_perjalanan/svg/${iconKondisi}-outline.svg"
        class = "list-icon"
      />
      <span>${kondisi}</span>
    </li>
    `;

  stringCuaca += `
    <div class="daftar-rekomendasi">
      <ul class="list">
        <li class="item-list">
          <img
            src="/static/panduan_perjalanan/svg/airplane-outline.svg"
            class = "list-icon"
          />
          <span>${penerbangan}</span>
        </li>
        ${suhuDestinasi}
        ${kondisiDestinasi}
      </ul>
    </div>
  `;
}

// event button

const btnHero = document.querySelector(".btn-hero");
const btnSubmit = document.querySelector(".btn-submit");
const descriptionSection = document.querySelector(".page-description");
const sectionPanduan = document.querySelector(".daftar-panduan");

btnHero.addEventListener("click", function () {
  descriptionSection.scrollIntoView({ behavior: "smooth" });
});

btnSubmit.addEventListener("click", addPanduan);
btnSubmit.addEventListener("click", function (e) {
  e.preventDefault();
  sectionPanduan.classList.remove("hidden");
  sectionPanduan.scrollIntoView({ behavior: "smooth" });
});
