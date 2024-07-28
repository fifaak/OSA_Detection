<!-- Home.vue -->
<template>
  <div class="good-night-container">
    <img loading="lazy" src="https://cdn.builder.io/api/v1/image/assets/TEMP/f8b3c38ac465a7bc7a71441f87d388fb98da3154f1d74ea3f1e940c5c18ceaf1?apiKey=167f8969fc9e4702b2c941ecb34dd7f8&" class="background-image" alt="" />
    <img loading="lazy" src="https://cdn.builder.io/api/v1/image/assets/TEMP/54afc3a23b4a729daee8341f9d60916b27cadf4fc0b646680ad1a9ee2326274d?apiKey=167f8969fc9e4702b2c941ecb34dd7f8&" class="top-image" alt="" @click="navigateToLogin" />
    <header class="greeting-header">
      <h1 class="greeting-text">{{ greeting }}</h1>
      <p class="time-display">{{ formattedTime }} น.</p>
    </header>
    <main class="main-content">
      <section class="sleep-start-section" @click="navigateToSleeping">
        <img loading="lazy" src="https://cdn.builder.io/api/v1/image/assets/TEMP/d2d95dc68ad82486c0a84439e3cdfc1d5b8de6bcb3f140154d61f9e3090e3cd8?apiKey=167f8969fc9e4702b2c941ecb34dd7f8&" class="sleep-icon" alt="Sleep icon" />
        <p class="sleep-text">เริ่มนอน</p>
      <!-- </section> -->
      <!-- <section class="sensor-selector"> -->
        <!-- <p id="connection_type"> -->
          <!-- <input type="radio" id="ble" name="type" value="1" checked> -->
          <!-- <label id="ble_label" for="ble">Bluetooth</label> -->
          <!-- <input type="radio" id="usb" name="type" value="0"> -->
          <!-- <label id="usb_label" for="usb">USB</label><br> -->
        <!-- </p> -->
        <!-- <button id="select_device" @click="selectDevice">Select a Go Direct Device</button> -->
        <!-- <div id="error" v-html="error"></div> -->
        <!-- <pre id="output">{{ output }}</pre> -->
      </section>
      <footer class="footer-actions">
        <div class="action-item">
          <img loading="lazy" src="../assets/Home.png" class="action-icon" alt="Breathing icon" />
        </div>
        <div class="action-item">
          <img loading="lazy" @click="navigateToDashboard" src="https://cdn.builder.io/api/v1/image/assets/TEMP/3608c38c5e37b108fb8646888d62b78880c6511ec2e9b9678d1d6ae4ae6acb29?apiKey=167f8969fc9e4702b2c941ecb34dd7f8&" class="action-icon" alt="Statistics icon" />
        </div>
      </footer>
    </main>
  </div>
</template>

