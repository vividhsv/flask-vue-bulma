<template>
    <div class="section">
        <div class="container">
            <div class="columns">
                <div class="column is-one-third">
                    <user-card></user-card>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
  import UserCard from './UserCard.vue'
  export default {
    name: 'profile',
    components: { UserCard }
  }
</script>
<style>
</style>
