<template>
    <section class="hero is-fullheight is-dark is-bold">
        <div class="hero-body">
            <div class="container">
                <div class="columns is-vcentered">
                    <transition enter-active-class="animated zoomIn">
                        <router-view></router-view>
                    </transition>
                </div>
            </div>
        </div>

    </section>
</template>
<script>
  export default {
    name: "auth",
  }

</script>
<style>
</style>