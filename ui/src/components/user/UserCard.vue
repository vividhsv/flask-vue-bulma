<template>
    <div class="card">
        <div class="card-image">
            <figure class="image is-4by3">
                <img src="http://bulma.io/images/placeholders/1280x960.png" alt="Image">
            </figure>
        </div>
        <div class="card-content">
            <div class="media">
                <div class="media-left">
                    <figure class="image" style="height: 40px; width: 40px;">
                        <img src="http://bulma.io/images/placeholders/96x96.png" alt="Image">
                    </figure>
                </div>
                <div class="media-content">
                    <p class="title is-4">{{ getFullName }}</p>
                    <p class="subtitle is-6">{{ getCurrentUser.email }}</p>
                </div>
            </div>
            <small>Join on {{ getCurrentUser.date_created | moment("MMMM Do YYYY") }}</small>
        </div>
    </div>
</template>
<script>
  import {mapGetters} from 'vuex'
  export default {
    name: 'profile',
    computed: mapGetters(['getFullName', 'getCurrentUser'])
  }
</script>
<style></style>
