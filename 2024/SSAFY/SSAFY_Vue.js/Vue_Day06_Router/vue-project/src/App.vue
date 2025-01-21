<template>
  <div>
    <h2>App.vue</h2>
    <nav>
      <RouterLink to="/">Home</RouterLink> | 
      <RouterLink to="/about">about</RouterLink> |
      <RouterLink :to="{name: 'home'}">HomeName</RouterLink> | 
      <RouterLink :to="{name: 'about'}">aboutName</RouterLink> |
      <RouterLink :to="{name: 'user', params :{id:'ssafy'}}">행복</RouterLink> | 
      <RouterLink :to="{name: 'user', params :{id:'heynem'}}">혜민</RouterLink> |
      <RouterLink :to="{name: 'login'}">로그인</RouterLink>
    </nav>
    <RouterView />
  </div>

</template>

<script setup>
  // import { RouterLink, RouterView } from 'vue-router';
</script>

<style scoped>

</style>