<template>
  <div class="good-night-container">
    <img loading="lazy" src="https://cdn.builder.io/api/v1/image/assets/TEMP/f8b3c38ac465a7bc7a71441f87d388fb98da3154f1d74ea3f1e940c5c18ceaf1?apiKey=167f8969fc9e4702b2c941ecb34dd7f8&" class="background-image" alt="" />
    <img loading="lazy" src="https://cdn.builder.io/api/v1/image/assets/TEMP/54afc3a23b4a729daee8341f9d60916b27cadf4fc0b646680ad1a9ee2326274d?apiKey=167f8969fc9e4702b2c941ecb34dd7f8&" class="top-image" alt="" />
    <img class="moon" src="../assets/moon.png" alt="">
    <header class="header">
      <p class="time">{{ formattedTime }}</p>
    </header>
    <main>
      <p class="status-message" v-html="formattedElapsedTime"></p>
      <button class="stop-recording-btn" @click="stopTimer">ยืนยันการตื่นนอน</button>
      <button @click="startSampling" class="start-recording-btn" style="z-index: 1;">เริ่มนอน</button>
      
      <section class="sensor-selector">
        <p id="connection_type">
          <input type="radio" id="ble" name="type" value="1" checked>
          <!-- <label id="ble_label" for="ble">Bluetooth</label> -->
          <!-- <input type="radio" id="usb" name="type" value="0"> -->
          <!-- <label id="usb_label" for="usb">USB</label><br> -->
        </p>
        <button id="select_device" @click="selectDevice">
          <img src="../assets/search.png" width="100%" alt="">
        </button>
        <!-- <div id="error" v-html="error"></div> -->
        <pre id="output">{{ output }}</pre>
        <!-- <p id="result">{{ result }}</p> -->
      </section>
    </main>
    <!-- <button class="test_btn" @click="navigateToAlert">test alert</button> -->
  </div>
</template>

<script>
import { ref, onMounted, onUnmounted, computed } from 'vue';
import router from '../router';
import axios from 'axios';
import "./Sleeping.css";

