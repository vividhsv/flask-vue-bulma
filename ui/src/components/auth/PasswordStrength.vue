<template>
    <progress class="progress" :value="passwordStrength" max="5"></progress>
</template>
<script>
  import zxcvbn from 'zxcvbn'

  export default{
    name: 'password-strength',
    props: {
      input: {
        type: String,
        required: true
      }
    },
    computed: {
      passwordStrength () {
        if (this.input) {
          return zxcvbn(this.input).score + 1
        }
        return null
      }
    }
  }

</script>
<style>
    .progress {
        border-radius: 0px;
        height: 0.25rem;
        margin-bottom: 0px;
    }

    .progress:not(:last-child) {
        margin-bottom: 0px;
    }

    progress[value="1"] {
        background: darkred;
    }

    progress[value="1"]::-webkit-progress-value {
        background: darkred;
    }

    progress[value="1"]::-moz-progress-bar {
        background: darkred;
    }

    progress[value="2"] {
        background: red;
    }

    progress[value="2"]::-webkit-progress-value {
        background: red;
    }

    progress[value="2"]::-moz-progress-bar {
        background: red;
    }

    progress[value="3"] {
        background: orange;
    }

    progress[value="3"]::-webkit-progress-value {
        background: orange;
    }

    progress[value="3"]::-moz-progress-bar {
        background: orange;
    }

    progress[value="4"] {
        background: yellowgreen;
    }

    progress[value="4"]::-webkit-progress-value {
        background: yellowgreen;
    }

    progress[value="4"]::-moz-progress-bar {
        background: yellowgreen;
    }

    progress[value="5"] {
        background: green;
    }

    progress[value="5"]::-webkit-progress-value {
        background: green;
    }

    progress[value="5"]::-moz-progress-bar {
        background: green;
    }
</style>