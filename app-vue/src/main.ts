import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import axios from 'axios'

const vuetify = createVuetify({
  components,
  directives,
})
const app = createApp(App)

axios.defaults.baseURL = 'http://127.0.0.1:8000/api'
app.use(createPinia())
app.use(router)
app.use(vuetify)

app.mount('#app')
