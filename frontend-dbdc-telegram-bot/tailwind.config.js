/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    screens: {
      'xs': '320px',   // small mobile
      'sm': '375px',   // regular mobile
      'ml': '430px',   // large mobile / small tablet
      'md': '640px',   // tablet
      'lg': '768px',   // large tablet / laptop
      'xl': '1024px',  // desktop
      '2xl': '1280px', // large desktop
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
