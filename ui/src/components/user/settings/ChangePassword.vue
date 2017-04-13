<template>
    <div class="column is-one-thrid">
        <form @submit.prevent="save">
            <label class="label">New Password</label>
            <p class="control">
                <input class="input" :class="{'is-danger': $v.user.password.$error}" type="password" placeholder="●●●●●●●" v-model="user.password" @blur="$v.user.password.$touch()">
                <password-strength :input="user.password"></password-strength>
                <span class="help is-danger animated fadeInDown"
                          v-if="!$v.user.password.required && $v.user.password.$dirty">Password is required</span>
            </p>
            <label class="label">Confirm Password</label>
            <p class="control">
                <input class="input" :class="{'is-danger': $v.user.repeatPassword.$error}" type="password" placeholder="●●●●●●●" v-model="user.repeatPassword" @blur="$v.user.repeatPassword.$touch()">
                <span class="help is-danger animated fadeInDown"
                          v-if="!$v.user.repeatPassword.sameAsPassword && $v.user.repeatPassword.$dirty">Passwords must be identical.</span>
            </p>
            <hr>
            <p class="control">
                <button class="button is-primary" :disabled="$v.$invalid">Change Password</button>
            </p>
        </form>
    </div>
</template>
<script>
  import PasswordStrength from '../../auth/PasswordStrength.vue'
  import {required, sameAs, minLength} from 'vuelidate/lib/validators'
  export default {
    name: 'change-password',
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
      save () {
        delete this.user.repeatPassword
        this.$http.put('/users/me', this.user)
          .then((response) => {
            this.$router.push('/')
            this.$notify.success({content: 'Password has been successfully reset'})
          })
          .catch((error) => {
            this.$notify.error({content: error.response.data.error})
          })
      }
    }
  }
</script>
<style></style>
