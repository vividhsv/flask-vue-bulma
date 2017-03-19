<template>
    <section>
    <Navi></Navi>
        <router-view>
        </router-view>
    </section>
</template>

<script>
  import Navi from './Navi.vue'
  export default{
    name: 'root',
    components: { Navi }
  }
</script>
<style>
</style>
