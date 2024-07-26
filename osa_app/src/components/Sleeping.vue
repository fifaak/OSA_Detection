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
      
      <section class="sensor-selector">
        <p id="connection_type">
          <input type="radio" id="ble" name="type" value="1" checked>
          <label id="ble_label" for="ble">Bluetooth</label>
          <input type="radio" id="usb" name="type" value="0">
          <label id="usb_label" for="usb">USB</label><br>
        </p>
        <button id="select_device" @click="selectDevice">Select a Go Direct Device</button>
        <div id="error" v-html="error"></div>
        <pre id="output">{{ output }}</pre>
        <button @click="startSampling" style="padding: 10px;z-index: 30;cursor: pointer;">Start Sampling</button>
      </section>
      
    </main>
    <button class="test_btn" @click="navigateToAlert">test alert</button>
  </div>
</template>

<script>
import { ref, onMounted, onUnmounted, computed } from 'vue';
import router from '../router';
import "./Sleeping.css"

export default {
  name: 'Sleeping',
  setup() {
    const currentTime = ref(new Date());
    const startTime = ref(null);
    const elapsedTime = ref(0);
    const error = ref('');
    const output = ref('');
    const godirect = ref(null);
    let device = null;
    let samplingInterval = null;
    const data = [];

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
    });

    const navigateToAlert = () => {
      router.push('/Alert1');
    };

    const saveToCSV = () => {
      const csvContent = "data:text/csv;charset=utf-8," + data.map(e => e.join(",")).join("\n");
      const encodedUri = encodeURI(csvContent);
      const link = document.createElement("a");
      link.setAttribute("href", encodedUri);
      link.setAttribute("download", "sensor_data.csv");
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    };

    const stopTimer = () => {
      clearInterval(timer);
      if (samplingInterval) {
        clearInterval(samplingInterval);
        saveToCSV();
      }
      router.push('/Dashboard');
    };

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

      startTime.value = new Date();

      const headers = ["Timestamp", "Seconds", "Temperature"];
      data.push(headers);

      let seconds = 0;

      const sensorDataHandler = (sensor) => {
        if (sensor.name.toLowerCase().includes('temperature')) {
          const currentTimestamp = new Date().toISOString();
          seconds += 0.5;
          console.log(`Timestamp: ${currentTimestamp}, Seconds: ${seconds}, Temperature: ${sensor.value}`);
          data.push([currentTimestamp, seconds.toFixed(1), sensor.value]);
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

      onUnmounted(() => clearInterval(samplingInterval));
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
    };
  }
}
</script>
