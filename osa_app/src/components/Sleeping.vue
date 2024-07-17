<template>
    <div class="good-night-container">
      <img loading="lazy" src="https://cdn.builder.io/api/v1/image/assets/TEMP/f8b3c38ac465a7bc7a71441f87d388fb98da3154f1d74ea3f1e940c5c18ceaf1?apiKey=167f8969fc9e4702b2c941ecb34dd7f8&" class="background-image" alt="" />
      <img loading="lazy" src="https://cdn.builder.io/api/v1/image/assets/TEMP/54afc3a23b4a729daee8341f9d60916b27cadf4fc0b646680ad1a9ee2326274d?apiKey=167f8969fc9e4702b2c941ecb34dd7f8&" class="top-image" alt="" />
      <header class="header">
        <h1 class="greeting">Good Night</h1>
        <p class="time">23:30</p>
      </header>
      <main>
        <p class="status-message">ระบบกำลังบันทึกอุณหภูมิขณะหายใจ</p>
        <img loading="lazy" src="https://cdn.builder.io/api/v1/image/assets/TEMP/b6716f6ccbb1c1d439e547792df58a0aa51bd9f1a0c2abe344ba68116c06896f?apiKey=167f8969fc9e4702b2c941ecb34dd7f8&" class="breathing-image" alt="Breathing visualization" />
        <button class="stop-recording-btn">หยุดบันทึกการหายใจ</button>
      </main>
      <footer class="navigation">
        <nav class="nav-item">
          <img loading="lazy" src="https://cdn.builder.io/api/v1/image/assets/TEMP/af64d9e061af55f3ffd053a886d5a6f2ca356878e33124188eab4780a9ae0bdc?apiKey=167f8969fc9e4702b2c941ecb34dd7f8&" class="nav-icon" alt="" />
          <span class="nav-text">การหายใจ</span>
        </nav>
        <nav class="nav-item">
          <img loading="lazy" src="https://cdn.builder.io/api/v1/image/assets/TEMP/55dcbbc5fdda874426f3fb73935fe657dbaa862496e944d8997a2167c0f31605?apiKey=167f8969fc9e4702b2c941ecb34dd7f8&" class="nav-icon" alt="" />
          <span class="nav-text">สถิติ</span>
        </nav>
      </footer>
    </div>
  </template>
  
  <style scoped>
  .good-night-container {
    display: flex;
    flex-direction: column;
    overflow: hidden;
    position: relative;
    aspect-ratio: 0.46;
    max-width: 480px;
    width: 100%;
    align-items: center;
    color: #fff;
    margin: 0 auto;
    padding: 37px 26px;
  }
  
  .background-image {
    position: absolute;
    inset: 0;
    height: 100%;
    width: 100%;
    object-fit: cover;
    object-position: center;
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
    font: 800 24px Rubik, sans-serif;
  }
  
  .time {
    margin-top: 15px;
    font: 900 64px Rubik, sans-serif;
  }
  
  .status-message {
    position: relative;
    margin-top: 27px;
    font: 300 20px Rubik, sans-serif;
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
    position: relative;
    -webkit-text-stroke: 1px rgba(0, 0, 0, 0.3);
    border: 1px solid rgba(0, 0, 0, 0.3);
    border-radius: 30px;
    background-color: #000;
    box-shadow: 0 4px 4px rgba(0, 0, 0, 0.25);
    align-self: stretch;
    margin-top: 54px;
    padding: 30px 60px;
    font: 700 24px Rubik, sans-serif;
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
    font-family: Rubik, sans-serif;
    margin-top: 5px;
  }
  </style>