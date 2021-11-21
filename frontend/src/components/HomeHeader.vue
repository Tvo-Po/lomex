<template>
    <header>
        <div @click="$router.push({ name: 'Home' })" class="home-button">
            <div class="icon"></div>
        </div>
    </header>
</template>

<script>
export default {
    name: 'HomeHeader'
}
</script>

<style scoped>

    header {
        height: 10px;
        padding-top: 10px;
        display: flex;
        align-items: center;
        justify-content: flex-start;
    }

    .home-button {
        background: linear-gradient(331.93deg, #1D222E 11.88%, #293140 85.18%);
        mix-blend-mode: normal;
        border: 2px solid rgba(29, 34, 46, 0.1);
        box-sizing: border-box;
        box-shadow: -10px -10px 20px rgba(57, 66, 83, 0.35), 10px 10px 20px rgba(24, 28, 39, 0.35);
        margin-top: 120px;
        width: 60px;
        height: 60px;
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        padding-bottom: 4px;
        transition: 0.2s;
        -o-transition: 0.2s ease-in-out;
        -moz-transition: 0.2s ease-in-out;
        -webkit-transition: 0.2s ease-in-out;
    }

    .icon {
        background: no-repeat url('../assets/Home.svg');
        background-position: center;
        height: 100%;
        width: 100%;
        transition: 0.2s;
        -o-transition: 0.2s ease-in-out;
        -moz-transition: 0.2s ease-in-out;
        -webkit-transition: 0.2s ease-in-out;
    }

    .home-button:hover {
        box-shadow: -5px -5px 20px 4px rgba(57, 66, 83, 0.35), 6px 6px 20px 6px rgba(24, 28, 39, 0.35);
        transition: 0.2s;
        -o-transition: 0.2s ease-in-out;
        -moz-transition: 0.2s ease-in-out;
        -webkit-transition: 0.2s ease-in-out;
    }

    .home-button:active {
        box-shadow: -5px -5px 10px rgba(72, 80, 99, 0.1), 5px 5px 10px rgba(24, 28, 39, 0.35), inset -2px -2px 4px rgba(72, 80, 99, 0.35), inset 5px 5px 5px #1D222E;
    }

    .icon:active {
        background: no-repeat url('../assets/HomeActive.svg');
        background-position: center;
        transition: 0.2s;
        -o-transition: 0.2s ease-in-out;
        -moz-transition: 0.2s ease-in-out;
        -webkit-transition: 0.2s ease-in-out;
    }

</style>