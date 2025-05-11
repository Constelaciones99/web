<script>
</script>
<template>
     <div class="row w-100 py-2 px-lg-5 d-flex justify-content-between" id="nav-brand">
                     <div class="col-3">
                <div class="btn-group">
    <button type="button" class="btn bg-transparent border-0 ms-4 ms-xxl-0" id="dropdown_titulo">Stringify</button>
    <button type="button" class="btn z-3 ps-4 ms-3 text-white bg-transparent border-0 dropdown-toggle dropdown-toggle-split" data-bs-toggle="dropdown" aria-expanded="false" data-bs-reference="parent">
      <span class="visually-hidden">Toggle Dropdown</span>
    </button>
    <ul class="dropdown-menu" id="sub-menu">
      <li><a class="dropdown-item" href="#">Contact us</a></li>
      <li><a class="dropdown-item" href="#">Feedback</a></li>
      <li><hr class="dropdown-divider"></li>
      <li><a class="dropdown-item" href="#">About</a></li>
    </ul>
  </div>
            </div>

            <div class="col-6 d-flex justify-content-end pe-2">

                <router-link to="/Notify" >
                <p class="mt-1 mb-0">
                    <img src="../../public/img/campana-bold.png" id="notice">
                </p>
                </router-link>

                <router-link to="/Profile">
                    <p class="mt-1 mb-0 ms-3 me-2">
                    <img src="../../public/img/avatar.png" class="rounded-5" id="nick">
                </p>
                </router-link>

            </div>
     </div>

</template>
<style scoped>

::-webkit-scrollbar {
     display: none;
 }

 @font-face {
     font-family:logo;
     src: url(../../public/fuentes/ledbetter.woff);
 }

 @font-face {
     font-family: subtitulos;
     src: url(../../public/fuentes/Hungtrey_Beatmora.otf);
 }

 @font-face {
     font-family: narracion;
     src: url(../../public/fuentes/Avenis.otf);
 }

 #dropdown_titulo{
    font-family:logo;
    font-size: 1.6em;
    scale:2.3;
    color: #fff;
 }


#notice, #nick{
    width: 2.5rem;
    height: auto;
}

#nav-brand{
    background: #E07F84;
  border-bottom: .25em #ddd solid;
}

</style>