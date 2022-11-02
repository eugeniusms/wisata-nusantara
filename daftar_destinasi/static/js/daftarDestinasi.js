$(document).ready(function () {
  // ================================ ALL ABOUT INITIATING DATA ================================
  var allData = null;
  var sukaAllData = null;
  var userLoggedIn = null;

  const allCategory = [
    "All",
    "Favorites",
    "Art&Culture",
    "Beach&Sea",
    "Caves",
    "Culinary",
    "Temples",
    "Forest",
    "Hills",
    "Historic",
    "Mountains",
    "Nature",
  ];
  // Saving Current State
  var searchKeyword = "";
  var kategoriAktif = "All";

  // Sidebar Elements
  const sidebarElements = [
    {
      name: "Home",
      id: "home-button",
      icon: "fa-solid fa-house",
      iconColor: "#CBD5E1",
      link: "/",
    },
    {
      name: "Events",
      id: "events-button",
      icon: "fa-solid fa-calendar-days",
      iconColor: "#CBD5E1",
      link: "/event/",
    },
    {
      name: "Journey",
      id: "journey-button",
      icon: "fa-solid fa-book",
      iconColor: "#CBD5E1",
      link: "/journey/",
    },
    {
      name: "Story",
      id: "story-button",
      icon: "fa-solid fa-comments",
      iconColor: "#CBD5E1",
      link: "/story/",
    },
    {
      name: "FAQ",
      id: "faq-button",
      icon: "fa-solid fa-question",
      iconColor: "#CBD5E1",
      link: "/faq/",
    },
    {
      name: "Wishlist",
      id: "wishlist-button",
      icon: "fa-solid fa-heart",
      iconColor: "#22C55E",
      link: "/destination/wishlist/",
    },
    {
      name: "Add Destination",
      id: "add-destination-button",
      icon: "fa-solid fa-plus",
      iconColor: "#22C55E",
      link: "/destination/add/",
    },
    {
      name: "Delete Destination",
      id: "delete-destination-button",
      icon: "fa-solid fa-trash",
      iconColor: "#BD4B4B",
      link: "/destination/delete/",
    },
  ];

  // Create Sidebar Element
  const sidebarElement = (element) => {
    if (element.name == "Wishlist" && userLoggedIn.length != 0) {
      return `
        <a href="/destination/wishlist/">
          <button class="text-slate-300 hover:text-bone" id=${element.id}>
            <div class="flex items-center py-1 mt-8">
              <i class="${element.icon}" style="font-size:14px;color:${element.iconColor};"></i>
              <p class="pl-2">${element.name}</p>
            </div>
          </button>
        </a>
      `;
    }
    if (element.name == "Wishlist" && userLoggedIn.length == 0) {
      return ``;
    }
    if (element.name == "Add Destination" && userLoggedIn.length == 0) {
      return ``;
    }
    if (
      element.name == "Delete Destination" &&
      userLoggedIn[0].fields.username != "eugenius.mario"
    ) {
      return ``;
    }

    if (
      element.id == "add-destination-button" ||
      element.id == "delete-destination-button"
    ) {
      return `
        <button class="text-slate-300 hover:text-bone" id=${element.id}>
          <div class="flex items-center py-1">
            <i class="${element.icon}" style="font-size:14px;color:${element.iconColor};"></i>
            <p class="pl-2">${element.name}</p>
          </div>
        </button>
      `;
    }
    return `
      <a href="${element.link}" class="text-slate-300 hover:text-bone">
        <div class="flex items-center py-1">
          <i class="${element.icon}" style="font-size:14px;color:${element.iconColor};"></i>
          <p class="pl-2">${element.name}</p>
        </div>
      </a>
    `;
  };

  // GET User Logged In
  $.ajax({
    url: "http://localhost:8000/auth/show-user-loggedin/json",
    type: "GET",
    success: function (data) {
      userLoggedIn = data;
      console.log(data);
      sidebarElements.map((element) => {
        $("#sidebar-destination").append(sidebarElement(element));
      });
      $("#hello-mobile").append(`<p>Hello, ${data[0].fields.username}!</p>`);
      $("#hello-tablet-desktop").append(
        `<p>Hello, ${data[0].fields.username}!</p>`
      );

      activateSidebarModal();
      activateDeleteDestinationButton();
    },
  });

  // ================================ END OF INITIATING DATA ===================================

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

  // GET All Destination Data
  $.ajax({
    url: "http://localhost:8000/destination/json",
    type: "GET",
    success: function (data) {
      console.log(data);
      allData = data;
      data.map((destinasi) => {
        $("#daftar-destinasi-mobile").append(destinationMobile(destinasi));
        $("#daftar-destinasi-tablet-desktop").append(
          destinationTabletDesktop(destinasi)
        );
        modalCard(destinasi);
      });
    },
  });

  // Search Destination (Mobile)
  $("#search-destination-mobile").keydown(function () {
    searchKeyword = $(this).val();
    showResult();
  });

  // Search Destination (Tablet & Desktop)
  $("#search-destination-tablet-desktop").keydown(function () {
    searchKeyword = $(this).val();
    showResult();
  });

  // ================================ END OF DESTINATION ================================

  // ================================ ALL ABOUT CATEGORY ================================
  allCategory.map((category) => {
    $("#kategori-mobile").append(`
      <div class="kategori" id=${category}>
        <button class="bg-black text-white text-[12px] rounded-3xl px-4 py-2 hover:bg-bone hover:drop-shadow-2xl hover:text-black focus:drop-shadow-2xl focus:bg-bone focus:text-black focus:font-bold transition duration-150 ease-in-out">${category}</button>
      </div>
    `);
    $("#kategori-tablet-desktop").append(`
      <div class="kategori" id=${category}>
        <button class="bg-black text-white text-[12px] rounded-3xl px-4 py-2 hover:bg-bone hover:drop-shadow-2xl hover:text-black hover:font-bold focus:drop-shadow-2xl focus:bg-bone focus:text-black focus:font-bold transition duration-150 ease-in-out">${category}</button>
      </div>
    `);
  });

  // IF CATEGORY CLICKED
  $(".kategori").click(function () {
    kategoriAktif = $(this).attr("id");
    $("#info-kategori-mobile").html(`
      Category : ${kategoriAktif}
    `);
    $("#info-kategori-tablet-desktop").html(`
      Category : ${kategoriAktif}
    `);
    showResult();
  });
  // ================================ END OF CATEGORY ===================================

  // ================================ RESULT SHOW =======================================
  const showResult = () => {
    const filteredData = allData
      .filter((destinasi) => {
        return kategoriAktif == "All"
          ? true
          : destinasi.fields.kategori
              .toLowerCase()
              .includes(kategoriAktif.toLowerCase());
      })
      .filter((destinasi) => {
        return searchKeyword == ""
          ? true
          : destinasi.fields.nama
              .toLowerCase()
              .includes(searchKeyword.toLowerCase());
      });

    $("#daftar-destinasi-mobile").html("");
    $("#daftar-destinasi-tablet-desktop").html("");

    filteredData.map((destinasi) => {
      $("#daftar-destinasi-mobile").append(destinationMobile(destinasi));
      $("#daftar-destinasi-tablet-desktop").append(
        destinationTabletDesktop(destinasi)
      );
      modalCard(destinasi);
    });

    // Jika kosong
    if (filteredData.length == 0) {
      $("#daftar-destinasi-not-found-tablet-desktop").html(`
        <div class="flex justify-center items-center">
          <p class="my-32 text-[48px] text-gray-700 font-montserrat font-bold">No destinations found :(</p>
        </div>
      `);
    } else {
      $("#daftar-destinasi-not-found-mobile").html("");
      $("#daftar-destinasi-not-found-tablet-desktop").html("");
    }
  };
  // ================================ END OF RESULT SHOW =================================

  // ================================ ALL ABOUT DESTINATION MODAL ========================
  const modalCard = (destinasi) => {
    // FOR MOBILE
    $(`#destinasi-card-mobile-${destinasi.pk}`).click(function () {
      // SUKA TOGGLE GRAY OR RED
      let sukaButton = `<i class="fa fa-duotone fa-heart animate-bounce" style="font-size:24px;color:#999999"></i>`; // GRAY
      let isLiked = false;
      let likeMessage = "Likes";

      for (like of sukaAllData) {
        if (
          like.fields.user == userLoggedIn[0].pk &&
          like.fields.destinasi == destinasi.pk
        ) {
          isLiked = true;
          break;
        }
      }
      if (isLiked) {
        sukaButton = `<i class="fa fa-solid fa-heart" style="font-size:24px;color:#BD4B4B"></i>`; // RED
        likeMessage = "Liked";
      }
      $(`#modalMobile`).html(`
        <div id="myModal" class="modal">
          <div class="modal-content-destination-mobile">
            <div class="bg-white rounded-3xl divide-y divide-slate-300">

              <div class="pt-5 px-6 pb-5 rounded-xl">
                <div class="flex justify-end">
                  <span class="text-3xl cursor-pointer hover:text-rose" id="close-modal">&times;</span>
                </div>
                <div class="flex justify-center">
                  <img src="${destinasi.fields.foto_cover_url}" class="h-44 rounded-3xl"/>
                </div>
                <div class="flex justify-center pt-4">
                  <div class="text-center">
                    <p class="font-bold text-[15px]">${destinasi.fields.nama}</p>
                    <p class="text-philippinesilver text-[12px]">${destinasi.fields.lokasi}</p>
                  </div>
                </div> 
              </div>

              <div class="bg-gradient-to-r from-slate-200 to-slate-100 divide-y divide-slate-300 rounded-b-3xl">
                <div>
                  <div class="flex justify-between px-6 pt-4 pb-4">
                    <div class="text-center">
                      <i class="fa fa-solid fa-sun" style="font-size:20px;color:#bdac4b"></i>
                      <p class="text-[10px] font-bold">${destinasi.fields.kategori}</p>
                      <p class="text-black text-[10px]">Category</p>
                    </div>
                    <div class="text-center">
                      <a href="/destination/suka/${destinasi.pk}">
                        ${sukaButton}
                      </a>
                      <p class="text-[11px] font-bold">${destinasi.fields.jumlah_suka}</p>
                      <p class="text-black text-[11px]">${likeMessage}</p>
                    </div>
                    <a href="${destinasi.fields.maps_url}" class="flex bg-white px-4 rounded-xl items-center border-black border-[1px] hover:bg-slate-300 hover:scale-105 transition duration-150 ease-in-out">
                      <div class="flex items-center text-center">
                        <i class="fa fa-duotone fa-map-location-dot" style="font-size:20px;color:#4bbd7a"></i>&nbsp;&nbsp;
                        <p class="text-[10px] font-bold">Open</p>
                        <p class="text-black/90 text-[10px]">Maps</p>
                      </div>
                    </a>
                  </div>
                </div>
                <p class="text-[10px] py-4 px-6">${destinasi.fields.deskripsi}</p>
              </div>

            </div>

          </div>
        </div>
      `);
      // Close the modal
      $("#close-modal").click(function () {
        $("#myModal").remove();
      });
    });

    // FOR TABLET & DESKTOP
    $(`#destinasi-card-tablet-desktop-${destinasi.pk}`).click(function () {
      // SUKA TOGGLE GRAY OR RED
      let sukaButton = `<i class="fa fa-duotone fa-heart animate-bounce" style="font-size:24px;color:#999999"></i>`; // GRAY
      let isLiked = false;
      let likeMessage = "Likes";

      for (like of sukaAllData) {
        if (
          like.fields.user == userLoggedIn[0].pk &&
          like.fields.destinasi == destinasi.pk
        ) {
          isLiked = true;
          break;
        }
      }
      if (isLiked) {
        sukaButton = `<i class="fa fa-solid fa-heart" style="font-size:24px;color:#BD4B4B"></i>`; // RED
        likeMessage = "Liked";
      }

      $(`#modalTabletDesktop`).html(`
        <div id="myModal" class="modal">
          <div class="modal-content-destination-tablet-desktop">
            <div class="bg-white rounded-3xl divide-y divide-slate-300">

              <div class="flex justify-between pt-5 px-6 pb-5 rounded-xl">
                <img src="${destinasi.fields.foto_cover_url}" class="h-44 rounded-3xl"/>
                <div class="flex items-center">
                  <div>
                    <p class="font-bold text-[16px]">${destinasi.fields.nama}</p>
                    <p class="text-philippinesilver text-[13px]">${destinasi.fields.lokasi}</p>
                  </div>
                </div> 
                <div class="flex items-start">
                  <span class="text-3xl cursor-pointer hover:text-rose" id="close-modal">&times;</span>
                </div>
              </div>

              <div class="bg-gradient-to-r from-slate-200 to-slate-100 divide-y divide-slate-300 rounded-b-3xl">
                <div>
                  <div class="flex gap-16 px-6 pt-4 pb-4">
                    <div class="text-center">
                      <i class="fa fa-solid fa-sun" style="font-size:24px;color:#bdac4b"></i>
                      <p class="text-[11px] font-bold">${destinasi.fields.kategori}</p>
                      <p class="text-black text-[11px]">Category</p>
                    </div>
                    <div class="text-center">
                      <a href="/destination/suka/${destinasi.pk}">
                        ${sukaButton}
                      </a>
                      <p class="text-[11px] font-bold">${destinasi.fields.jumlah_suka}</p>
                      <p class="text-black text-[11px]">${likeMessage}</p>
                    </div>
                    <a href="${destinasi.fields.maps_url}" class="flex bg-white px-4 rounded-xl items-center border-black border-[1px] hover:bg-slate-300 hover:scale-105 transition duration-150 ease-in-out">
                      <div class="flex items-center text-center">
                        <i class="fa fa-duotone fa-map-location-dot" style="font-size:24px;color:#4bbd7a"></i>&nbsp;&nbsp;
                        <p class="text-[11px] font-bold">Open</p>
                        <p class="text-black/90 text-[11px]">Maps</p>
                      </div>
                    </a>
                  </div>
                </div>
                <p class="text-[12px] py-4 px-6">${destinasi.fields.deskripsi}</p>
              </div>

            </div>

          </div>
        </div>
      `);
      // Close the modal
      $("#close-modal").click(function () {
        $("#myModal").remove();
      });
    });
  };

  // DELETE DESTINATION

  const activateDeleteDestinationButton = () => {
    $("#delete-destination-button").click(function () {
      const deleteButtons = document.querySelectorAll("#delete-card-button");
      // TOGGLE SHOW/HIDE
      for (button of deleteButtons) {
        if (button.style.display !== "none") {
          button.style.display = "none";
        } else {
          button.style.display = "block";
        }
      }

      const createdByMark = document.querySelectorAll("#destinasi-created-by");
      // TOGGLE SHOW/HIDE
      for (mark of createdByMark) {
        if (mark.style.display !== "none") {
          mark.style.display = "none";
        } else {
          mark.style.display = "block";
        }
      }
    });
  };

  // GET All Suka Destination Data
  $.ajax({
    url: "http://localhost:8000/destination/suka/json",
    type: "GET",
    success: function (data) {
      sukaAllData = data;
      console.log(sukaAllData);
    },
  });

  // [POST] ADD DESTINASI
  $("#tambah-destinasi").click(function () {
    // event.preventDefault();
    const formTerisi =
      $("#id_nama") &&
      $("#id_deskripsi") &&
      $("#id_lokasi") &&
      $("#id_kategori") &&
      $("#id_foto_thumbnail_url") &&
      $("#id_foto_cover_url") &&
      $("#id_maps_url");
    if (formTerisi) {
      $.post(
        (url = "/destination/add/"),
        (data = {
          nama: $("#id_nama").val(),
          deskripsi: $("#id_deskripsi").val(),
          kategori: $("#id_kategori").val(),
          lokasi: $("#id_lokasi").val(),
          foto_thumbnail_url: $("#id_foto_thumbnail_url").val(),
          foto_cover_url: $("#id_foto_cover_url").val(),
          maps_url: $("#id_maps_url").val(),
        }),
        function (res, status) {
          if (status == "success") {
            console.log(res);
          }
        }
      );
    }
  });
});
