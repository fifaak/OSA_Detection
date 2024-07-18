<template>
    <div class="breathing-alert">
      <img loading="lazy" src="https://cdn.builder.io/api/v1/image/assets/TEMP/f8b3c38ac465a7bc7a71441f87d388fb98da3154f1d74ea3f1e940c5c18ceaf1?apiKey=167f8969fc9e4702b2c941ecb34dd7f8&" class="background-image" alt="" />
      <img loading="lazy" src="../assets/Alert.png" class="alert-icon" alt="Alert icon" />
      <h1 class="alert-message">คุณหยุดหายใจเกิน 25 วินาที !</h1>
      <p class="alert-level">ระดับ เตือน</p>
      <button class="stop-button" @click="navigateToSleeping">กดเพื่อหยุด</button>
      <button class="test_btn" @click="navigateToSOS">test alert</button>

    </div>
  </template>
  
  <script>

    // import { ref, computed, onMounted, onUnmounted } from 'vue';
    import { useRouter } from 'vue-router';
    export default {
    name: 'Alert1',
    setup() {
        const router = useRouter();
        const navigateToSleeping = () => {
            router.push('/sleeping');
        }
        const navigateToSOS = () =>{
        router.push('/Alert2');
      }
        return {
            navigateToSleeping,
            navigateToSOS
        };
    
    }
}
  </script>
  
  <style scoped>
  .breathing-alert {
    display: flex;
    flex-direction: column;
    overflow: hidden;
    /* position: absolute; */
    aspect-ratio: 0.46;
    /* max-width: 480px; */
    width: 100%;
    padding: 0;
    align-items: center;
    color: #fff;
    font-weight: 800;
    margin: 0 auto;
    /* border: 2px solid black; */
  }
  .test_btn{
    z-index: 2;
    position: absolute;
    bottom: 40px;
  }
  .background-image {
    position: absolute;
    inset: 0;
    height: 100%;
    width: 100%;
    object-fit: cover;
    object-position: center;
  }
  
  .alert-icon {
    z-index: 0;
    aspect-ratio: 1;
    object-fit: auto;
    object-position: center;
    width: 250px;
    /* box-shadow: 0 4px 49px #000; */
    margin-top: 68px;
    min-width: 60%;
    /* border: 2px solid black; */
  }
  
  .alert-message {
    position: relative;
    font-family: "CustomFont", sans-serif;
    font-weight: 600;
    font-size: 20px;
    margin-top: 15px;
    margin-bottom:0px;
  }
  
  .alert-level {
    position: relative;
    text-align: center;
    color: rgb(214, 214, 214);
    font-family: "CustomFont", sans-serif;
    font-weight: 400;
    font-size: 20px;
    margin-top: 1px;
  }
  
  .stop-button {
    position: relative;
    -webkit-text-stroke: 1px rgba(0, 0, 0, 0.3);
    font-family: Rubik, sans-serif;
    border: 1px solid rgba(0, 0, 0, 0.3);
    border-radius: 30px;
    background-color: #000;
    box-shadow: 0 4px 4px rgba(0, 0, 0, 0.25);
    align-self: stretch;
    margin-top: 78px;
    font-weight: 700;
    width:80%;
    text-align: center;
    color:white;
    font-size: 20px;
    font-family: "CustomFont", sans-serif;
    margin: auto;
    white-space: nowrap;
    text-align: center;
    padding: 17px 40px;
    margin-top: 250px;
    cursor: pointer;
  }
  </style>