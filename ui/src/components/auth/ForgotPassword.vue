<template>
    <div class="column is-4 is-offset-4">
        <h1 class="title">
            Reset Password
        </h1>
        <div class="box">
            <label class="label">Email</label>
            <p class="control">
                <input class="input" :class="{'is-danger': $v.user.email.$error}" type="text"
                       placeholder="jsmith@example.org" v-model="user.email" @blur="$v.user.email.$touch()">
                <span class="help is-danger fadeInDown"
                      v-if="(!$v.user.email.required || !$v.user.email.email) && $v.user.email.$dirty">Valid email address is required</span>
            </p>
            <hr>
            <p class="control">
                <button class="button is-primary" @click="reset" :disabled="$v.$invalid">Request Reset</button>
                <router-link to="/auth/login" tag="button" class="button">Cancel</router-link>
            </p>
        </div>
        <p class="has-text-centered">
            <router-link to="/auth/register">Register an Account</router-link>
            |
            <router-link to="/auth/login">Log In</router-link>
            |
            <a href="#">Need help?</a>
        </p>
    </div>
</template>
<script>
  import {required, email} from 'vuelidate/lib/validators'
  export default {
    name: 'forgot-password',
    data: function () {
      return {
        user: {
          email: ""
        }
      }
    },
    validations: {
      user: {
        email: {
          required,
          email
        },
      }
    },
    methods: {
      reset(){
        this.$http.post("/auth/reset", this.user)
          .then((response) => {
            alertify.success(response.data.message)
            this.$router.push("/")
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