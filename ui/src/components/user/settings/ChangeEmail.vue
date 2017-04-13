<template>
    <div class="column is-one-thrid">
        <form @submit.prevent="save">
            <label class="label">Email</label>
            <p class="control">
                <input class="input" :class="{'is-danger': $v.user.email.$error}" type="text" placeholder="Email" v-model="user.email" @blur="$v.user.email.$touch()">
                <span class="help is-danger animated fadeInDown"
                          v-if="(!$v.user.email.required || !$v.user.email.email) && $v.user.email.$dirty">Valid email address is required</span>
            </p>
            <hr>
            <p class="control">
                <button class="button is-primary" type="submit" :disabled="$v.$invalid">Save</button>
            </p>
        </form>
    </div>
</template>
<script>
  import {required, email} from 'vuelidate/lib/validators'
  import clone from 'lodash/clone'
  export default{
    name: 'change-email',
    data () {
      return {
        user: {
          email: clone(this.$store.getters.getCurrentUser.email)
        }
      }
    },
    validations: {
      user: {
        email: {
          required, email
        }
      }
    },
    methods: {
      save () {
        this.$http.put('/users/me', this.user)
          .then((response) => {
            this.$store.dispatch('update_user', response.data)
            this.$notify.success({content: 'User email updated successfully'})
          })
          .catch((error) => {
            this.$notify.error({content: error.response.data.error})
          })
      }
    }
  }
</script>
<style></style>
