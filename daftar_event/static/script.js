// $("#submit-btn").click(function(){
//   $.post("/daftar-event/tambah-event/", {nama:$("#nama").val(), lokasi:$("#lokasi").val(), jenis:$("#jenis").val(), deskripsi:$("#deskripsi").val()}, function(data){
//     $(".container").append(`<div class="bg-white rounded-2xl p-8 shadow-xl flex flex-col gap-2 max-w-[300px]">
//     <a href="#">
//       <img class="rounded-t-lg" src="https://thumbs.dreamstime.com/b/pink-cosmos-flowe-flowerbackground-112007426.jpg" alt="" />
//   </a>
//     <p class="text-center text-xl font-semibold">${data.nama}</p>
//     <p class="text-center text-xs">${data.lokasi}</p>
//     <a href="/daftar-event/event/${data.pk}" class="inline-flex items-center py-2 px-3 text-sm font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
//       Read more
//       <svg aria-hidden="true" class="ml-2 -mr-1 w-4 h-4" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
//   </a>
//   </div>`)
// })
// })