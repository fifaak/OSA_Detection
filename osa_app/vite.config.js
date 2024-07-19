import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  pwa: {
    iconPaths: {
      favicon32: '/osa_app/src/assets/S__4423684 1.png',
      favicon16: '/osa_app/src/assets/S__4423684 1.png',
      appleTouchIcon: '/osa_app/src/assets/S__4423684 1.png',
      maskIcon: '/osa_app/src/assets/S__4423684 1.png',
      msTileImage: '/osa_app/src/assets/S__4423684 1.png'
    }
  }
})
