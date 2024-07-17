<template>
    <div class="chart-container">
      <canvas ref="chartCanvas"></canvas>
    </div>
  </template>
  
  <script>
  import { ref, onMounted } from 'vue';
  import Chart from 'chart.js/auto';
  
  export default {
    name: 'TemperatureChart',
    setup() {
      const chartCanvas = ref(null);
      let chart = null;
  
      onMounted(() => {
        const ctx = chartCanvas.value.getContext('2d');
        chart = new Chart(ctx, {
          type: 'line',
          data: {
            labels: [],
            datasets: [{
              label: 'Temperature',
              data: [],
              borderColor: '#f87979',
              tension: 0.5
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
              x: {
                type: 'linear',
                position: 'bottom',
                title: {
                  display: true,
                  text: 'Time (seconds)'
                }
              },
              y: {
                title: {
                  display: true,
                  text: 'Temperature'
                }
              }
            }
          }
        });
      });
  
      const updateChartData = (time, temperature) => {
        if (chart) {
          chart.data.labels.push(time);
          chart.data.datasets[0].data.push(temperature);
  
          if (parseFloat(time)>5) {
            //   chart.data.datasets[0].data.shift();
              chart.data.labels.shift();
          }
  
          chart.update();
        }
      };
  
      return { chartCanvas, updateChartData };
    }
  };
  </script>
  
  <style scoped>
  .chart-container {
    height: 400px;
  }
  </style>