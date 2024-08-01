module.exports = {
  content: ['./templates/**/*.html',
  '**/templates/**/*.html'],
  theme: {
    extend: {

      container: {
          center: true,
          padding: {
            DEFAULT: "1rem",
            lg: "0.625rem", 
          }
      },
    
      fontFamily: {
          "Vazir": "Vazir",
          "VazirBold": "Vazir Bold",
      },

    },

  },
  plugins: [],
}
