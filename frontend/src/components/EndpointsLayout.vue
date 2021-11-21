<template>
        <div class="endpoint-layout">
            <home-header></home-header>
            <router-view></router-view>
        </div>
</template>

<script>
import HomeHeader from './HomeHeader.vue'

export default {
    components: { HomeHeader }
}
</script>