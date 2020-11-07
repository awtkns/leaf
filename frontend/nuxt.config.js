import colors from 'vuetify/es5/util/colors'

export default {
  // Disable server-side rendering (https://go.nuxtjs.dev/ssr-mode)
  ssr: false,

  // Global page headers (https://go.nuxtjs.dev/config-head)
  head: {
    titleTemplate: '%s - frontend',
    title: 'frontend',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      {rel: 'stylesheet', href: 'https://fonts.googleapis.com/css2?family=Quantico:wght@400;700&display=swap'}
    ]
  },
  css: [
     '@/assets/main.css'
  ],
  plugins: [
  ],
  components: true,
  buildModules: [
    '@nuxtjs/vuetify',
  ],

  modules: [
    '@nuxtjs/axios',
    // '@nuxtjs/pwa',
    'nuxt-socket-io',
  ],
  io: {
    // module options
    sockets: [{url: 'http://localhost:5000'}]
  },

  axios: {
    baseURL:  process.env.API_URL || 'http://localhost:5000'
  },

  // Vuetify module configuration (https://go.nuxtjs.dev/config-vuetify)
  vuetify: {
    theme: {
      options: { customProperties: true },
      dark: false,
      themes: {
        light: {
          primary: '#51b847',
          accent: '#1982c4',
          secondary: '#398840',
          muted_accent: '#688D9D',
          main_bg: '#e6e6e6',
          light: '#ffffff',
          info: colors.teal.lighten1,
          warning: colors.amber.base,
          error: colors.deepOrange.accent4,
          success: colors.green.accent3,
          dark: '#0D1321'
        }
      }
    }
  },
}
