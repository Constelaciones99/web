import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
  history: createWebHistory(import.meta.BASE_URL),
  routes: [
    {
      path: "/",
      name: "",
      component: () => import("../views/WorldView.vue"),
    },
    {
      path: "/LogeoPage",
      name: "logeo",
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../views/LogeoPage.vue"),
    },
    {
      path: "/Card",
      name: "card-index",
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../views/HomeView.vue"),
    },
    {
      path: "/PrivatePage",
      name: "private",
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../views/PrivateView.vue"),
    },
    {
      path: "/PublicPage",
      name: "public",
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../views/PublicView.vue"),
    },
    {
      path: "/Home",
      name: "home",
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../views/IndexView.vue"),
    },
    {
      path: "/Search",
      name: "search",
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../views/SearchView.vue"),
    },
    {
      path: "/New",
      name: "new",
      component: () => import("../views/NewView.vue"),
    },
    {
      path: "/Gym",
      name: "gym",
      component: () => import("../views/GymView.vue"),
    },
    {
      path: "/Tips",
      name: "tips",
      component: () => import("../views/AdviceView.vue"),
    },
    {
      path: "/Notify",
      name: "novedades",
      component: () => import("../views/NotifyView.vue"),
    },
    {
      path: "/Profile",
      name: "perfil",
      component: () => import("../views/ProfileView.vue"),
    },
  ],
});

export default router;