export default {
  name: 'Sleeping',
  setup() {
    const currentTime = ref(new Date());
    const startTime = ref(null);
    const elapsedTime = ref(0);
    const error = ref('');
    const output = ref('');
    const result = ref('');
    const godirect = ref(null);
    let device = null;
    let samplingInterval = null;
    let predictionInterval = null;
    const sensorData = ref([]);

    const startRecordingBtn = ref(null);

    const updateTime = () => {
      currentTime.value = new Date();
      if (startTime.value) {
        elapsedTime.value = Math.floor((currentTime.value - startTime.value) / 1000);
      }
    };

    const formattedTime = computed(() => {
      const hours = currentTime.value.getHours().toString().padStart(2, '0');
      const minutes = currentTime.value.getMinutes().toString().padStart(2, '0');
      return `${hours}:${minutes}น.`;
    });

    const formattedElapsedTime = computed(() => {
      const hours = Math.floor(elapsedTime.value / 3600);
      const minutes = Math.floor((elapsedTime.value % 3600) / 60);
      const seconds = elapsedTime.value % 60;
      return `นอน ${hours} ชม. <br> ${minutes} นาที : ${seconds}วินาที`;
    });

    let timer;

    onMounted(async () => {
      console.log('Sleeping component mounted');
      timer = setInterval(updateTime, 1000);

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

    onUnmounted(() => {
      clearInterval(timer);
      if (samplingInterval) {
        clearInterval(samplingInterval);
      }
      if (predictionInterval) {
        clearInterval(predictionInterval);
      }
    });

    const navigateToAlert = () => {
      router.push('/Alert1');
    };

    const stopTimer = () => {
      clearInterval(timer);
      if (samplingInterval) {
        clearInterval(samplingInterval);
      }
      if (predictionInterval) {
        clearInterval(predictionInterval);
      }
      saveToCSV();
      sendSensorData();
      router.push('/Dashboard');
    };

    const initializeDeviceSupport = () => {
      const usbBtn = document.querySelector('#usb');
      const usbLabel = document.querySelector('#usb_label');
      const bleBtn = document.querySelector('#ble');
      const bleLabel = document.querySelector('#ble_label');

      // Check Bluetooth availability
      if (navigator.bluetooth && typeof navigator.bluetooth.getAvailability === 'function') {
        navigator.bluetooth.getAvailability().then((available) => {
          if (available) {
            bleLabel.innerHTML = `Bluetooth`;
          } else {
            bleLabel.innerHTML = `Bluetooth <span style="color:red">Not Available</span>`;
            bleBtn.disabled = true;
          }
        }).catch((error) => {
          console.error("Error checking Bluetooth availability:", error);
          bleLabel.innerHTML = `Bluetooth <span style="color:red">Error</span>`;
          bleBtn.disabled = true;
        });
      } else {
        bleLabel.innerHTML = `Bluetooth <span style="color:red">Not Supported</span>`;
        bleBtn.disabled = true;
      }

      // Check USB availability
      if (navigator.usb) {
        usbLabel.innerHTML = `USB`;
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
        if (device && device.isConnected) {
          await device.close();
        }

        if (bluetooth) {
          device = await godirect.value.selectDevice();
        } else {
          device = await godirect.value.selectDevice({ usb: true });
        }

        if (device) {
          output.value += `\nConnected to ${device.name}\n`;

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
            output.value += `\nDisconnected from ${device.name}\n`;
          });

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

    const startSampling = () => {
      console.log("start!!");
      if (!device) {
        error.value = "No device connected. Please select a device first.";
        return;
      }

      startRecordingBtn.value.style.zIndex = '-1';

      startTime.value = new Date();
      sensorData.value = [];

      let seconds = 0;

      const sensorDataHandler = (sensor) => {
        if (sensor.name.toLowerCase().includes('temperature')) {
          seconds += 0.5;
          console.log(`Seconds: ${seconds}, Temperature: ${sensor.value}`);
          sensorData.value.push([seconds.toFixed(1), sensor.value]);
        }
      };

      device.sensors.forEach(sensor => {
        sensor.setEnabled(true);
      });

      samplingInterval = setInterval(() => {
        device.sensors.forEach(sensor => {
          sensorDataHandler(sensor);
        });
      }, 500); // Sample every 0.5 seconds

      predictionInterval = setInterval(() => {
        sendSensorData();
      }, 25000); // Predict every 25 seconds

      onUnmounted(() => {
        clearInterval(samplingInterval);
        clearInterval(predictionInterval);
      });
    };

    const saveToCSV = () => {
      console.log("Downloading CSV");
      const csvContent = "sec,temp\n" + sensorData.value.map(e => e.join(",")).join("\n");
      const blob = new Blob([csvContent], { type: 'text/csv' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.style.display = 'none';
      a.href = url;
      a.download = `sensor_data_${Date.now()}.csv`;
      document.body.appendChild(a);
      a.click();
      URL.revokeObjectURL(url);
    };

    const sendSensorData = async () => {
      console.log("Sending sensor data");
      const csvContent = "sec,temp\n" + sensorData.value.map(e => e.join(",")).join("\n");
      const blob = new Blob([csvContent], { type: 'text/csv' });
      const formData = new FormData();
      formData.append('file', blob, 'sensor_data.csv');
      formData.append('max_length', '51');

      try {
        const response = await axios.post('http://127.0.0.1:5000/predict', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        });

        if (response.status === 200) {
          result.value = `state: ${response.data.state}`;
          if (response.data.state === 'Warning') {
            router.push('/Alert1');
          }
        } else {
          console.error('Error response:', response.data);
          result.value = `Error: ${response.data.error}`;
        }
      } catch (error) {
        console.error('Fetch error:', error);
        if (error.response) {
          console.error('Response data:', error.response.data);
          console.error('Response status:', error.response.status);
          console.error('Response headers:', error.response.headers);
        } else if (error.request) {
          console.error('Request data:', error.request);
        } else {
          console.error('Error message:', error.message);
        }
        result.value = `Fetch error: ${error.message}`;
      }

      // Retain only the last 25 seconds of data
      const last25SecondsData = sensorData.value.slice(-50); // 50 samples for 25 seconds
      sensorData.value = last25SecondsData;
    };

    return {
      formattedTime,
      formattedElapsedTime,
      stopTimer,
      navigateToAlert,
      selectDevice,
      startSampling,
      error,
      output,
      result,
      startRecordingBtn,
    };
  }
};
</script>

<style>
/* Add some styling to make sure result area is visible */
#result {
  font-size: 18px;
  font-weight: bold;
  color: green;
  padding: 10px;
  border: 1px solid #ddd;
  margin-top: 20px;
  display: inline-block;
}
#error {
  color: red;
  font-weight: bold;
}
</style>
