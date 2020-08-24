<template>
  <div>
    <h1>Login</h1>
    <input type="text" v-model="username" placeholder="username" />
    <br />
    <input type="password" v-model="password" placeholder="password" />
    <br />
    <div>
      <button @click="login">Login</button>
    </div>
    <ul v-if="errors && errors.length">
      <li v-for="error in errors" :key="error">
        {{ error.message }}
      </li>
    </ul>
  </div>
</template>
<script>
import axios from "axios";
import { mapState, mapMutations } from "vuex";

export default {
  name: "login",
  computed: { ...mapState(["access_token", "refresh_token"]) },
  data() {
    return {
      username: "",
      password: "",
      errors: []
    };
  },
  methods: {
    ...mapMutations(["updateAccessToken", "updateRefreshToken"]),
    login: function() {
      axios
        .post("http://localhost:8000/token/", {
          username: this.username,
          password: this.password
        })
        .then(response => {
          this.$store.dispatch("updateAccessToken", response.data.access);
          this.$store.dispatch("updateRefreshToken", response.data.refresh);
          this.$router.replace("/");
        })
        .catch(e => {
          return Promise.reject(e);
        });
    }
  }
};
</script>
