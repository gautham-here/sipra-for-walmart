/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        primary: "#0053e2",
        yellow: "#ffc220",
        lightblue: "#65c5f5",
      },
    },
  },
  plugins: [],
};