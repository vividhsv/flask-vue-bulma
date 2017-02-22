<template>
    <div class="notification" :class="typeClass" v-show="isShow">
        <button class="delete" @click="handleClose"></button>
        <div class="title is-5" v-if="title">{{ title }}</div>
        {{ content }}
    </div>
</template>
<script>
  export default {
    props: {
      duration: {
        type: Number,
        default: 4500,
      },
      type: {
        type: String,
        default: 'default',
      },
      title: {
        type: String,
      },
      content: {
        type: String,
        default: '',
      },
    },
    data(){
      return {
        isShow: false
      }
    },
    computed: {
      typeClass(){
        return this.type ? `is-${this.type}` : null
      }
    },
    methods: {
      handleClose() {
        this.isShow = false;
        setTimeout(() => {
          this.$destroy();
          this.$el.remove();
        }, 100);
      },
      close() {
        clearTimeout(this.timer);
        this.isShow = false;
        this.$destroy();
        this.$el.remove();
      },
    },
    beforeMount() {
      let parent;
      parent = document.querySelector('.notifications');
      if (!parent) {
        parent = document.createElement('div');
        parent.classList.add('notifications');
        document.body.appendChild(parent);
      }
      parent.appendChild(this.$el);
    },
    mounted() {
      this.isShow = true
      this.timer = setTimeout(() => this.close(), this.duration);
    },

  }

</script>
<style>
    .notifications {
        position: fixed;
        max-width: 400px;
        top: 20px;
        right: 5px;
        z-index: 5000;
    }
</style>