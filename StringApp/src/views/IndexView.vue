<script setup>
//import FooterComponent from '@/components/FooterComponent.vue';
import NavComponent from '@/components/NavComponent.vue';


</script>
<template>
     <div class="col-12 col-sm-12 col-md-12 col-lg-12 col-xl-12 col-xxl-9 ms-xxl-5">
    <div class="row">
            <div class="col-12" id="nav-fix">
                <NavComponent></NavComponent>
            </div>
            <main class="col-12">
                    <router-view></router-view>
            </main>

    <nav class="navbar py-0 fixed-bottom col-12 d-flex justify-content-center bg-white" id="nav-fix">

        <div class="col-12 col-md-8 col-xl-6 col-xxl-4 d-flex justify-content-evenly pt-0  rounded-top-5" id="fix-foot">
                         <router-link to="/buscar">
                            <p class="mb-0 py-2" >
                            <img src="../../public/img/home.png" class="" id="icons"> 
                         </p>
                         </router-link>
                         <p class="mb-0 py-2" >
                            <img src="../../public/img/lupa.png" class="" id="icons"> 
                         </p>
                         <p class="mb-0 py-2" >
                            <img src="../../public/img/mas.png" class="" id="icons"> 
                         </p>
                         <p class="mb-0 py-2" >
                            <img src="../../public/img/objetivo.png" class="" id="icons"> 
                         </p>
                         <p class="mb-0 py-2" >
                            <img src="../../public/img/rayo.png" class="" id="icons"> 
                         </p>
        </div>

    </nav>
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


#fix-foot{
    background: #E07F84;
}

#icons{
    width: 2.5rem;
    height: auto;
}



</style>