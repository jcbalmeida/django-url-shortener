import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Login from "../views/Login.vue";
import store from "../store";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
    meta: {
      requiresAuth: false
    }
  },
  {
    path: "*",
    redirect: "/login"
  },
  { path: "/", redirect: "/login" },
  {
    path: "/login",
    name: "Login",
    component: Login
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

router.beforeEach((to, from, next) => {
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth);
  console.debug(requiresAuth);
  const access_token = store.state.accessToken;
  console.debug(access_token);
  if (requiresAuth && !access_token) {
    next("login");
  } else {
    next();
  }
});

export default router;
