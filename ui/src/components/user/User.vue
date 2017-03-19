<template>
    <div>
        <Navi></Navi>
        <router-view></router-view>
    </div>
</template>

<script>
  import Navi from '../Navi.vue'
  export default{
    name: 'user',
    components: {Navi}
  }
</script>
<style>
</style>
