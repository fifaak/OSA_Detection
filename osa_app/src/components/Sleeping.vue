<!-- Sleeping.vue -->
<template>
      <div class="good-night-container">
        <img loading="lazy" src="https://cdn.builder.io/api/v1/image/assets/TEMP/f8b3c38ac465a7bc7a71441f87d388fb98da3154f1d74ea3f1e940c5c18ceaf1?apiKey=167f8969fc9e4702b2c941ecb34dd7f8&" class="background-image" alt="" />
        <img loading="lazy" src="https://cdn.builder.io/api/v1/image/assets/TEMP/54afc3a23b4a729daee8341f9d60916b27cadf4fc0b646680ad1a9ee2326274d?apiKey=167f8969fc9e4702b2c941ecb34dd7f8&" class="top-image" alt="" />
        <img class="moon" src="../assets/moon.png" alt="">
        <header class="header">
          <h1 class="greeting">Good Night</h1>
          <p class="time">23:30</p>
        </header>
        <main>
          <p class="status-message">1 Hrs/20 min</p>
          <img loading="lazy" src="https://cdn.builder.io/api/v1/image/assets/TEMP/b6716f6ccbb1c1d439e547792df58a0aa51bd9f1a0c2abe344ba68116c06896f?apiKey=167f8969fc9e4702b2c941ecb34dd7f8&" class="breathing-image" alt="Breathing visualization" />
          <button class="stop-recording-btn">ยืนยันการตื่นนอน</button>
        </main>

      </div>
  
  </template>
  <script>
  export default {
    name: 'Sleeping',
    mounted() {
    console.log('Sleeping component mounted');
  }
  }
  </script>
  <style scoped>
.good-night-container {
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
}.footer-actions {
  /* border: 2px solid white; */
  position: absolute; 
    bottom: -40px; 
    z-index: 10;
  display: flex;

  left: 50%;
  transform: translate(-50%, -50%);

  /* width: 100%; */
  align-items: start;
  gap: 160px;
  font-size: 15px;
  font-weight: 400;
  white-space: nowrap;
}
  
  .background-image {
    position: absolute;
    inset: 0;
    height: 100%;
    width: 100%;
    object-fit: cover;
    object-position: center;
  }
  .moon{
    top: 53%;
  left: 50%;
  text-align: center;
  transform: translate(-50%, -50%);
    position: absolute;
    margin: 0;
    width: 200px;
    height: 200px;
    z-index: 1;
  }
  .top-image {
    aspect-ratio: 9.09;
    object-fit: auto;
    object-position: center;
    width: 344px;
  }
  
  .header {
    position: relative;
    margin-top: 71px;
    text-align: center;
  }
  
  .greeting {
    font: 800 24px 'CustomFont', sans-serif;
  }
  
  .time {
    margin-top: 15px;
    
    font: 900 64px 'CustomFont', sans-serif;
  }
  
  .status-message {
    top: 68%;
  left: 50%;
  text-align: center;
  transform: translate(-50%, -50%);
    position: absolute;
    margin-top: 27px;
   
    font: 300 20px 'CustomFont', sans-serif;
  }
  
  .breathing-image {
    aspect-ratio: 0.99;
    object-fit: auto;
    object-position: center;
    width: 216px;
    margin-top: 57px;
    max-width: 100%;
  }
  
  .stop-recording-btn {
    top: 80%;
  left: 50%;
  text-align: center;
  transform: translate(-50%, -50%);
    position: absolute;
    -webkit-text-stroke: 1px rgba(0, 0, 0, 0.3);
    border: 1px solid rgba(0, 0, 0, 0.3);
    border-radius: 30px;
    background-color: #000;
    box-shadow: 0 4px 4px rgba(0, 0, 0, 0.25);
    align-self: stretch;
    margin-top: 5px;
    text-align: center;
    padding: 30px 60px;
    font: 700 24px 'CustomFont', sans-serif;
    color: #fff;
    text-align: center;
    white-space: nowrap;
    cursor: pointer;
    
  }
  
  .navigation {
    position: relative;
    align-self: stretch;
    display: flex;
    margin-top: 52px;
    gap: 20px;
    font-size: 15px;
    font-weight: 400;
  }
  
  .nav-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    flex: 1;
  }
  
  .nav-icon {
    width: 38px;
    height: auto;
  }
  
  .nav-text {
    font-family: 'CustomFont', sans-serif;
    margin-top: 5px;
  }
  </style>