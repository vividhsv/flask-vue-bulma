<template>
    <div class="dropdown">
        <button class="button is-info drop-marker" @click="toggle" v-on-clickaway="away">
            <span class="drop-marker">{{ name }}</span>
            <span class="icon drop-marker">
                <i class="fa fa-angle-down drop-marker"></i>
            </span>
        </button>
        <div class="dropdown-content" :class="{'showdrop' : isShown }">
            <slot name="content"></slot>
        </div>
    </div>
</template>
<script>
  import {mixin as clickaway} from 'vue-clickaway'

  export default {
    name: 'drop-down',
    mixins: [clickaway],
    props: {
      name: {
        type: String,
        required: true
      }
    },
    data () {
      return {
        isShown: false
      }
    },
    methods: {
      away () {
        if (this.isShown) {
          this.isShown = false
        }
      },
      toggle () {
        this.isShown = !this.isShown
      }
    }
  }
</script>
<style>
    .dropdown {
        margin-left: .75rem;
        display: inline-block;
        position: relative;
        vertical-align: middle;
        width: max-content;
    }
    .dropdown-content {
        position: absolute;
        border-radius: 3px;
        margin-top: .20rem;
        display: none;
        border: 1px solid #dbdbdb;
        text-align: left;
        background-color: #ffffff;
        width: 100%;
        min-width: max-content;
    }
    .showdrop {
        display: block;
    }
    .dropdown-content hr {
        margin-top: 0px;
        margin-bottom: 0px;
    }

</style>
