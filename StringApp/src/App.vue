<script>
import axios from 'axios'
export default{
  data(){
    return{
      datos:[]
    }
  },methods:{
      async fetchDatabase(){
         axios.get('http://localhost:3100/api/datos').then(
          response=>{
            //this.datos=response.data

            response.data[0].forEach(x=>this.datos.push(x.fullname))
            //console.log(this.datos)
          }
          ).catch(error=>{
            console.log(error)
                })

    }

  },mounted(){

          this.fetchDatabase()
        }
}
</script>
<template>
     <div class="container-fluid" id="pagina-central">
        <div class="row d-flex justify-content-center">

             <div class="col-12 col-md-12 col-xxl-6 p-0 px-lg-5 d-flex justify-content-center z-3" id="nix-top">
                 <div class="row w-100 py-2 px-lg-5 d-flex justify-content-between" id="nav-brand">
                     <div class="col-3">
                <div class="btn-group">
    <button type="button" class="btn bg-transparent border-0 ms-4 ms-xxl-0" id="dropdown_titulo">Stringify</button>
    <button type="button" class="btn z-3 ps-4 ms-3 text-white bg-transparent border-0 dropdown-toggle dropdown-toggle-split" data-bs-toggle="dropdown" aria-expanded="false" data-bs-reference="parent">
      <span class="visually-hidden">Toggle Dropdown</span>
    </button>
    <ul class="dropdown-menu" id="sub-menu">
      <li v-for="dato in datos" :key="dato" ><a class="dropdown-item">{{ dato }}</a></li>
      <!-- <li><a class="dropdown-item" href="#">Contact us</a></li>
      <li><a class="dropdown-item" href="#">Feedback</a></li>
      <li><hr class="dropdown-divider"></li>
      <li><a class="dropdown-item" href="#">About</a></li> -->
    </ul>
  </div>
            </div>

            <div class="col-6 d-flex justify-content-end pe-2">

                <router-link to="/Notify" >
                <p class="mt-1 mb-0">
                    <img src="../public/img/campana-bold.png" id="notice">
                </p>
                </router-link>

                <router-link to="/Profile">
                    <p class="mt-1 mb-0 ms-3 me-2">
                    <img src="../public/img/avatar.png" class="rounded-5" id="nick">
                </p>
                </router-link>

            </div>
     </div>
             </div>
            <div class="col-12 col-xl-6 py-5 my-5 px-sm-3 mx-md-3 px-lg-5 px-xl-5 d-flex justify-content-center">
              <router-view></router-view>
            </div>

  <nav class="navbar py-0 fixed-bottom col-12 d-flex justify-content-center" id="nav-fix">
      <div class="col-12 col-md-8 col-xl-6 col-xxl-4 d-flex justify-content-evenly pt-0  rounded-top-5" id="fix-foot">

          <router-link to="/">
            <p class="mb-0 py-2" >
              <img src="../public/img/home-bold.png" class="" id="icons">
            </p>
          </router-link>

          <router-link to="/Search">
            <p class="mb-0 py-2" >
              <img src="../public/img/lupa.png" class="" id="icons"> 
            </p>
          </router-link>

          <router-link to="/New">
            <p class="mb-0 py-2" >
              <img src="../public/img/mas-bold.png" class="" id="icons"> 
            </p>
          </router-link>

          <router-link to="/Gym">
            <p class="mb-0 py-2" >
              <img src="../public/img/objetivo-bold.png" class="" id="icons"> 
            </p>
          </router-link>

          <router-link to="/Tips">
            <p class="mb-0 py-2" >
              <img src="../public/img/rayo-bold.png" class="" id="icons"> 
            </p>
          </router-link>

        </div>
    </nav>

        </div>
    </div>
</template>
<style scoped>

::-webkit-scrollbar{
     display: none;
 }

 @font-face {
     font-family:logo;
     src: url(../public/fuentes/ledbetter.woff);
 }

 @font-face {
     font-family: subtitulos;
     src: url(../public/fuentes/Hungtrey_Beatmora.otf);
 }

 @font-face {
     font-family: narracion;
     src: url(../public/fuentes/Avenis.otf);
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

 #pagina-central{
  background: #ddd;
 }
</style>
