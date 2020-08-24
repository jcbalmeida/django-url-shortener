import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    accessToken: "",
    refreshToken: ""
  },
  mutations: {
    updateAccessToken(state, token) {
      state.accessToken = token;
    },
    updateRefreshToken(state, token) {
      state.refreshToken = token;
    }
  },
  actions: {
    updateAccessToken(context, token) {
      context.commit("updateAccessToken", token);
    },
    updateRefreshToken(context, token) {
      context.commit("updateRefreshToken", token);
    }
  },
  modules: {}
});
