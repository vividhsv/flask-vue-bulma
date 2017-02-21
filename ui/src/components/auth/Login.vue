<template>
    <div class="column is-4 is-offset-4">
        <h1 class="title">
            Login
        </h1>
        <div class="box">
            <label class="label">Email</label>
            <p class="control">
                <input class="input" :class="{'is-danger': $v.user.email.$error}" type="text"
                       placeholder="jsmith@example.org" v-model="user.email" @blur="$v.user.email.$touch()">
                <span class="help is-danger fadeInDown"
                      v-if="(!$v.user.email.required || !$v.user.email.email) && $v.user.email.$dirty">Valid email address is required</span>
            </p>
            <label class="label">Password</label>
            <p class="control">
                <input class="input" :class="{'is-danger': $v.user.password.$error}" type="password"
                       placeholder="●●●●●●●" v-model="user.password" @blur="$v.user.password.$touch()">
                <span class="help is-danger animated fadeInDown"
                      v-if="!$v.user.password.required && $v.user.password.$dirty">Password is required</span>
            </p>
            <hr>
            <p class="control">
                <button class="button is-primary" @click="login" :disabled="$v.$invalid">Login</button>
                <router-link to="/" tag="button" class="button">Cancel</router-link>
            </p>
        </div>
        <p class="has-text-centered">
            <router-link to="/auth/register">Register an Account</router-link>
            |
            <router-link to="/auth/forgotpassword">Forgot password</router-link>
            |
            <a href="#">Need help?</a>
        </p>
    </div>
</template>
<script>
  import {required, email} from 'vuelidate/lib/validators'
  export default{
    name: 'login',
    data: function () {
      return {
        user: {
          email: "",
          password: ""
        }
      }
    },
    validations: {
      user: {
        email: {
          required,
          email
        },
        password: {
          required
        }
      }
    },
    methods: {
      login(){
        this.$http.post('/auth/login', this.user)
          .then((response) => {
            this.$auth.setToken(response.data.auth_token)
            this.$router.push("/dashboard")
          })
          .catch((error) => {
            alertify.error(error.response.data.error)
          })
      }
    }

  }
</script>
<style>
</style>