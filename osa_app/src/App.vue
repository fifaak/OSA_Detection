<template>
  <div id="app">
    <transition name="fade" mode="out-in">
      <router-view />
    </transition>
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
/* src/assets/styles/transitions.css */
.fade-enter-active, .fade-leave-active {
    transition: opacity .1s;
  }
  .fade-enter, .fade-leave-to {
    opacity: 0;
  }
  
#app {
  font-family: 'CustomFont', sans-serif;
  font-size: 16px;
  color: #333;
}
</style>
