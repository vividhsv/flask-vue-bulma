<template>
    <div class="column is-4 is-offset-4">
        <h1 class="title">
            Register an Account
        </h1>
        <div class="box">
            <form @submit.prevent="register">
                <label class="label">First Name</label>
                <p class="control">
                    <input class="input" :class="{'is-danger': $v.user.first_name.$error}" type="text"
                           placeholder="John"
                           v-model="user.first_name" @blur="$v.user.first_name.$touch()">
                    <span class="help is-danger animated fadeInDown"
                          v-if="!$v.user.first_name.required && $v.user.first_name.$dirty">First Name is required</span>
                </p>
                <label class="label">Last Name</label>
                <p class="control">
                    <input class="input" :class="{'is-danger': $v.user.last_name.$error}" type="text"
                           placeholder="Smith"
                           v-model="user.last_name" @blur="$v.user.last_name.$touch()">
                    <span class="help is-danger animated fadeInDown"
                          v-if="!$v.user.last_name.required && $v.user.last_name.$dirty">Last Name is required</span>
                </p>
                <label class="label">Email</label>
                <p class="control">
                    <input class="input" :class="{'is-danger': $v.user.email.$error}" type="text"
                           placeholder="jsmith@example.org" v-model="user.email" @blur="$v.user.email.$touch()">
                    <span class="help is-danger animated fadeInDown"
                          v-if="(!$v.user.email.required || !$v.user.email.email) && $v.user.email.$dirty">Valid email address is required</span>
                </p>
                <hr>
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
                    <button type="submit" class="button is-primary" :disabled="$v.$invalid">Register</button>
                    <router-link to="/" tag="button" class="button is-default">Cancel</router-link>
                </p>
            </form>
        </div>
        <p class="has-text-centered">
            <router-link to="/auth/login">Login</router-link>
            |
            <a href="#">Need help?</a>
        </p>
    </div>
</template>
<script>
  import {required, email, sameAs, alpha, minLength} from 'vuelidate/lib/validators'
  import PasswordStrength from './PasswordStrength.vue'

  export default {
    name: 'register',
    components: {PasswordStrength},
    data () {
      return {
        user: {
          first_name: '',
          last_name: '',
          email: '',
          password: '',
          repeatPassword: ''
        }
      }
    },
    validations: {
      user: {
        first_name: {
          required, alpha
        },
        last_name: {
          required, alpha
        },
        email: {
          required,
          email
        },
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
      register () {
        delete this.user.repeatPassword
        this.$http.post('/auth/registration', this.user)
          .then((response) => {
            this.$router.push('/auth/login')
            this.$notify.success({content: 'Registration Successful. You can now login.'})
          })
          .catch((error) => {
            console.log(error)
            if (error.response.status === 400) {
              for (let [key, value] of Object.entries(error.response.data)) {
                this.$notify.error(key + ': ' + value)
              }
            }
            if (error.response.status === 409) {
              this.$notify.error({content: error.response.data.error})
            }
          })
      }
    }
  }
</script>
<style>

</style>
