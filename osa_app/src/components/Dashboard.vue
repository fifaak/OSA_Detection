<template>
    <div class="good-night-container">

        <article class="sleep-statistics">
            <img loading="lazy"
                src="https://cdn.builder.io/api/v1/image/assets/TEMP/f8b3c38ac465a7bc7a71441f87d388fb98da3154f1d74ea3f1e940c5c18ceaf1?apiKey=167f8969fc9e4702b2c941ecb34dd7f8&"
                class="background-image" alt="" />
                <img loading="lazy"
                    src="https://cdn.builder.io/api/v1/image/assets/TEMP/54afc3a23b4a729daee8341f9d60916b27cadf4fc0b646680ad1a9ee2326274d?apiKey=167f8969fc9e4702b2c941ecb34dd7f8&"
                    class="top-image" alt="" @click="navigateToLogin" />
            <header class="header">
                <div class="date-container">
                    <img loading="lazy"
                        src="https://cdn.builder.io/api/v1/image/assets/TEMP/1db51993561da88ead5f71743d011c54dd38338c0bb332ccc6c0f8c47bfb111a?apiKey=167f8969fc9e4702b2c941ecb34dd7f8&"
                        class="calendar-icon" alt="Calendar Icon" />
                    <time class="date">สถิติ : 6 ก.ค. 2567</time>
                </div>
            </header>
            <section class="graph-container"></section>
            <h1 class="graph-title">กราฟแสดงการเปลี่ยนแปลงอุณหภูมิ</h1>
            <section class="statistics-container">
                <p class="content">
                    <span class="label">นอนหลับ: </span>
                    <span class="value">8 ชม</span>.
                </p>
                <p class="content">
                    <span class="label">หยุดหายใจนานสุด: </span>
                    <span class="value">35 วินาที</span>
                </p>
                <p class="content">
                    <span class="label">พบเตือนหยุดหายใจ:</span>
                    <span class="value">1 ครั้ง</span>
                </p>
            </section>
            <footer class="footer-actions">
            <div class="action-item">
              <img loading="lazy" @click="navigrateToHome" src="../assets/Home.png" class="action-icon" alt="Breathing icon" />
              <!-- <p class="action-text">การหายใจ</p> -->
            </div>
            <div class="action-item">
              <img loading="lazy" src="https://cdn.builder.io/api/v1/image/assets/TEMP/3608c38c5e37b108fb8646888d62b78880c6511ec2e9b9678d1d6ae4ae6acb29?apiKey=167f8969fc9e4702b2c941ecb34dd7f8&" class="action-icon" alt="Statistics icon" />
              <!-- <p class="action-text">สถิติ</p> -->
            </div>
          </footer>
        </article>
    </div>
</template>
<script>

import { ref, computed, onMounted, onUnmounted } from 'vue';
import { useRouter } from 'vue-router';
export default {
    name: 'Dashboard',
    setup() {
        const router = useRouter();
        const navigateToLogin = () => {
            router.push('/');
        }
        const navigrateToHome = () =>{
            router.push('/home');
        }
        return {
            navigateToLogin,
            navigrateToHome
        };
    }

}
</script>

<style scoped>
.good-night-container {
  /* padding-top:50px; */
  display: flex;
  flex-direction: column;
  overflow: hidden;
  /* position: absolute; */
  aspect-ratio: 0.46;
  /* max-width: 480px; */
  width: 100%;
  /* padding: 0; */
  align-items: center;
  color: #fff;
  font-weight: 800;
  margin: 0 auto;
  /* border: 2px solid black; */
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
  font-family: 'CustomFont', sans-serif;
  color:white;
  margin-top: 5px;
}
.footer-actions {
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
.top-image{
  position: absolute;
  inset: 0;
  height: auto;
  width: 80%;

  left: 50%;
  top: 8%;
  transform: translate(-50%, -50%);
  /* object-fit: cover; */
  /* object-position: center; */
}
.header {
    position: relative;
    align-self: stretch;
    display: flex;
    width: 100%;
    flex-direction: column;
    /* padding: 0 21px; */
}

.logo {
    aspect-ratio: 9.09;
    object-fit: auto;
    object-position: center;
    width: 348px;
    align-self: center;
}

.date-container {
    display: flex;
    margin-top: 100px;
    gap: 7px;
}

.calendar-icon {
    aspect-ratio: 0.97;
    object-fit: auto;
    object-position: center;
    width: 31px;
}

.date {
    flex-grow: 1;
    flex-basis: auto;
    margin: auto 0;
    color: white;
}



.graph-container {
    position: relative;
    box-shadow: 0 4px 13.3px 0 rgba(0, 0, 0, 0.25);
    background-color: #fff;
    align-self: stretch;
    min-height: 266px;
    margin: auto;
    margin-top: 12px;
    width: 80vw;
    padding:0px;
    border-radius: 30px;
}

.graph-title {
    position: relative;
    text-align: center;
    margin-top: 9px;
    font-size: 16px;
    font-weight: 400;
    color: #cecece;
}

.statistics-container {
    position: relative;
    margin: auto;
    border-radius: 30px;
    background-color: rgba(2, 0, 53, 0.727);
    display: flex;
    /* margin-top: 22px; */
    width: 80%;
    flex-direction: column;
    align-items: start;
    font-size: 20px;
    font-weight: 300;
    padding: 10px 30px;
    color: white;
}


.content {
    margin: 10px;
}

.apnea-duration {
    margin-top: 25px;
}

.apnea-count {
    margin-top: 15px;
}

.value {
    font-weight: 700;
}
.footer-actions {
    /* border: 2px solid white; */
    position: absolute;
    bottom: 20px;
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

.action-item {
  display: flex;
  margin-top: 11px;
  flex-direction: column;
  flex: 1;
  cursor: pointer;
  padding:20px;
  border-radius: 30px;
  background-color: rgba(0, 0, 0, 0.157);
}

.action-icon {
  aspect-ratio: 0.94;
  object-fit: auto;
  object-position: center;
  width: 36px;
  align-self: center;
}

.action-text {
  font-family: 'CustomFont', sans-serif;
  margin-top: 5px;
}

.label {
    font-size: 15px;
    color: rgba(255, 255, 255, 0.626)
}

.value {
    font-size: 15px;
    color: rgb(255, 255, 255)
}
</style>