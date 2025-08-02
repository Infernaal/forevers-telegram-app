/** @type {import('tailwindcss').Config} */
export default {
  darkMode: 'class',
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    screens: {
      'xs': '375px',
      'sm': '640px',
      'md': '768px',
      'lg': '1024px',
      'xl': '1280px',
      '2xl': '1536px',
    },
    extend: {
      colors: {
        'dbd-primary': '#2019CE',
        'dbd-orange': '#FF6800',
        'dbd-dark': '#02070E',
        'dbd-gray': '#4B4D50',
        'dbd-light-gray': '#7E7E7E',
        'dbd-off-white': '#FAFAFA',
        'dbd-light-blue': '#EFEEFF',
        'dbd-light-orange': '#FFF3E7',
      },
      fontFamily: {
        'montserrat': ['Montserrat', 'system-ui', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'Helvetica Neue', 'Arial', 'sans-serif'],
        'sans': ['Montserrat', 'system-ui', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'Helvetica Neue', 'Arial', 'sans-serif'],
      }
    },
  },
  plugins: [],
}
