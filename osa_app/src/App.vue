<!-- App.vue -->
<template>
  <div id="app">
    <h1>Excel Data Stream</h1>
    <table v-if="rows.length">
      <thead>
        <tr>
          <th v-for="(value, key) in rows[0]" :key="key">{{ key }}</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(row, index) in rows" :key="index">
          <td v-for="(value, key) in row" :key="key">{{ value }}</td>
        </tr>
      </tbody>
    </table>
    <p v-else>Waiting for data...</p>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      rows: []
    }
  },
  mounted() {
    this.fetchData()
  },
  methods: {
    async fetchData() {
      try {
        const response = await fetch('http://127.0.0.1:8000/stream')
        const reader = response.body.getReader()
        const decoder = new TextDecoder()

        while (true) {
          const { done, value } = await reader.read()
          if (done) break

          const chunk = decoder.decode(value)
          const lines = chunk.split('\n')

          for (const line of lines) {
            if (line.trim()) {
              const data = JSON.parse(line)
              this.rows.push(data)
            }
          }
        }
      } catch (error) {
        console.error('Error fetching data:', error)
      }
    }
  }
}
</script>

<style>
table {
  border-collapse: collapse;
  width: 100%;
}
th, td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}
th {
  background-color: #f2f2f2;
}
</style>