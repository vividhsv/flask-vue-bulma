<template>
    <section class="hero is-fullheight is-default is-bold">
        <div class="hero-head">
            <div class="container">
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
                                <Dropdown :name="current_user.first_name">
                                      <ul slot="content" class="menu-list">
                                        <li><a>Profile</a></li>
                                        <li><a>Settings</a></li>
                                          <hr>
                                        <li><a @click="logout">Logout</a></li>
                                      </ul>
                                </Dropdown>
                          </span>
                        </div>
                    </div>
                </nav>
            </div>
        </div>

        <div class="hero-body">
            <div class="container has-text-centered">
                <div class="columns is-vcentered">
                    <div class="column is-5">
                        <figure class="image is-4by3">
                            <img src="http://placehold.it/800x600" alt="Description">
                        </figure>
                    </div>
                    <div class="column is-6 is-offset-1">
                        <h1 class="title is-2">
                            Superhero Scaffolding
                        </h1>
                        <h2 class="subtitle is-4">
                            Let this cover page describe a product or service.
                        </h2>
                        <br>
                        <p class="has-text-centered">
                            <a class="button is-large">
                                Learn more
                            </a>
                        </p>
                    </div>
                </div>
            </div>
        </div>

        <div class="hero-foot">
            <div class="container">
                <div class="tabs is-centered">
                    <ul>
                        <li><a>And this at the bottom</a></li>
                    </ul>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
  import Dropdown from './Dropdown.vue'
  export default{
    name: 'root',
    components: {Dropdown},
    data () {
      return {
        current_user: this.$store.state.current_user,
        isloggedIn: this.$auth.loggedIn()
      }
    },
    methods: {
      logout () {
        this.$auth.destoryToken()
        this.isloggedIn = false
      }
    }
  }
</script>

<style>
</style>

