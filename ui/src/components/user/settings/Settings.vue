<template>
    <section class="section">
        <div class="container">
            <div class="columns">
                <div class="column is-2">
                    <aside class="menu">
                        <ul class="menu-list">
                            <li>
                                <router-link active-class="is-active" to="/user/settings/info">User Information
                                </router-link>
                            </li>
                            <li>
                                <router-link active-class="is-active" to="/user/settings/email">Change Email
                                </router-link>
                            </li>
                            <li>
                                <router-link active-class="is-active" to="/user/settings/changepassword">Change
                                    Password
                                </router-link>
                            </li>
                            <li>
                                <router-link active-class="is-active" to="/user/settings/delete">Delete Account
                                </router-link>
                            </li>
                        </ul>
                    </aside>
                </div>
                <router-view></router-view>
                <div class="column is-4">
                    <user-card></user-card>
                </div>
            </div>
        </div>
    </section>
</template>
<script>
  import UserCard from '../UserCard.vue'
  export default {
    name: 'Settings',
    components: {UserCard}
  }
</script>
<style>
</style>
