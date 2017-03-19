<template>
    <nav class="nav has-shadow">
        <div class="container">
            <div class="nav-left">
                <router-link to="/" class="nav-item">
                    <img src="../assets/bulma.png" alt="Description">
                </router-link>
            </div>
            <div class="nav-right nav-menu">
                <a class="nav-item is-tab is-active">
                    Home
                </a>
                <a class="nav-item is-tab">
                    Features
                </a>
                <a class="nav-item is-tab">
                    Team
                </a>
                <a class="nav-item is-tab">
                    Help
                </a>
                <span class="nav-item" v-if="!isloggedIn">
                    <router-link to="/auth/login" tag="button" class="button">
                      Log in
                    </router-link>
                    <router-link to="/auth/register" tag="button" class="button is-info">
                      Sign up
                    </router-link>
                </span>
                <span class="nav-item" v-if="isloggedIn">
                    <Dropdown :name="getFullName">
                          <ul slot="content" class="menu-list">
                            <li><router-link to="/user/profile">Profile</router-link></li>
                            <li><router-link to="/user/settings">Settings</router-link></li>
                              <hr>
                            <li><a @click="logout">Logout</a></li>
                          </ul>
                    </Dropdown>
                </span>
            </div>
        </div>
    </nav>
</template>
<script>
  import Dropdown from './Dropdown.vue'
  import {mapGetters} from 'vuex'
  export default{
    name: 'navi',
    components: {Dropdown},
    data () {
      return {
        isloggedIn: this.$auth.loggedIn()
      }
    },
    computed: mapGetters(['getFullName']),
    methods: {
      logout () {
        this.$auth.destoryToken()
        this.isloggedIn = false
        this.$router.push('/')
      }
    },
    created () {
      if (this.$auth.loggedIn()) {
        this.$http.defaults.headers.common['Authorization'] = `Bearer ${this.$auth.getToken()}`
        this.$store.dispatch('set_me')
      }
    }
  }
</script>
<style>
</style>