<script>
import { ref, computed, onMounted, onUnmounted } from 'vue';
import { useRouter } from 'vue-router';
import "./Home.css"
export default {
  name: 'SleepingView',
  setup() {
    const router = useRouter();
    const godirect = ref(null);
    const currentTime = ref(new Date());
    const error = ref('');
    const output = ref('');

    const navigateToSleeping = () => {
      router.push('/sleeping');
    };
    const navigateToLogin = () => {
      router.push('/');
    }
    const navigateToDashboard = () => {
      router.push('/dashboard');
    }

    const updateTime = () => {
      currentTime.value = new Date();
    };

    onMounted(async () => {
      updateTime();
      const timer = setInterval(updateTime, 1000);
      onUnmounted(() => clearInterval(timer));

      try {
        const gdModule = await import('@vernier/godirect');
        godirect.value = gdModule.default;
        console.log("Go Direct library loaded:", godirect.value);
        initializeDeviceSupport();
      } catch (err) {
        console.error("Failed to load Go Direct library:", err);
        error.value = "Failed to load Go Direct library";
      }
    });

    const formattedTime = computed(() => {
      const hours = currentTime.value.getHours().toString().padStart(2, '0');
      const minutes = currentTime.value.getMinutes().toString().padStart(2, '0');
      return `${hours}:${minutes}`;
    });

    const greeting = computed(() => {
      const hour = currentTime.value.getHours();
      if (hour >= 5 && hour < 12) return 'Good Morning';
      if (hour >= 12 && hour < 17) return 'Good Afternoon';
      if (hour >= 17 && hour < 21) return 'Good Evening';
      return 'Good Night';
    });

    const initializeDeviceSupport = () => {
      const usbBtn = document.querySelector('#usb');
      const usbLabel = document.querySelector('#usb_label');
      const bleBtn = document.querySelector('#ble');
      const bleLabel = document.querySelector('#ble_label');

      if (navigator.bluetooth && typeof navigator.bluetooth.getAvailability === 'function') {
        navigator.bluetooth.getAvailability().then((available) => {
          if (available) {
            bleLabel.innerHTML = `Bluetooth: RD`;
            console.log("Bluetooth: ready");
          } else {
            bleLabel.innerHTML = `Bluetooth <span style="color:red">Not Available</span>`;
            bleBtn.disabled = true;
          }
        });
      } else {
        bleLabel.innerHTML = `Bluetooth <span style="color:red">Not Supported</span>`;
        bleBtn.disabled = true;
      }

      if (navigator.usb) {
        usbLabel.innerHTML = `USB: RD`;
      } else {
        usbLabel.innerHTML = `USB <span style="color:red">Not Supported</span>`;
        usbBtn.disabled = true;
      }

      if (!navigator.bluetooth && !navigator.usb) {
        document.querySelector('#select_device').style.display = 'none';
      }
    };

    const selectDevice = async () => {
  if (!godirect.value) {
    console.error("Go Direct library not loaded yet");
    error.value = "Go Direct library not loaded yet";
    return;
  }
  const bluetooth = document.querySelector('input[name="type"]:checked').value === "1";
  console.log("clicked");
  error.value = "";
  try {
    let device;
    if (bluetooth) {
      device = await godirect.value.selectDevice();
    } else {
      device = await godirect.value.selectDevice({ usb: true });
    }

    if (device) {
      // Check if the device is already open
      if (device.isConnected) {
        console.log(`Device ${device.name} is already connected. Disconnecting...`);
        await device.close();
        console.log(`Device ${device.name} disconnected.`);
      }

      output.value += `\n Connected to ${device.name}`;
      output.value += `\n Reading measurements \n`;

      try {
        await device.open();
      } catch (openError) {
        if (openError.message.includes('already open')) {
          console.log(`Device ${device.name} was already open. Proceeding with existing connection.`);
        } else {
          throw openError;
        }
      }

      device.on('device-closed', () => {
        output.value += `\n\n Disconnected from ${device.name}\n`;
      });

      const sensorDataHandler = (sensor) => {
        const currentTimestamp = new Date();
        const timeString = `${currentTimestamp.getHours().toString().padStart(2, '0')}:${currentTimestamp.getMinutes().toString().padStart(2, '0')}:${currentTimestamp.getSeconds().toString().padStart(2, '0')}`;
        console.log(`Sensor: ${sensor.name} value: ${sensor.value} units: ${sensor.unit}`);
        output.value += `\n Time: ${timeString}, Sensor: ${sensor.name} value: ${sensor.value} units: ${sensor.unit}`;
      };

      device.sensors.forEach(sensor => {
        sensor.setEnabled(true);
      });

      const intervalId = setInterval(() => {
        device.sensors.forEach(sensor => {
          sensorDataHandler(sensor);
        });
      }, 500); // Sample every 0.5 seconds

      onUnmounted(() => clearInterval(intervalId));
    } else {
      error.value = "No device found";
    }
  } catch (err) {
    console.error(err);
    error.value += "\n " + err;
    if (err.toString().includes('cross-origin')) {
      error.value += '\n<p><b>Are you running in an embedded iframe? Try running this example in its own window.</b></p>';
    }
  }
};


    return {
      formattedTime,
      greeting,
      navigateToSleeping,
      navigateToLogin,
      navigateToDashboard,
      selectDevice,
      error,
      output
    };
  }
};
</script>

