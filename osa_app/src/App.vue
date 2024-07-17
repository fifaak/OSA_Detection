<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style>
@font-face {
  font-family: 'CustomFont';
  src: url('./assets/fonts/Kanit-Regular.ttf') format('truetype');
  font-weight: normal;
  font-style: normal;
}

#app {
  font-family: 'CustomFont', sans-serif;
  font-size: 16px;
  color: #333;
}
</style>
