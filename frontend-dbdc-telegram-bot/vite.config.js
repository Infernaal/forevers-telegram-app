import { fileURLToPath, URL } from 'node:url'
import { defineConfig, loadEnv } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'

export default defineConfig(({ mode }) => {
  // Загружаем переменные окружения из корневой директории
  const env = loadEnv(mode, process.cwd() + '/../', '')
  
  return {
    plugins: [
      vue(),
      vueDevTools(),
    ],
    resolve: {
      alias: {
        '@': fileURLToPath(new URL('./src', import.meta.url))
      },
    },
    define: {
      // Передаем переменные окружения в клиентский код
      'import.meta.env.VITE_TELEGRAM_BOT_NAME': JSON.stringify(env.TELEGRAM_BOT_NAME || 'dbdc_test_bot'),
      'import.meta.env.VITE_API_BASE_URL': JSON.stringify(env.VITE_API_BASE_URL || 'https://dbdc-mini.dubadu.com/api/v1/dbdc'),
    },
    base: './', // важно, если ты деплоишь как статик сайт в подкаталог
    build: {
      assetsDir: 'assets',
      outDir: 'dist',
      rollupOptions: {
        output: {
          entryFileNames: `assets/[name]-[hash].js`,
          chunkFileNames: `assets/[name]-[hash].js`,
          assetFileNames: `assets/[name]-[hash][extname]`
        }
      }
    },
    server: {
      // Если ты разрабатываешь и хочешь отключить кэш
      headers: {
        'Cache-Control': 'no-store'
      }
    }
  }
})
