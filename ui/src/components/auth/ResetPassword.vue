<template>
    <div class="column is-4 is-offset-4">
        <h1 class="title">
            Reset Password
        </h1>
        <div class="box">
            <form @submit.prevent="reset_password">
                <label class="label">Password</label>
                <p class="control">
                    <input class="input" :class="{'is-danger': $v.user.password.$error}" type="password"
                           placeholder="●●●●●●●" v-model="user.password" @blur="$v.user.password.$touch()">
                    <password-strength :input="user.password"></password-strength>
                    <span class="help is-danger animated fadeInDown"
                          v-if="!$v.user.password.required && $v.user.password.$dirty">Password is required</span>
                </p>
                <label class="label">Confirm Password</label>
                <p class="control">
                    <input class="input" :class="{'is-danger': $v.user.repeatPassword.$error}" type="password"
                           placeholder="●●●●●●●" v-model="user.repeatPassword" @blur="$v.user.repeatPassword.$touch()">
                    <span class="help is-danger animated fadeInDown"
                          v-if="!$v.user.repeatPassword.sameAsPassword && $v.user.repeatPassword.$dirty">Passwords must be identical.</span>
                </p>
                <hr>
                <p class="control">
                    <button type="submit" class="button is-primary" :disabled="$v.$invalid">Reset</button>
                    <router-link to="/" tag="button" class="button is-default">Cancel</router-link>
                </p>
            </form>
        </div>
        <p class="has-text-centered">
            <router-link to="/auth/register">Register an Account</router-link>
            |
            <router-link to="/auth/login">Log In</router-link>
            |
            <a href="#">Need help?</a>
        </p>
        </form>
    </div>
</template>
<script>
  import {required, sameAs, minLength} from 'vuelidate/lib/validators'
  import PasswordStrength from './PasswordStrength.vue'

  export default {
    name: 'reset-password',
    components: {PasswordStrength},
    data () {
      return {
        user: {
          password: '',
          repeatPassword: ''
        }
      }
    },
    validations: {
      user: {
        password: {
          required,
          minLength: minLength(8)
        },
        repeatPassword: {
          sameAsPassword: sameAs('password')
        }
      }
    },
    methods: {
      reset_password(){
        delete this.user.repeatPassword
        this.$http.post('/auth/reset/' + this.$route.query.token, this.user)
          .then((response) => {
            this.$router.push('/')
            this.$notify.success({content: response.data.message})
          })
          .catch((error) => {
            this.$notify.error({content: error.response.data.error})
          })
      }
    }
  }
</script>
<style>

</style>