/** @type {import('tailwindcss').Config} */
module.exports = {

  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    colors: {
      "light-primary": "#f8fafc",
      "dark-primary": "#1e293b",
      "light-secondary": "#94a3b8",
      "dark-secondary": "#e2e8f0",

      "white": "#ffffff",
      "black": "#000000",
      "green": "#22c55e",
      "gray-200": "#e5e7eb"
    },
    extend: {},
  },
  plugins: [],
}
