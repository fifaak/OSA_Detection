<template>
    <div class="sos-alert">
      <img loading="lazy" src="https://cdn.builder.io/api/v1/image/assets/TEMP/9452a1ddf71b262acb33814e6c34f332bc9a99a3d4fc21eef5a71740e4b3aa2a?apiKey=167f8969fc9e4702b2c941ecb34dd7f8&" class="background-image" alt="Emergency background" />
      <header class="alert-header">
        <h1 class="alert-title">SOS</h1>
        <p class="alert-message">คุณหยุดหายใจเกิน 50 วินาที !</p>
        <p class="alert-severity">ระดับ วิกฤต</p>
      </header>
      <main class="alert-main">
        <button class="confirm-button">ยืนยัน ช่วยสำเร็จ</button>
        <p class="system-message">
          <span class="light-text">ระบบกำลังติดต่อ</span><br />ข้อความช่วยเหลือ
        </p>
      </main>
      <footer class="contact-list">
        <div class="contact-item">
          <img loading="lazy" src="https://cdn.builder.io/api/v1/image/assets/TEMP/c9a48952e69ede8f00a7276db538059ced8692dda0ecceceedf8745fde4bb785?apiKey=167f8969fc9e4702b2c941ecb34dd7f8&" class="contact-image" alt="Daughter's contact" />
          <p class="contact-label">ลูกสาว</p>
        </div>
        <div class="contact-item">
          <img loading="lazy" src="https://cdn.builder.io/api/v1/image/assets/TEMP/b9064bfe9bf592cff08f5ca645f064e18c1daddf0d5ce16388a494d0268dbdc1?apiKey=167f8969fc9e4702b2c941ecb34dd7f8&" class="contact-image" alt="Son's contact" />
          <p class="contact-label">ลูกชาย</p>
        </div>
      </footer>
    </div>
  </template>
  
  <style scoped>
  .sos-alert {
    display: flex;
    flex-direction: column;
    overflow: hidden;
    border: 1px solid #000;
    position: relative;
    aspect-ratio: 0.46;
    max-width: 480px;
    width: 100%;
    align-items: center;
    font-size: 24px;
    color: #fff;
    margin: 0 auto;
    padding: 80px 34px 22px;
  }
  
  .background-image {
    position: absolute;
    inset: 0;
    height: 100%;
    width: 100%;
    object-fit: cover;
    object-position: center;
  }
  
  .alert-header {
    position: relative;
    text-align: center;
  }
  
  .alert-title {
    -webkit-text-stroke: 5px #000;
    border: 5px solid #000;
    margin-top: 183px;
    font: 400 96px Spinnaker, sans-serif;
  }
  
  .alert-message {
    color: rgba(255, 255, 255, 0.7);
    font: 600 24px Rubik, sans-serif;
    margin-top: 36px;
  }
  
  .alert-severity {
    color: #fc0;
    font: 900 36px Rubik, sans-serif;
    margin-top: 7px;
  }
  
  .alert-main {
    position: relative;
    width: 100%;
  }
  
  .confirm-button {
    -webkit-text-stroke: 1px rgba(0, 0, 0, 0.3);
    font: 700 24px Rubik, sans-serif;
    border: 1px solid rgba(0, 0, 0, 0.3);
    border-radius: 30px;
    background-color: #000;
    box-shadow: 0 4px 4px rgba(0, 0, 0, 0.25);
    width: 100%;
    margin-top: 71px;
    padding: 32px 60px;
    color: #fff;
    cursor: pointer;
  }
  
  .system-message {
    text-align: center;
    font: 600 24px Rubik, sans-serif;
    margin-top: 90px;
    width: 295px;
  }
  
  .light-text {
    font-weight: 300;
  }
  
  .contact-list {
    display: flex;
    margin-top: 24px;
    gap: 20px;
    font-size: 13px;
    color: #fc0;
  }
  
  .contact-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    flex: 1;
  }
  
  .contact-image {
    width: 46px;
    aspect-ratio: 1;
    object-fit: cover;
    box-shadow: 0 4px 4px rgba(0, 0, 0, 0.25);
  }
  
  .contact-label {
    font: 300 13px Rubik, sans-serif;
    margin-top: 10px;
  }
  </style>