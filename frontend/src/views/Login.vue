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

export default {
  name: "login",
  data() {
    return {
      username: "",
      password: "",
      errors: []
    };
  },
  methods: {
    login: function() {
      axios
        .post("http://localhost:8000/token/", {
          username: this.username,
          password: this.password
        })
        .then(response => {
          console.log(response);
          this.$router.replace("/");
        })
        .catch(e => {
          console.debug(e);
        });
    }
  }
};
</script>
