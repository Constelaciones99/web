<template>

    <div class="col-12 px-5 bg-white rounded-4 shadow mt-5" id="very-card">
        <div class="row">

            <div class="col-12 card border-0" style="width: 19em;">
                <img src="img/buscar.png" class="card-img-top">
                <div class="card-body" id="description">
                    <h5 class="card-title" id="title">Cuenta Privada</h5>
                    <hr>
                    <form action="#">

                        <div class="input-group has-validation">
                            <span class="input-group-text" id="validationTooltipUsernamePrepend">🔑</span>
                            <input type="password" class="form-control" id="validationTooltipUsername"
                                aria-describedby="validationTooltipUsernamePrepend" placeholder="Nombre de Usuario"
                                required>

                            <span class="">*Solo necesitas un nombre original en cuenta privada 👀 </span>
                            <div class="invalid-tooltip">
                                Please choose a unique and valid username.
                            </div>
                        </div>

                        <br>
                <router-link to="/Home">
                    <a href="#" class="btn" id="btn_create">Ingresar</a>
                </router-link>

                    </form>
                    <hr>
                    <!--  <p class="card-text"> -->
                    Ideal para quienes desean explorar antes de comprometerse: <br>

                    👀<b>Solo ver:</b> Conoce la plataforma antes de participar. <br>
                    🕵🏻 <b>Publica anonimamente:</b> Permite esconder tus secretos y luego migrarlos a una
                    cuenta pública.
                    <router-link to="/">
                        <a class="btn btn-primary mt-2" id="btn_regresar"> Come Back </a>
                    </router-link>


                    <hr class="pb-0 mt-1">

                    <span class="text-center mt-5 ms-5" id="logo">Stringify</span>

                </div>
            </div>

        </div>
    </div>
</template>
<style scoped>
::-webkit-scrollbar {
    display: none;
}

@font-face {
    font-family: titulos;
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

@font-face {
    font-family: logo;
    src: url(../../public/fuentes/ledbetter.woff);
}


#title {
    font-family: subtitulos;
    font-size: 2.6em;
    color: #E07F84;
    scale: 1.3;
}

#description {
    font-family: narracion;
}

body {
    background: #ccc;
}

#very-card {
    font-family: logo;
}


input,
p,
a {
    font-size: 1.1em;
}

#btn_create {
    background: #7FB2F9;
    color: #fff;
    border: 2px solid #7FB2F9
}

#submit {
    background: #7FB2F9;
    color: #fff;
    border: 2px solid #7FB2F9
}

#btn_regresar {
    background: #E07F84;
    border: 2px #E07F84 solid;
}


#logo {
    font-family: logo;
    font-size: 3em;
    color: #E07F84;
}
</style>