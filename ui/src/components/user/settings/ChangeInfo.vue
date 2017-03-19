<template>
    <div class="column is-one-thrid">
        <form>
            <label class="label">First Name</label>
            <p class="control">
                <input class="input" :class="{'is-danger': $v.user.first_name.$error}" type="text"
                       placeholder="First Name"
                       v-model="user.first_name" @blur="$v.user.first_name.$touch()">
                <span class="help is-danger animated fadeInDown"
                      v-if="!$v.user.first_name.required && $v.user.first_name.$dirty">First Name is required</span>
            </p>
            <label class="label">Last Name</label>
            <p class="control">
                <input class="input" :class="{'is-danger': $v.user.last_name.$error}" type="text"
                       placeholder="Last Name"
                       v-model="user.last_name" @blur="$v.user.last_name.$touch()">
                <span class="help is-danger animated fadeInDown"
                      v-if="!$v.user.last_name.required && $v.user.last_name.$dirty">Last Name is required</span>
            </p>
            <hr>
            <p class="control">
                <button class="button is-primary" @click="save">Save</button>
            </p>
        </form>
    </div>
</template>
<script>
  import {required, alpha} from 'vuelidate/lib/validators'
  import clone from 'lodash/clone'
  export default {
    name: 'info',
    data () {
      return {
        user: {
          first_name: clone(this.$store.getters.getCurrentUser.first_name),
          last_name: clone(this.$store.getters.getCurrentUser.last_name)
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
        }
      }
    },
    methods: {
      save () {
        this.$http.put(`/users/${this.$store.getters.getCurrentUser.id}`, this.user)
          .then((response) => {
            this.$store.dispatch('update_user', response.data)
            this.$notify.success({content: 'User information updated successfully'})
          })
      }
    }
  }
</script>
<style></style>
