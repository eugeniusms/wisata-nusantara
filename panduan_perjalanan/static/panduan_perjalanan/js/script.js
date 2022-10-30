'use strict';

async function getJson() {
  return fetch("./get_data").then( res => res.json())
}

async function updateUI() {
  document.querySelector(".daftar-panduan").innerHTML = "";
  const panduan = await getJson();
  // belum selesai
  let htmlString = ``;
  panduan.forEach(item => {
    htmlString += `
    <div>
      <div>${item.fields.kota_asal}</div>
      <div>${item.fields.kota_destinasi}</div>
    <div/>
    `
  });

  // document.querySelector(".daftar-panduan").insertAdjacentHTML("afterbegin", htmlString);
}

function addPanduan() {
  fetch("./create_data/", {
        method: "POST",
        body: new FormData(document.querySelector('#form-panduan'))
    }).then(updateUI);
  return false;
}

document.querySelector(".btn-submit").addEventListener("click", addPanduan);

const btnHero = document.querySelector(".btn-hero");
const secForm = document.querySelector(".form-section");
const formPanduan = document.querySelector("#form-panduan");
const btnSubmit = document.querySelector(".btn-submit");
const secPanduan = document.querySelector(".section-container");

btnHero.addEventListener("click", function(e) {
  secForm.scrollIntoView({behavior:"smooth"})
})

btnSubmit.addEventListener("click", function(e) {
  secPanduan.scrollIntoView({behavior:"smooth"});
})

// Weather App
const apiKey = "2bf8699a999ba51b8a89cb7600b39312";

function getWeather(city) {
  fetch(
    "https://api.openweathermap.org/data/2.5/weather?q=" +
      city +
      "&units=metric&appid=" +
      apiKey
    )
  .then((response) => {
    if (!response.ok) {
      alert("No weather found.");
      throw new Error("No weather found.");
    }
    return response.json();
  })
  .then((data) => displayWeather(data));  
}

function displayWeather(data) {
  const { name } = data;
  const { icon, description } = data.weather[0];
  const { temp, humidity } = data.main;
  const { speed } = data.wind;
  console.log(name, icon, description, temp, humidity, speed);
}

getWeather("Jakarta");

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
