<template>
  <div class="good-night-container">
    <img loading="lazy" src="https://cdn.builder.io/api/v1/image/assets/TEMP/f8b3c38ac465a7bc7a71441f87d388fb98da3154f1d74ea3f1e940c5c18ceaf1?apiKey=167f8969fc9e4702b2c941ecb34dd7f8&" class="background-image" alt="" />
    <img loading="lazy" src="https://cdn.builder.io/api/v1/image/assets/TEMP/54afc3a23b4a729daee8341f9d60916b27cadf4fc0b646680ad1a9ee2326274d?apiKey=167f8969fc9e4702b2c941ecb34dd7f8&" class="top-image" alt="" />
    <header class="greeting-header">
      <h1 class="greeting-text">Good Night</h1>
      <p class="time-display">23:30</p>
    </header>
    <main class="main-content">
      <section class="sleep-start-section">
        <img loading="lazy" src="https://cdn.builder.io/api/v1/image/assets/TEMP/d2d95dc68ad82486c0a84439e3cdfc1d5b8de6bcb3f140154d61f9e3090e3cd8?apiKey=167f8969fc9e4702b2c941ecb34dd7f8&" class="sleep-icon" alt="Sleep icon" />
        <p class="sleep-text">เริ่มนอน</p>
      </section>
      <footer class="footer-actions">
        <div class="action-item">
          <img loading="lazy" src="https://cdn.builder.io/api/v1/image/assets/TEMP/be0156c2384f31ea9ae55796cedf39f1cce6313e4893a5f9fdad6f7973f8c4d0?apiKey=167f8969fc9e4702b2c941ecb34dd7f8&" class="action-icon" alt="Breathing icon" />
          <p class="action-text">การหายใจ</p>
        </div>
        <div class="action-item">
          <img loading="lazy" src="https://cdn.builder.io/api/v1/image/assets/TEMP/3608c38c5e37b108fb8646888d62b78880c6511ec2e9b9678d1d6ae4ae6acb29?apiKey=167f8969fc9e4702b2c941ecb34dd7f8&" class="action-icon" alt="Statistics icon" />
          <p class="action-text">สถิติ</p>
        </div>
      </footer>
    </main>
  </div>
</template>

<script>
import { ref } from 'vue';

export default {
  name: 'LoginForm'
};
</script>


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
  font-weight: 800;
  margin: 0 auto;
  padding: 45px 0;
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
  max-width: 344px;
}

.greeting-header {
  position: relative;
  text-align: center;
  margin-top: 60px;
}

.greeting-text {
  font: 24px Rubik, sans-serif;
}

.time-display {
  text-shadow: 0 4px 4px rgba(0, 0, 0, 0.25);
  align-self: stretch;
  margin-top: 7px;
  width: 100%;
  font: 64px Rubik, sans-serif;
}

.sleep-start-section {
  position: relative;
  border: 5px solid rgba(0, 0, 0, 1);
  box-shadow: 0 4px 4px 0 rgba(0, 0, 0, 0.25) inset;
  background-color: #fff;
  border-radius: 50%;
  display: flex;
  margin-top: 205px;
  width: 230px;
  max-width: 100%;
  flex-direction: column;
  font-size: 32px;
  color: #1e1e1e;
  white-space: nowrap;
  text-align: center;
  padding: 62px 64px;
}

.sleep-icon {
  aspect-ratio: 1.45;
  object-fit: auto;
  object-position: center;
  width: 100%;
  margin-left: 12px;
}

.sleep-text {
  font-family: Rubik, sans-serif;
  margin-top: 14px;
}

.footer-actions {
  position: relative;
  display: flex;
  margin-top: 49px;
  width: 100%;
  max-width: 298px;
  align-items: start;
  gap: 20px;
  font-size: 15px;
  font-weight: 400;
  white-space: nowrap;
}

.action-item {
  display: flex;
  margin-top: 11px;
  flex-direction: column;
  flex: 1;
  padding: 0 20px;
}

.action-icon {
  aspect-ratio: 0.94;
  object-fit: auto;
  object-position: center;
  width: 36px;
  align-self: center;
}

.action-text {
  font-family: Rubik, sans-serif;
  margin-top: 5px;
}
</style>