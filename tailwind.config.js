/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./wardbulletin/main/templates/main/*.html"],
  safelist: [
    { pattern: /bg-(\w+)-(50|100|200|400|600|800)/ },
    { pattern: /border-(\w+)-400/ },
    { pattern: /border-l-(\w+)-400/ },
    { pattern: /border-x-(\w+)-400/ },
    { pattern: /divide-(\w+)-800/ },
    { pattern: /fill-(\w+)-800/ },
    { pattern: /prose-(\w+)/ },
    { pattern: /text-(\w+)-(100|200|600|900)/ },
    { 
      pattern: /text-(\w+)-(50|800)/,
      variants: ['hover']
    },
  ],
  theme: {
    extend: {
      colors: {
        brown: {
          50: '#fdf8f6',
          100: '#f2e8e5',
          200: '#eaddd7',
          300: '#e0cec7',
          400: '#d2bab0',
          500: '#bfa094',
          600: '#a18072',
          700: '#977669',
          800: '#846358',
          900: '#43302b',
        },
      },
      typography: ({ theme }) => ({
        brown: {
          css: {
            '--tw-prose-body': theme('colors.brown[800]'),
            '--tw-prose-headings': theme('colors.brown[900]'),
            '--tw-prose-lead': theme('colors.brown[700]'),
            '--tw-prose-links': theme('colors.brown[900]'),
            '--tw-prose-bold': theme('colors.brown[900]'),
            '--tw-prose-counters': theme('colors.brown[600]'),
            '--tw-prose-bullets': theme('colors.brown[400]'),
            '--tw-prose-hr': theme('colors.brown[300]'),
            '--tw-prose-quotes': theme('colors.brown[900]'),
            '--tw-prose-quote-borders': theme('colors.brown[300]'),
            '--tw-prose-captions': theme('colors.brown[700]'),
            '--tw-prose-code': theme('colors.brown[900]'),
            '--tw-prose-pre-code': theme('colors.brown[100]'),
            '--tw-prose-pre-bg': theme('colors.brown[900]'),
            '--tw-prose-th-borders': theme('colors.brown[300]'),
            '--tw-prose-td-borders': theme('colors.brown[200]'),
            '--tw-prose-invert-body': theme('colors.brown[200]'),
            '--tw-prose-invert-headings': theme('colors.white'),
            '--tw-prose-invert-lead': theme('colors.brown[300]'),
            '--tw-prose-invert-links': theme('colors.white'),
            '--tw-prose-invert-bold': theme('colors.white'),
            '--tw-prose-invert-counters': theme('colors.brown[400]'),
            '--tw-prose-invert-bullets': theme('colors.brown[600]'),
            '--tw-prose-invert-hr': theme('colors.brown[700]'),
            '--tw-prose-invert-quotes': theme('colors.brown[100]'),
            '--tw-prose-invert-quote-borders': theme('colors.brown[700]'),
            '--tw-prose-invert-captions': theme('colors.brown[400]'),
            '--tw-prose-invert-code': theme('colors.white'),
            '--tw-prose-invert-pre-code': theme('colors.brown[300]'),
            '--tw-prose-invert-pre-bg': 'rgb(0 0 0 / 50%)',
            '--tw-prose-invert-th-borders': theme('colors.brown[600]'),
            '--tw-prose-invert-td-borders': theme('colors.brown[700]'),
          }
        },
        red: {
          css: {
            '--tw-prose-body': theme('colors.red[800]'),
            '--tw-prose-headings': theme('colors.red[900]'),
            '--tw-prose-lead': theme('colors.red[700]'),
            '--tw-prose-links': theme('colors.red[900]'),
            '--tw-prose-bold': theme('colors.red[900]'),
            '--tw-prose-counters': theme('colors.red[600]'),
            '--tw-prose-bullets': theme('colors.red[400]'),
            '--tw-prose-hr': theme('colors.red[300]'),
            '--tw-prose-quotes': theme('colors.red[900]'),
            '--tw-prose-quote-borders': theme('colors.red[300]'),
            '--tw-prose-captions': theme('colors.red[700]'),
            '--tw-prose-code': theme('colors.red[900]'),
            '--tw-prose-pre-code': theme('colors.red[100]'),
            '--tw-prose-pre-bg': theme('colors.red[900]'),
            '--tw-prose-th-borders': theme('colors.red[300]'),
            '--tw-prose-td-borders': theme('colors.red[200]'),
            '--tw-prose-invert-body': theme('colors.red[200]'),
            '--tw-prose-invert-headings': theme('colors.white'),
            '--tw-prose-invert-lead': theme('colors.red[300]'),
            '--tw-prose-invert-links': theme('colors.white'),
            '--tw-prose-invert-bold': theme('colors.white'),
            '--tw-prose-invert-counters': theme('colors.red[400]'),
            '--tw-prose-invert-bullets': theme('colors.red[600]'),
            '--tw-prose-invert-hr': theme('colors.red[700]'),
            '--tw-prose-invert-quotes': theme('colors.red[100]'),
            '--tw-prose-invert-quote-borders': theme('colors.red[700]'),
            '--tw-prose-invert-captions': theme('colors.red[400]'),
            '--tw-prose-invert-code': theme('colors.white'),
            '--tw-prose-invert-pre-code': theme('colors.red[300]'),
            '--tw-prose-invert-pre-bg': 'rgb(0 0 0 / 50%)',
            '--tw-prose-invert-th-borders': theme('colors.red[600]'),
            '--tw-prose-invert-td-borders': theme('colors.red[700]'),
          }
        },
        orange: {
          css: {
            '--tw-prose-body': theme('colors.orange[800]'),
            '--tw-prose-headings': theme('colors.orange[900]'),
            '--tw-prose-lead': theme('colors.orange[700]'),
            '--tw-prose-links': theme('colors.orange[900]'),
            '--tw-prose-bold': theme('colors.orange[900]'),
            '--tw-prose-counters': theme('colors.orange[600]'),
            '--tw-prose-bullets': theme('colors.orange[400]'),
            '--tw-prose-hr': theme('colors.orange[300]'),
            '--tw-prose-quotes': theme('colors.orange[900]'),
            '--tw-prose-quote-borders': theme('colors.orange[300]'),
            '--tw-prose-captions': theme('colors.orange[700]'),
            '--tw-prose-code': theme('colors.orange[900]'),
            '--tw-prose-pre-code': theme('colors.orange[100]'),
            '--tw-prose-pre-bg': theme('colors.orange[900]'),
            '--tw-prose-th-borders': theme('colors.orange[300]'),
            '--tw-prose-td-borders': theme('colors.orange[200]'),
            '--tw-prose-invert-body': theme('colors.orange[200]'),
            '--tw-prose-invert-headings': theme('colors.white'),
            '--tw-prose-invert-lead': theme('colors.orange[300]'),
            '--tw-prose-invert-links': theme('colors.white'),
            '--tw-prose-invert-bold': theme('colors.white'),
            '--tw-prose-invert-counters': theme('colors.orange[400]'),
            '--tw-prose-invert-bullets': theme('colors.orange[600]'),
            '--tw-prose-invert-hr': theme('colors.orange[700]'),
            '--tw-prose-invert-quotes': theme('colors.orange[100]'),
            '--tw-prose-invert-quote-borders': theme('colors.orange[700]'),
            '--tw-prose-invert-captions': theme('colors.orange[400]'),
            '--tw-prose-invert-code': theme('colors.white'),
            '--tw-prose-invert-pre-code': theme('colors.orange[300]'),
            '--tw-prose-invert-pre-bg': 'rgb(0 0 0 / 50%)',
            '--tw-prose-invert-th-borders': theme('colors.orange[600]'),
            '--tw-prose-invert-td-borders': theme('colors.orange[700]'),
          }
        },
        amber: {
          css: {
            '--tw-prose-body': theme('colors.amber[800]'),
            '--tw-prose-headings': theme('colors.amber[900]'),
            '--tw-prose-lead': theme('colors.amber[700]'),
            '--tw-prose-links': theme('colors.amber[900]'),
            '--tw-prose-bold': theme('colors.amber[900]'),
            '--tw-prose-counters': theme('colors.amber[600]'),
            '--tw-prose-bullets': theme('colors.amber[400]'),
            '--tw-prose-hr': theme('colors.amber[300]'),
            '--tw-prose-quotes': theme('colors.amber[900]'),
            '--tw-prose-quote-borders': theme('colors.amber[300]'),
            '--tw-prose-captions': theme('colors.amber[700]'),
            '--tw-prose-code': theme('colors.amber[900]'),
            '--tw-prose-pre-code': theme('colors.amber[100]'),
            '--tw-prose-pre-bg': theme('colors.amber[900]'),
            '--tw-prose-th-borders': theme('colors.amber[300]'),
            '--tw-prose-td-borders': theme('colors.amber[200]'),
            '--tw-prose-invert-body': theme('colors.amber[200]'),
            '--tw-prose-invert-headings': theme('colors.white'),
            '--tw-prose-invert-lead': theme('colors.amber[300]'),
            '--tw-prose-invert-links': theme('colors.white'),
            '--tw-prose-invert-bold': theme('colors.white'),
            '--tw-prose-invert-counters': theme('colors.amber[400]'),
            '--tw-prose-invert-bullets': theme('colors.amber[600]'),
            '--tw-prose-invert-hr': theme('colors.amber[700]'),
            '--tw-prose-invert-quotes': theme('colors.amber[100]'),
            '--tw-prose-invert-quote-borders': theme('colors.amber[700]'),
            '--tw-prose-invert-captions': theme('colors.amber[400]'),
            '--tw-prose-invert-code': theme('colors.white'),
            '--tw-prose-invert-pre-code': theme('colors.amber[300]'),
            '--tw-prose-invert-pre-bg': 'rgb(0 0 0 / 50%)',
            '--tw-prose-invert-th-borders': theme('colors.amber[600]'),
            '--tw-prose-invert-td-borders': theme('colors.amber[700]'),
          }
        },
        yellow: {
          css: {
            '--tw-prose-body': theme('colors.yellow[800]'),
            '--tw-prose-headings': theme('colors.yellow[900]'),
            '--tw-prose-lead': theme('colors.yellow[700]'),
            '--tw-prose-links': theme('colors.yellow[900]'),
            '--tw-prose-bold': theme('colors.yellow[900]'),
            '--tw-prose-counters': theme('colors.yellow[600]'),
            '--tw-prose-bullets': theme('colors.yellow[400]'),
            '--tw-prose-hr': theme('colors.yellow[300]'),
            '--tw-prose-quotes': theme('colors.yellow[900]'),
            '--tw-prose-quote-borders': theme('colors.yellow[300]'),
            '--tw-prose-captions': theme('colors.yellow[700]'),
            '--tw-prose-code': theme('colors.yellow[900]'),
            '--tw-prose-pre-code': theme('colors.yellow[100]'),
            '--tw-prose-pre-bg': theme('colors.yellow[900]'),
            '--tw-prose-th-borders': theme('colors.yellow[300]'),
            '--tw-prose-td-borders': theme('colors.yellow[200]'),
            '--tw-prose-invert-body': theme('colors.yellow[200]'),
            '--tw-prose-invert-headings': theme('colors.white'),
            '--tw-prose-invert-lead': theme('colors.yellow[300]'),
            '--tw-prose-invert-links': theme('colors.white'),
            '--tw-prose-invert-bold': theme('colors.white'),
            '--tw-prose-invert-counters': theme('colors.yellow[400]'),
            '--tw-prose-invert-bullets': theme('colors.yellow[600]'),
            '--tw-prose-invert-hr': theme('colors.yellow[700]'),
            '--tw-prose-invert-quotes': theme('colors.yellow[100]'),
            '--tw-prose-invert-quote-borders': theme('colors.yellow[700]'),
            '--tw-prose-invert-captions': theme('colors.yellow[400]'),
            '--tw-prose-invert-code': theme('colors.white'),
            '--tw-prose-invert-pre-code': theme('colors.yellow[300]'),
            '--tw-prose-invert-pre-bg': 'rgb(0 0 0 / 50%)',
            '--tw-prose-invert-th-borders': theme('colors.yellow[600]'),
            '--tw-prose-invert-td-borders': theme('colors.yellow[700]'),
          }
        },
        lime: {
          css: {
            '--tw-prose-body': theme('colors.lime[800]'),
            '--tw-prose-headings': theme('colors.lime[900]'),
            '--tw-prose-lead': theme('colors.lime[700]'),
            '--tw-prose-links': theme('colors.lime[900]'),
            '--tw-prose-bold': theme('colors.lime[900]'),
            '--tw-prose-counters': theme('colors.lime[600]'),
            '--tw-prose-bullets': theme('colors.lime[400]'),
            '--tw-prose-hr': theme('colors.lime[300]'),
            '--tw-prose-quotes': theme('colors.lime[900]'),
            '--tw-prose-quote-borders': theme('colors.lime[300]'),
            '--tw-prose-captions': theme('colors.lime[700]'),
            '--tw-prose-code': theme('colors.lime[900]'),
            '--tw-prose-pre-code': theme('colors.lime[100]'),
            '--tw-prose-pre-bg': theme('colors.lime[900]'),
            '--tw-prose-th-borders': theme('colors.lime[300]'),
            '--tw-prose-td-borders': theme('colors.lime[200]'),
            '--tw-prose-invert-body': theme('colors.lime[200]'),
            '--tw-prose-invert-headings': theme('colors.white'),
            '--tw-prose-invert-lead': theme('colors.lime[300]'),
            '--tw-prose-invert-links': theme('colors.white'),
            '--tw-prose-invert-bold': theme('colors.white'),
            '--tw-prose-invert-counters': theme('colors.lime[400]'),
            '--tw-prose-invert-bullets': theme('colors.lime[600]'),
            '--tw-prose-invert-hr': theme('colors.lime[700]'),
            '--tw-prose-invert-quotes': theme('colors.lime[100]'),
            '--tw-prose-invert-quote-borders': theme('colors.lime[700]'),
            '--tw-prose-invert-captions': theme('colors.lime[400]'),
            '--tw-prose-invert-code': theme('colors.white'),
            '--tw-prose-invert-pre-code': theme('colors.lime[300]'),
            '--tw-prose-invert-pre-bg': 'rgb(0 0 0 / 50%)',
            '--tw-prose-invert-th-borders': theme('colors.lime[600]'),
            '--tw-prose-invert-td-borders': theme('colors.lime[700]'),
          }
        },
        green: {
          css: {
            '--tw-prose-body': theme('colors.green[800]'),
            '--tw-prose-headings': theme('colors.green[900]'),
            '--tw-prose-lead': theme('colors.green[700]'),
            '--tw-prose-links': theme('colors.green[900]'),
            '--tw-prose-bold': theme('colors.green[900]'),
            '--tw-prose-counters': theme('colors.green[600]'),
            '--tw-prose-bullets': theme('colors.green[400]'),
            '--tw-prose-hr': theme('colors.green[300]'),
            '--tw-prose-quotes': theme('colors.green[900]'),
            '--tw-prose-quote-borders': theme('colors.green[300]'),
            '--tw-prose-captions': theme('colors.green[700]'),
            '--tw-prose-code': theme('colors.green[900]'),
            '--tw-prose-pre-code': theme('colors.green[100]'),
            '--tw-prose-pre-bg': theme('colors.green[900]'),
            '--tw-prose-th-borders': theme('colors.green[300]'),
            '--tw-prose-td-borders': theme('colors.green[200]'),
            '--tw-prose-invert-body': theme('colors.green[200]'),
            '--tw-prose-invert-headings': theme('colors.white'),
            '--tw-prose-invert-lead': theme('colors.green[300]'),
            '--tw-prose-invert-links': theme('colors.white'),
            '--tw-prose-invert-bold': theme('colors.white'),
            '--tw-prose-invert-counters': theme('colors.green[400]'),
            '--tw-prose-invert-bullets': theme('colors.green[600]'),
            '--tw-prose-invert-hr': theme('colors.green[700]'),
            '--tw-prose-invert-quotes': theme('colors.green[100]'),
            '--tw-prose-invert-quote-borders': theme('colors.green[700]'),
            '--tw-prose-invert-captions': theme('colors.green[400]'),
            '--tw-prose-invert-code': theme('colors.white'),
            '--tw-prose-invert-pre-code': theme('colors.green[300]'),
            '--tw-prose-invert-pre-bg': 'rgb(0 0 0 / 50%)',
            '--tw-prose-invert-th-borders': theme('colors.green[600]'),
            '--tw-prose-invert-td-borders': theme('colors.green[700]'),
          }
        },
        emerald: {
          css: {
            '--tw-prose-body': theme('colors.emerald[800]'),
            '--tw-prose-headings': theme('colors.emerald[900]'),
            '--tw-prose-lead': theme('colors.emerald[700]'),
            '--tw-prose-links': theme('colors.emerald[900]'),
            '--tw-prose-bold': theme('colors.emerald[900]'),
            '--tw-prose-counters': theme('colors.emerald[600]'),
            '--tw-prose-bullets': theme('colors.emerald[400]'),
            '--tw-prose-hr': theme('colors.emerald[300]'),
            '--tw-prose-quotes': theme('colors.emerald[900]'),
            '--tw-prose-quote-borders': theme('colors.emerald[300]'),
            '--tw-prose-captions': theme('colors.emerald[700]'),
            '--tw-prose-code': theme('colors.emerald[900]'),
            '--tw-prose-pre-code': theme('colors.emerald[100]'),
            '--tw-prose-pre-bg': theme('colors.emerald[900]'),
            '--tw-prose-th-borders': theme('colors.emerald[300]'),
            '--tw-prose-td-borders': theme('colors.emerald[200]'),
            '--tw-prose-invert-body': theme('colors.emerald[200]'),
            '--tw-prose-invert-headings': theme('colors.white'),
            '--tw-prose-invert-lead': theme('colors.emerald[300]'),
            '--tw-prose-invert-links': theme('colors.white'),
            '--tw-prose-invert-bold': theme('colors.white'),
            '--tw-prose-invert-counters': theme('colors.emerald[400]'),
            '--tw-prose-invert-bullets': theme('colors.emerald[600]'),
            '--tw-prose-invert-hr': theme('colors.emerald[700]'),
            '--tw-prose-invert-quotes': theme('colors.emerald[100]'),
            '--tw-prose-invert-quote-borders': theme('colors.emerald[700]'),
            '--tw-prose-invert-captions': theme('colors.emerald[400]'),
            '--tw-prose-invert-code': theme('colors.white'),
            '--tw-prose-invert-pre-code': theme('colors.emerald[300]'),
            '--tw-prose-invert-pre-bg': 'rgb(0 0 0 / 50%)',
            '--tw-prose-invert-th-borders': theme('colors.emerald[600]'),
            '--tw-prose-invert-td-borders': theme('colors.emerald[700]'),
          }
        },
        teal: {
          css: {
            '--tw-prose-body': theme('colors.teal[800]'),
            '--tw-prose-headings': theme('colors.teal[900]'),
            '--tw-prose-lead': theme('colors.teal[700]'),
            '--tw-prose-links': theme('colors.teal[900]'),
            '--tw-prose-bold': theme('colors.teal[900]'),
            '--tw-prose-counters': theme('colors.teal[600]'),
            '--tw-prose-bullets': theme('colors.teal[400]'),
            '--tw-prose-hr': theme('colors.teal[300]'),
            '--tw-prose-quotes': theme('colors.teal[900]'),
            '--tw-prose-quote-borders': theme('colors.teal[300]'),
            '--tw-prose-captions': theme('colors.teal[700]'),
            '--tw-prose-code': theme('colors.teal[900]'),
            '--tw-prose-pre-code': theme('colors.teal[100]'),
            '--tw-prose-pre-bg': theme('colors.teal[900]'),
            '--tw-prose-th-borders': theme('colors.teal[300]'),
            '--tw-prose-td-borders': theme('colors.teal[200]'),
            '--tw-prose-invert-body': theme('colors.teal[200]'),
            '--tw-prose-invert-headings': theme('colors.white'),
            '--tw-prose-invert-lead': theme('colors.teal[300]'),
            '--tw-prose-invert-links': theme('colors.white'),
            '--tw-prose-invert-bold': theme('colors.white'),
            '--tw-prose-invert-counters': theme('colors.teal[400]'),
            '--tw-prose-invert-bullets': theme('colors.teal[600]'),
            '--tw-prose-invert-hr': theme('colors.teal[700]'),
            '--tw-prose-invert-quotes': theme('colors.teal[100]'),
            '--tw-prose-invert-quote-borders': theme('colors.teal[700]'),
            '--tw-prose-invert-captions': theme('colors.teal[400]'),
            '--tw-prose-invert-code': theme('colors.white'),
            '--tw-prose-invert-pre-code': theme('colors.teal[300]'),
            '--tw-prose-invert-pre-bg': 'rgb(0 0 0 / 50%)',
            '--tw-prose-invert-th-borders': theme('colors.teal[600]'),
            '--tw-prose-invert-td-borders': theme('colors.teal[700]'),
          }
        },
        cyan: {
          css: {
            '--tw-prose-body': theme('colors.cyan[800]'),
            '--tw-prose-headings': theme('colors.cyan[900]'),
            '--tw-prose-lead': theme('colors.cyan[700]'),
            '--tw-prose-links': theme('colors.cyan[900]'),
            '--tw-prose-bold': theme('colors.cyan[900]'),
            '--tw-prose-counters': theme('colors.cyan[600]'),
            '--tw-prose-bullets': theme('colors.cyan[400]'),
            '--tw-prose-hr': theme('colors.cyan[300]'),
            '--tw-prose-quotes': theme('colors.cyan[900]'),
            '--tw-prose-quote-borders': theme('colors.cyan[300]'),
            '--tw-prose-captions': theme('colors.cyan[700]'),
            '--tw-prose-code': theme('colors.cyan[900]'),
            '--tw-prose-pre-code': theme('colors.cyan[100]'),
            '--tw-prose-pre-bg': theme('colors.cyan[900]'),
            '--tw-prose-th-borders': theme('colors.cyan[300]'),
            '--tw-prose-td-borders': theme('colors.cyan[200]'),
            '--tw-prose-invert-body': theme('colors.cyan[200]'),
            '--tw-prose-invert-headings': theme('colors.white'),
            '--tw-prose-invert-lead': theme('colors.cyan[300]'),
            '--tw-prose-invert-links': theme('colors.white'),
            '--tw-prose-invert-bold': theme('colors.white'),
            '--tw-prose-invert-counters': theme('colors.cyan[400]'),
            '--tw-prose-invert-bullets': theme('colors.cyan[600]'),
            '--tw-prose-invert-hr': theme('colors.cyan[700]'),
            '--tw-prose-invert-quotes': theme('colors.cyan[100]'),
            '--tw-prose-invert-quote-borders': theme('colors.cyan[700]'),
            '--tw-prose-invert-captions': theme('colors.cyan[400]'),
            '--tw-prose-invert-code': theme('colors.white'),
            '--tw-prose-invert-pre-code': theme('colors.cyan[300]'),
            '--tw-prose-invert-pre-bg': 'rgb(0 0 0 / 50%)',
            '--tw-prose-invert-th-borders': theme('colors.cyan[600]'),
            '--tw-prose-invert-td-borders': theme('colors.cyan[700]'),
          }
        },
        sky: {
          css: {
            '--tw-prose-body': theme('colors.sky[800]'),
            '--tw-prose-headings': theme('colors.sky[900]'),
            '--tw-prose-lead': theme('colors.sky[700]'),
            '--tw-prose-links': theme('colors.sky[900]'),
            '--tw-prose-bold': theme('colors.sky[900]'),
            '--tw-prose-counters': theme('colors.sky[600]'),
            '--tw-prose-bullets': theme('colors.sky[400]'),
            '--tw-prose-hr': theme('colors.sky[300]'),
            '--tw-prose-quotes': theme('colors.sky[900]'),
            '--tw-prose-quote-borders': theme('colors.sky[300]'),
            '--tw-prose-captions': theme('colors.sky[700]'),
            '--tw-prose-code': theme('colors.sky[900]'),
            '--tw-prose-pre-code': theme('colors.sky[100]'),
            '--tw-prose-pre-bg': theme('colors.sky[900]'),
            '--tw-prose-th-borders': theme('colors.sky[300]'),
            '--tw-prose-td-borders': theme('colors.sky[200]'),
            '--tw-prose-invert-body': theme('colors.sky[200]'),
            '--tw-prose-invert-headings': theme('colors.white'),
            '--tw-prose-invert-lead': theme('colors.sky[300]'),
            '--tw-prose-invert-links': theme('colors.white'),
            '--tw-prose-invert-bold': theme('colors.white'),
            '--tw-prose-invert-counters': theme('colors.sky[400]'),
            '--tw-prose-invert-bullets': theme('colors.sky[600]'),
            '--tw-prose-invert-hr': theme('colors.sky[700]'),
            '--tw-prose-invert-quotes': theme('colors.sky[100]'),
            '--tw-prose-invert-quote-borders': theme('colors.sky[700]'),
            '--tw-prose-invert-captions': theme('colors.sky[400]'),
            '--tw-prose-invert-code': theme('colors.white'),
            '--tw-prose-invert-pre-code': theme('colors.sky[300]'),
            '--tw-prose-invert-pre-bg': 'rgb(0 0 0 / 50%)',
            '--tw-prose-invert-th-borders': theme('colors.sky[600]'),
            '--tw-prose-invert-td-borders': theme('colors.sky[700]'),
          }
        },
        blue: {
          css: {
            '--tw-prose-body': theme('colors.blue[800]'),
            '--tw-prose-headings': theme('colors.blue[900]'),
            '--tw-prose-lead': theme('colors.blue[700]'),
            '--tw-prose-links': theme('colors.blue[900]'),
            '--tw-prose-bold': theme('colors.blue[900]'),
            '--tw-prose-counters': theme('colors.blue[600]'),
            '--tw-prose-bullets': theme('colors.blue[400]'),
            '--tw-prose-hr': theme('colors.blue[300]'),
            '--tw-prose-quotes': theme('colors.blue[900]'),
            '--tw-prose-quote-borders': theme('colors.blue[300]'),
            '--tw-prose-captions': theme('colors.blue[700]'),
            '--tw-prose-code': theme('colors.blue[900]'),
            '--tw-prose-pre-code': theme('colors.blue[100]'),
            '--tw-prose-pre-bg': theme('colors.blue[900]'),
            '--tw-prose-th-borders': theme('colors.blue[300]'),
            '--tw-prose-td-borders': theme('colors.blue[200]'),
            '--tw-prose-invert-body': theme('colors.blue[200]'),
            '--tw-prose-invert-headings': theme('colors.white'),
            '--tw-prose-invert-lead': theme('colors.blue[300]'),
            '--tw-prose-invert-links': theme('colors.white'),
            '--tw-prose-invert-bold': theme('colors.white'),
            '--tw-prose-invert-counters': theme('colors.blue[400]'),
            '--tw-prose-invert-bullets': theme('colors.blue[600]'),
            '--tw-prose-invert-hr': theme('colors.blue[700]'),
            '--tw-prose-invert-quotes': theme('colors.blue[100]'),
            '--tw-prose-invert-quote-borders': theme('colors.blue[700]'),
            '--tw-prose-invert-captions': theme('colors.blue[400]'),
            '--tw-prose-invert-code': theme('colors.white'),
            '--tw-prose-invert-pre-code': theme('colors.blue[300]'),
            '--tw-prose-invert-pre-bg': 'rgb(0 0 0 / 50%)',
            '--tw-prose-invert-th-borders': theme('colors.blue[600]'),
            '--tw-prose-invert-td-borders': theme('colors.blue[700]'),
          }
        },
        indigo: {
          css: {
            '--tw-prose-body': theme('colors.indigo[800]'),
            '--tw-prose-headings': theme('colors.indigo[900]'),
            '--tw-prose-lead': theme('colors.indigo[700]'),
            '--tw-prose-links': theme('colors.indigo[900]'),
            '--tw-prose-bold': theme('colors.indigo[900]'),
            '--tw-prose-counters': theme('colors.indigo[600]'),
            '--tw-prose-bullets': theme('colors.indigo[400]'),
            '--tw-prose-hr': theme('colors.indigo[300]'),
            '--tw-prose-quotes': theme('colors.indigo[900]'),
            '--tw-prose-quote-borders': theme('colors.indigo[300]'),
            '--tw-prose-captions': theme('colors.indigo[700]'),
            '--tw-prose-code': theme('colors.indigo[900]'),
            '--tw-prose-pre-code': theme('colors.indigo[100]'),
            '--tw-prose-pre-bg': theme('colors.indigo[900]'),
            '--tw-prose-th-borders': theme('colors.indigo[300]'),
            '--tw-prose-td-borders': theme('colors.indigo[200]'),
            '--tw-prose-invert-body': theme('colors.indigo[200]'),
            '--tw-prose-invert-headings': theme('colors.white'),
            '--tw-prose-invert-lead': theme('colors.indigo[300]'),
            '--tw-prose-invert-links': theme('colors.white'),
            '--tw-prose-invert-bold': theme('colors.white'),
            '--tw-prose-invert-counters': theme('colors.indigo[400]'),
            '--tw-prose-invert-bullets': theme('colors.indigo[600]'),
            '--tw-prose-invert-hr': theme('colors.indigo[700]'),
            '--tw-prose-invert-quotes': theme('colors.indigo[100]'),
            '--tw-prose-invert-quote-borders': theme('colors.indigo[700]'),
            '--tw-prose-invert-captions': theme('colors.indigo[400]'),
            '--tw-prose-invert-code': theme('colors.white'),
            '--tw-prose-invert-pre-code': theme('colors.indigo[300]'),
            '--tw-prose-invert-pre-bg': 'rgb(0 0 0 / 50%)',
            '--tw-prose-invert-th-borders': theme('colors.indigo[600]'),
            '--tw-prose-invert-td-borders': theme('colors.indigo[700]'),
          }
        },
        violet: {
          css: {
            '--tw-prose-body': theme('colors.violet[800]'),
            '--tw-prose-headings': theme('colors.violet[900]'),
            '--tw-prose-lead': theme('colors.violet[700]'),
            '--tw-prose-links': theme('colors.violet[900]'),
            '--tw-prose-bold': theme('colors.violet[900]'),
            '--tw-prose-counters': theme('colors.violet[600]'),
            '--tw-prose-bullets': theme('colors.violet[400]'),
            '--tw-prose-hr': theme('colors.violet[300]'),
            '--tw-prose-quotes': theme('colors.violet[900]'),
            '--tw-prose-quote-borders': theme('colors.violet[300]'),
            '--tw-prose-captions': theme('colors.violet[700]'),
            '--tw-prose-code': theme('colors.violet[900]'),
            '--tw-prose-pre-code': theme('colors.violet[100]'),
            '--tw-prose-pre-bg': theme('colors.violet[900]'),
            '--tw-prose-th-borders': theme('colors.violet[300]'),
            '--tw-prose-td-borders': theme('colors.violet[200]'),
            '--tw-prose-invert-body': theme('colors.violet[200]'),
            '--tw-prose-invert-headings': theme('colors.white'),
            '--tw-prose-invert-lead': theme('colors.violet[300]'),
            '--tw-prose-invert-links': theme('colors.white'),
            '--tw-prose-invert-bold': theme('colors.white'),
            '--tw-prose-invert-counters': theme('colors.violet[400]'),
            '--tw-prose-invert-bullets': theme('colors.violet[600]'),
            '--tw-prose-invert-hr': theme('colors.violet[700]'),
            '--tw-prose-invert-quotes': theme('colors.violet[100]'),
            '--tw-prose-invert-quote-borders': theme('colors.violet[700]'),
            '--tw-prose-invert-captions': theme('colors.violet[400]'),
            '--tw-prose-invert-code': theme('colors.white'),
            '--tw-prose-invert-pre-code': theme('colors.violet[300]'),
            '--tw-prose-invert-pre-bg': 'rgb(0 0 0 / 50%)',
            '--tw-prose-invert-th-borders': theme('colors.violet[600]'),
            '--tw-prose-invert-td-borders': theme('colors.violet[700]'),
          }
        },
        purple: {
          css: {
            '--tw-prose-body': theme('colors.purple[800]'),
            '--tw-prose-headings': theme('colors.purple[900]'),
            '--tw-prose-lead': theme('colors.purple[700]'),
            '--tw-prose-links': theme('colors.purple[900]'),
            '--tw-prose-bold': theme('colors.purple[900]'),
            '--tw-prose-counters': theme('colors.purple[600]'),
            '--tw-prose-bullets': theme('colors.purple[400]'),
            '--tw-prose-hr': theme('colors.purple[300]'),
            '--tw-prose-quotes': theme('colors.purple[900]'),
            '--tw-prose-quote-borders': theme('colors.purple[300]'),
            '--tw-prose-captions': theme('colors.purple[700]'),
            '--tw-prose-code': theme('colors.purple[900]'),
            '--tw-prose-pre-code': theme('colors.purple[100]'),
            '--tw-prose-pre-bg': theme('colors.purple[900]'),
            '--tw-prose-th-borders': theme('colors.purple[300]'),
            '--tw-prose-td-borders': theme('colors.purple[200]'),
            '--tw-prose-invert-body': theme('colors.purple[200]'),
            '--tw-prose-invert-headings': theme('colors.white'),
            '--tw-prose-invert-lead': theme('colors.purple[300]'),
            '--tw-prose-invert-links': theme('colors.white'),
            '--tw-prose-invert-bold': theme('colors.white'),
            '--tw-prose-invert-counters': theme('colors.purple[400]'),
            '--tw-prose-invert-bullets': theme('colors.purple[600]'),
            '--tw-prose-invert-hr': theme('colors.purple[700]'),
            '--tw-prose-invert-quotes': theme('colors.purple[100]'),
            '--tw-prose-invert-quote-borders': theme('colors.purple[700]'),
            '--tw-prose-invert-captions': theme('colors.purple[400]'),
            '--tw-prose-invert-code': theme('colors.white'),
            '--tw-prose-invert-pre-code': theme('colors.purple[300]'),
            '--tw-prose-invert-pre-bg': 'rgb(0 0 0 / 50%)',
            '--tw-prose-invert-th-borders': theme('colors.purple[600]'),
            '--tw-prose-invert-td-borders': theme('colors.purple[700]'),
          }
        },
        fuchsia: {
          css: {
            '--tw-prose-body': theme('colors.fuschia[800]'),
            '--tw-prose-headings': theme('colors.fuschia[900]'),
            '--tw-prose-lead': theme('colors.fuschia[700]'),
            '--tw-prose-links': theme('colors.fuschia[900]'),
            '--tw-prose-bold': theme('colors.fuschia[900]'),
            '--tw-prose-counters': theme('colors.fuschia[600]'),
            '--tw-prose-bullets': theme('colors.fuschia[400]'),
            '--tw-prose-hr': theme('colors.fuschia[300]'),
            '--tw-prose-quotes': theme('colors.fuschia[900]'),
            '--tw-prose-quote-borders': theme('colors.fuschia[300]'),
            '--tw-prose-captions': theme('colors.fuschia[700]'),
            '--tw-prose-code': theme('colors.fuschia[900]'),
            '--tw-prose-pre-code': theme('colors.fuschia[100]'),
            '--tw-prose-pre-bg': theme('colors.fuschia[900]'),
            '--tw-prose-th-borders': theme('colors.fuschia[300]'),
            '--tw-prose-td-borders': theme('colors.fuschia[200]'),
            '--tw-prose-invert-body': theme('colors.fuschia[200]'),
            '--tw-prose-invert-headings': theme('colors.white'),
            '--tw-prose-invert-lead': theme('colors.fuschia[300]'),
            '--tw-prose-invert-links': theme('colors.white'),
            '--tw-prose-invert-bold': theme('colors.white'),
            '--tw-prose-invert-counters': theme('colors.fuschia[400]'),
            '--tw-prose-invert-bullets': theme('colors.fuschia[600]'),
            '--tw-prose-invert-hr': theme('colors.fuschia[700]'),
            '--tw-prose-invert-quotes': theme('colors.fuschia[100]'),
            '--tw-prose-invert-quote-borders': theme('colors.fuschia[700]'),
            '--tw-prose-invert-captions': theme('colors.fuschia[400]'),
            '--tw-prose-invert-code': theme('colors.white'),
            '--tw-prose-invert-pre-code': theme('colors.fuschia[300]'),
            '--tw-prose-invert-pre-bg': 'rgb(0 0 0 / 50%)',
            '--tw-prose-invert-th-borders': theme('colors.fuschia[600]'),
            '--tw-prose-invert-td-borders': theme('colors.fuschia[700]'),
          }
        },
        pink: {
          css: {
            '--tw-prose-body': theme('colors.pink[800]'),
            '--tw-prose-headings': theme('colors.pink[900]'),
            '--tw-prose-lead': theme('colors.pink[700]'),
            '--tw-prose-links': theme('colors.pink[900]'),
            '--tw-prose-bold': theme('colors.pink[900]'),
            '--tw-prose-counters': theme('colors.pink[600]'),
            '--tw-prose-bullets': theme('colors.pink[400]'),
            '--tw-prose-hr': theme('colors.pink[300]'),
            '--tw-prose-quotes': theme('colors.pink[900]'),
            '--tw-prose-quote-borders': theme('colors.pink[300]'),
            '--tw-prose-captions': theme('colors.pink[700]'),
            '--tw-prose-code': theme('colors.pink[900]'),
            '--tw-prose-pre-code': theme('colors.pink[100]'),
            '--tw-prose-pre-bg': theme('colors.pink[900]'),
            '--tw-prose-th-borders': theme('colors.pink[300]'),
            '--tw-prose-td-borders': theme('colors.pink[200]'),
            '--tw-prose-invert-body': theme('colors.pink[200]'),
            '--tw-prose-invert-headings': theme('colors.white'),
            '--tw-prose-invert-lead': theme('colors.pink[300]'),
            '--tw-prose-invert-links': theme('colors.white'),
            '--tw-prose-invert-bold': theme('colors.white'),
            '--tw-prose-invert-counters': theme('colors.pink[400]'),
            '--tw-prose-invert-bullets': theme('colors.pink[600]'),
            '--tw-prose-invert-hr': theme('colors.pink[700]'),
            '--tw-prose-invert-quotes': theme('colors.pink[100]'),
            '--tw-prose-invert-quote-borders': theme('colors.pink[700]'),
            '--tw-prose-invert-captions': theme('colors.pink[400]'),
            '--tw-prose-invert-code': theme('colors.white'),
            '--tw-prose-invert-pre-code': theme('colors.pink[300]'),
            '--tw-prose-invert-pre-bg': 'rgb(0 0 0 / 50%)',
            '--tw-prose-invert-th-borders': theme('colors.pink[600]'),
            '--tw-prose-invert-td-borders': theme('colors.pink[700]'),
          }
        },
        rose: {
          css: {
            '--tw-prose-body': theme('colors.rose[800]'),
            '--tw-prose-headings': theme('colors.rose[900]'),
            '--tw-prose-lead': theme('colors.rose[700]'),
            '--tw-prose-links': theme('colors.rose[900]'),
            '--tw-prose-bold': theme('colors.rose[900]'),
            '--tw-prose-counters': theme('colors.rose[600]'),
            '--tw-prose-bullets': theme('colors.rose[400]'),
            '--tw-prose-hr': theme('colors.rose[300]'),
            '--tw-prose-quotes': theme('colors.rose[900]'),
            '--tw-prose-quote-borders': theme('colors.rose[300]'),
            '--tw-prose-captions': theme('colors.rose[700]'),
            '--tw-prose-code': theme('colors.rose[900]'),
            '--tw-prose-pre-code': theme('colors.rose[100]'),
            '--tw-prose-pre-bg': theme('colors.rose[900]'),
            '--tw-prose-th-borders': theme('colors.rose[300]'),
            '--tw-prose-td-borders': theme('colors.rose[200]'),
            '--tw-prose-invert-body': theme('colors.rose[200]'),
            '--tw-prose-invert-headings': theme('colors.white'),
            '--tw-prose-invert-lead': theme('colors.rose[300]'),
            '--tw-prose-invert-links': theme('colors.white'),
            '--tw-prose-invert-bold': theme('colors.white'),
            '--tw-prose-invert-counters': theme('colors.rose[400]'),
            '--tw-prose-invert-bullets': theme('colors.rose[600]'),
            '--tw-prose-invert-hr': theme('colors.rose[700]'),
            '--tw-prose-invert-quotes': theme('colors.rose[100]'),
            '--tw-prose-invert-quote-borders': theme('colors.rose[700]'),
            '--tw-prose-invert-captions': theme('colors.rose[400]'),
            '--tw-prose-invert-code': theme('colors.white'),
            '--tw-prose-invert-pre-code': theme('colors.rose[300]'),
            '--tw-prose-invert-pre-bg': 'rgb(0 0 0 / 50%)',
            '--tw-prose-invert-th-borders': theme('colors.rose[600]'),
            '--tw-prose-invert-td-borders': theme('colors.rose[700]'),
          }
        }
      })
    },
  },
  corePlugins: {},
  plugins: [
    require('@tailwindcss/typography'),
  ],
}
