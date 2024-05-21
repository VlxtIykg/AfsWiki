/** @type {import('tailwindcss').Config} */
const colors = require('tailwindcss/colors')
export default {
	content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    screens: {
      sm: '480px',
      md: '768px',
      lg: '976px',
      xl: '1440px',
    },
    colors: {
			white: colors.white,
      gray: colors.slate,
      green: colors.emerald,
      purple: colors.violet,
      yellow: colors.amber,
			orange: colors.orange,
      black: {
				DEFAULT: "#000"
			},
			pink: {
				'50': '#fdf4ff',
				'100': '#fae8ff',
				'200': '#f5d0fe',
				'300': '#f0abfc',
				'400': '#e879f9',
				'500': '#d946ef',
				'600': '#c026d3',
				'700': '#a21caf',
				'800': '#86198f',
				'900': '#701a75',
				'950': '#4a044e',
				DEFAULT: '#500724'
			},
			default: '#0f172a',
    },
    fontFamily: {
      sans: ['Graphik', 'sans-serif'],
      serif: ['Merriweather', 'serif'],
    },
    extend: {
      spacing: {
        '128': '32rem',
        '144': '36rem',
      },
      borderRadius: {
        '4xl': '2rem',
      },
			fontFamily: {
        display: 'Oswald, ui-serif', // Adds a new `font-display` class
      },
			colors: {
				black: {
					background: '#0f172a',
				},
			},
    }
	},
	plugins: [],
}
