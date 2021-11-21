<template>
  <div>
    <div class="home">
      <h1>API</h1>
      <div @click="$router.push({ name: 'Genres' })">
        <api-button>Genres</api-button>
      </div>
      <div @click="$router.push({ name: 'Actors' })">
        <api-button>Actors</api-button>
      </div>
      <div @click="$router.push({ name: 'Directors' })">
        <api-button>Directors</api-button>
      </div>
    </div>
  </div>
</template>

<script>

import ApiButton from '@/components/UI/ApiButton.vue'

export default {
  name: 'Home',
  components: {
    ApiButton
  }
}
</script>

<style scoped>
  .home {
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding-bottom: 70px;
  }

  h1 {
    font-size: 40px;
    font-weight: 700;
    color: rgba(255, 255, 255, 0.65);
    line-height: 30px;
    margin: 0 auto;
    text-align: center;
    padding: 12px 0px;
    width: 360px;
  }
</style>
