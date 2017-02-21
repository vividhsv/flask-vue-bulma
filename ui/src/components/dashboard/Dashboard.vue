<template>
    <div class="columns">
        <aside class="column is-2 aside hero is-fullheight is-hidden-mobile">
            <div>
                <div class="main">
                    <div class="title">Main</div>
                    <a href="#" class="item active"><span class="icon"><i class="fa fa-home"></i></span><span
                            class="name">Dashboard</span></a>
                    <a href="#" class="item"><span class="icon"><i class="fa fa-map-marker"></i></span><span
                            class="name">Activity</span></a>
                    <a href="#" class="item"><span class="icon"><i class="fa fa-th-list"></i></span><span class="name">Timeline</span></a>
                    <a href="#" class="item"><span class="icon"><i class="fa fa-folder-o"></i></span><span class="name">Folders</span></a>
                </div>
            </div>
        </aside>
        <div class="column is-10 admin-panel">
            <nav class="nav has-shadow" id="top">
                <div class="container">
                    <div class="nav-left">
                        <a class="nav-item" href="#">
                            <img src="../../assets/bulma.png" alt="Description">
                        </a>
                    </div>
                    <div class="nav-right nav-menu">
                        <span class="nav-item">
                            <button @click="logout" class="button is-info">
                            Logout
                            </button>
                        </span>
                    </div>
                </div>
            </nav>
            <section class="hero is-small">
                <!-- Hero content: will be in the middle -->
                <div class="hero-body">
                    <div class="container">
                        <h1 class="title">
                            Admin Dashboard
                        </h1>
                        <h2 class="subtitle">
                            A simple admin template
                        </h2>
                    </div>
                </div>
            </section>
        </div>
    </div>
</template>
<script>
  export default {
    name: 'dashboard',
    methods: {
      logout(){
        this.$auth.destoryToken()
        this.$router.push('/')
      }
    }
  }
</script>
<style>
    body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
        height: 100%;
    }

    .button.is-success {
        background-color: #2EB398;
    }

    .nav.is-dark {
        background-color: #232B2D;
        color: #F6F7F7;
    }

    .nav.is-dark .nav-item a, .nav.is-dark a.nav-item {
        color: #F6F7F7;
    }

    .nav.is-dark .nav-item a.button.is-default {
        color: #F6F7F7;
        background-color: transparent;
        border-width: 2px;
    }

    .aside {
        background-color: #354052;
        margin-right: -10px;
    }

    .aside .main {
        padding: 40px;
        color: #6F7B7E;
    }

    .aside .title {
        color: #6F7B7E;
        font-size: 12px;
        font-weight: bold;
        text-transform: uppercase;
    }

    .aside .main .item {
        display: block;
        padding: 10px 0;
        color: #6F7B7E;
    }

    .aside .main .item.active {
        color: #F6F7F7;
    }

    .aside .main .icon {
        font-size: 19px;
        padding-right: 30px;
    }

    .aside .main .name {
        font-size: 16px;
        font-weight: bold;
    }

    .admin-panel {
        padding-bottom: 0;
    }

    .content {
        display: block;
        background-color: #fff;
        padding: 40px 20px;
    }

    .hero .tabs ul {
        border-bottom: 1px solid #d3d6db;
    }

</style>