<script setup>
import  NavComponent from '@/components/NavComponent.vue'



</script>
<template>
     <div class="row d-flex justify-content-center">

             <div class="col-12 col-md-12 col-xxl-6 p-0 px-lg-5 d-flex justify-content-center z-3" id="nix-top">
                <NavComponent></NavComponent>
             </div>
            <div class="col-12 col-xl-6 py-5 my-5 px-sm-3 mx-md-3 px-lg-5 px-xl-5 d-flex justify-content-center">
              <router-view></router-view>
            </div>

  <nav class="navbar py-0 fixed-bottom col-12 d-flex justify-content-center" id="nav-fix">
      <div class="col-12 col-md-8 col-xl-6 col-xxl-4 d-flex justify-content-evenly pt-0  rounded-top-5" id="fix-foot">

          <router-link to="/">
            <p class="mb-0 py-2" >
              <img src="../../public/img/home-bold.png" class="" id="icons">
            </p>
          </router-link>

          <router-link to="/Search">
            <p class="mb-0 py-2" >
              <img src="../../public/img/lupa.png" class="" id="icons"> 
            </p>
          </router-link>

          <router-link to="/New">
            <p class="mb-0 py-2" >
              <img src="../../public/img/mas-bold.png" class="" id="icons"> 
            </p>
          </router-link>

          <router-link to="/Gym">
            <p class="mb-0 py-2" >
              <img src="../../public/img/objetivo-bold.png" class="" id="icons"> 
            </p>
          </router-link>

          <router-link to="/Tips">
            <p class="mb-0 py-2" >
              <img src="../../public/img/rayo-bold.png" class="" id="icons"> 
            </p>
          </router-link>

        </div>
    </nav>

        </div>
</template>
<style scoped>

::-webkit-scrollbar{
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

#nix-top{
  position: fixed;
}

#fix-foot{
    background: #E07F84;
}

#nav-fix{
  background: #ddd;
  border-top: .25em #ddd solid;
}

#icons{
    width: 2.5rem;
    height: auto;
}

</style>