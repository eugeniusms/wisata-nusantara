$(document).ready(function () {
  var allData = null;
  var userLoggedIn = null;
  var allSukaData = null;

  // GET User Logged In
  $.ajax({
    url: "/auth/show-user-loggedin/json",
    type: "GET",
    success: function (data) {
      userLoggedIn = data;

      $("#hello-mobile").append(`<p>Hello, ${data[0].fields.username}!</p>`);
      $("#hello-tablet-desktop").append(
        `<p>Hello, ${data[0].fields.username}!</p>`
      );

      getAllDestinationData();
    },
  });

  // GET All Destination Data
  const getAllDestinationData = () => {
    $.ajax({
      url: "/destination/json",
      type: "GET",
      success: function (data) {
        allData = data;
        getAllSukaData();
      },
    });
  };

  // GET All Suka Destination Data
  const getAllSukaData = () => {
    $.ajax({
      url: "/destination/suka/json",
      type: "GET",
      success: function (data) {
        allSukaData = data;

        var allSukaDataIdDestination = [];
        allSukaData.map((suka) => {
          if (suka.fields.user == userLoggedIn[0].pk) {
            allSukaDataIdDestination.push(suka.fields.destinasi);
          }
        });

        const filteredData = allData.filter((destination) => {
          return allSukaDataIdDestination.includes(destination.pk);
        });

        filteredData.map((destinasi) => {
          $("#daftar-destinasi-mobile").append(destinationMobile(destinasi));
          $("#daftar-destinasi-tablet-desktop").append(
            destinationTabletDesktop(destinasi)
          );
        });
      },
    });
  };

  // ================================ ALL ABOUT DESTINATION ====================================
  // Destination Card : Mobile
  const destinationMobile = (destinasi) => {
    return `
      <div id="destinasi-card-mobile-${destinasi.pk}">
        <div class="p-4 hover:scale-105 transition duration-150 ease-in-out">
          <div class="bg-local rounded-3xl w-[200px] shadow-2xl" id="card" style="background-image:url(${destinasi.fields.foto_thumbnail_url});background-size:250px;">
            <div class="h-[210px]"></div>
            <div class="flex justify-between bg-white gap-3 items-center rounded-xl p-4 m-2 w-[185px]">
              <div>
                <p class="font-bold text-[11px]">${destinasi.fields.nama}</p>
                <p class="text-philippinesilver text-[9px]">${destinasi.fields.lokasi}</p>
              </div> 
              <div class="text-center">
                <i class="fa fa-duotone fa-heart" style="font-size:24px;color:#BD4B4B"></i>
                <p class="text-[9px]">${destinasi.fields.jumlah_suka}</p>
              </div>
            </div>
            <div class="h-[1px]"></div>
          </div>
        </div>
      </div>
    `;
  };
  // Destination Card : Tablet & Desktop
  const destinationTabletDesktop = (destinasi) => {
    return `
      <div id="destinasi-card-tablet-desktop-${destinasi.pk}" class="destinasi-card">
        <div class="p-4 hover:scale-105 transition duration-150 ease-in-out">
          <div class="bg-local rounded-3xl w-[200px] shadow-2xl relative" id="card" style="background-image:url(${destinasi.fields.foto_thumbnail_url});background-size:250px;">
            <a href="/destination/delete/${destinasi.pk}" id="delete-card-button" class="hidden">
              <div class="absolute top-0 right-0">
                <i class="bg-white rounded-full p-4 m-2 fa fa-solid fa-trash text-rose z-49 hover:scale-110 hover:bg-rose hover:text-white transition duration-150 ease-in-out"></i>
              </div>
            </a>
            <div class="h-[210px]"></div>
            <div class="flex justify-between bg-white gap-3 items-center rounded-xl p-4 m-2 w-[185px]">
              <div>
                <p class="font-bold text-[11px]">${destinasi.fields.nama}</p>
                <p class="text-philippinesilver text-[9px]">${destinasi.fields.lokasi}</p>
              </div> 
              <div class="text-center">
                <i class="fa fa-duotone fa-heart" style="font-size:24px;color:#BD4B4B"></i>
                <p class="text-[9px]">${destinasi.fields.jumlah_suka}</p>
              </div>
            </div>
            <div class="h-[1px]"></div>
          </div>
        </div>
      </div>
    `;
  };
});
