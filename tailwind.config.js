const { colors, fontFamily } = require('tailwindcss/defaultTheme')

module.exports = {
  purge: ['./public/*.html', './public/**/*.html'],
  mode: 'jit',
  theme: {
    minHeight: {
      0: '0',
      '1/4': '25%',
      '1/2': '50%',
      '3/4': '75%',
      full: '100%',
      1200: '1200px',
    },
    extend: {
      screens: {
        portrait: { raw: '(orientation: portrait)' },
        portraitmd: { raw: '(orientation: portrait) and (min-width: 768px)' },
      },
      fontFamily: {
        mono: ['Meslo', ...fontFamily.mono],
      },
      keyframes: {
        top450: {
          '0%, 30%, 100%': { top: '0', opacity: '0' },
          '40%, 90%': { top: '450px', opacity: '1' },
          '95%': { top: '450px', opacity: '0' },
        },
        showat50: {
          '0%, 35%, 100%': { opacity: '0' },
          '40%, 95%': { opacity: '1' },
        },
        showat75: {
          '0%, 67%, 100%': { opacity: '0' },
          '70%, 95%': { opacity: '1' },
        },
        scaleinout: {
          '0%, 5%, 65%, 100%': { transform: 'scale(1) translateY(0)' },
          '10%, 60%': { transform: 'scale(2.3) translateY(40px)' },
        },
        fadeinoutfirst: {
          '0%, 50%': { opacity: '0' },
          '25%, 45%': { opacity: '1' },
        },
        fadeinoutsecond: {
          '50%, 100%': { opacity: '0' },
          '75%, 95%': { opacity: '1' },
        },
        fadeinout: {
          '0%, 100%': { opacity: '0' },
          '30%, 80%': { opacity: '1' },
        },
        fadeinoutfast: {
          '0%, 100%': { opacity: '0' },
          '30%, 90%': { opacity: '1' },
        },
        fadeinoutstep: {
          '0%, 100%': { opacity: '0' },
          '5%, 95%': { opacity: '0' },
          '10%, 90%': { opacity: '0.35' },
          '20%, 80%': { opacity: '0.35' },
          '25%, 75%': { opacity: '0.65' },
          '35%, 65%': { opacity: '0.65' },
          '40%, 60%': { opacity: '1' },
        },
        darkinout: {
          '0%, 100%': { 'filter': 'brightness(1)' },
          '50%': { 'filter': 'brightness(0.2)' },
        },
      },
      animation: {
        top450: 'top450 8s ease-out 3s infinite',
        showat50: 'showat50 8s ease-in-out 3s infinite',
        showat75: 'showat75 8s ease-in-out 3s infinite',
        fadeinout: 'fadeinout 10s ease-in-out 3s infinite',
        fadeinoutfirst: 'fadeinoutfirst 10s ease-in-out 3s infinite',
        fadeinoutsecond: 'fadeinoutsecond 10s ease-in-out 3s infinite',
        fadeinoutfast: 'fadeinoutfast 10s ease-in-out 3s infinite',
        scaleinout: 'scaleinout 8s ease-out 3s infinite',
        fadeinoutstep: 'fadeinoutstep 10s ease-in-out 3s infinite',
        darkinout: 'darkinout 5s ease-in-out infinite',
      },
      colors: {
        "white-warm": '#FFEAD7',
        yellow: {
          ...colors.yellow,
          lunar: '#FFD586',
          bright: '#FFB500',
          sunflower: '#F7CE68',
        },
        orange: {
          ...colors.orange,
          bright: '#F96332',
          peach: '#FBAB7E',
          bmac: '#ff813f',
        },
        red: {
          ...colors.red,
          bright: '#F23343',
          hot: '#FF1536',
          mars: '#862833',
          dull: '#C75764',
        },
        pink: {
          ...colors.pink,
          magenta: '#E14283',
          magentish: '#811a4c',
        },
        maroon: '#aa9483',
        sepia: '#B97F64',
        mauve: {
          default: '#312A4C',
          gray: '#3E385B',
          lightgray: '#40365d',
          darkgray: '#292837',
          dark: '#291B3B',
          blackish: '#120d13',
          black: '#1E1D22',
        },
        green: {
          ...colors.green,
          spotify: '#70B069',
          weird: '#46BD62',
          muted: '#54D381',
        },
        blue: {
          ...colors.blue,
          calm: '#6488B9',
          gray: '#B1B2DD',
          muted: '#2977FF',
          facebook: '#3B5998',
          twitter: '#1DA1F2',
          linkedin: '#0077b5',
          dark: '#050129',
        },
        github: '#ffffff',
        reddit: '#FF4500',
      },
    },
  },
  variants: {},
  plugins: [],
}
