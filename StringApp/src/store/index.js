import { createStore } from "vuex";
import axios from "axios";
export default createStore({
  state: {
    navif: true,
    datos: [],
  },
  getters: {},
  mutations: {
    enviarDatos() {
      console.log(this.datos);
    },
  },
  actions: {
    async fetchDatabase({ commit }) {
      axios
        .get("http://localhost:3100/api/datos")
        .then((response) => {
          console.log(response.data[0][0]);
          response.data[0][0].forEach((x) => {
            this.datos.push(x.user);
            console.log(x);
          });
        })
        .catch((error) => {
          console.log(error);
        });

      this.commit("enviarDatos");
    },
  },
  modules: {},
});
