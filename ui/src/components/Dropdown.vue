<template>
    <div class="dropdown">
        <button class="button is-info drop-marker" @click="toggle">
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
  export default {
    name: 'drop-down',
    props: {
      name: {
        type: String,
        required: true
      },
    },
    data(){
      return {
        isShown: false
      }
    },
    methods: {
      toggle(){
        this.isShown = !this.isShown;
        if (this.isShown) {
          window.addEventListener('click', (e) => {
            if (!e.target.matches('.drop-marker') && this.isShown) {
              this.isShown = false
            }
          })
        } else {
          window.removeEventListener('click', (e) => {
            if (!e.target.matches('.drop-marker') && this.isShown) {
              this.isShown = false
            }
          })
        }
      },
    },
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
        /*box-shadow: 0 6px 12px rgba(0,0,0,.175);*/

    }

    .showdrop {
        display: block;
    }

    .dropdown-content hr {
        margin-top: 0px;
        margin-bottom: 0px;
    }

</style>