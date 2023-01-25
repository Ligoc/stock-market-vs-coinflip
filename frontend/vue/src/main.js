import { createApp } from 'vue'
import App from './App.vue'
import './assets/main_styles.css'
import '@vuepic/vue-datepicker/dist/main.css'
import 'bootstrap-icons/font/bootstrap-icons.css'
import VueApexCharts from "vue3-apexcharts"
import Datepicker from '@vuepic/vue-datepicker'
import VueSelect  from "vue-select";
import axios from './plugins/axios'
import moment from './plugins/moment'




const app = createApp(App)
app.use(VueApexCharts)
app.use(axios)
app.use(moment)
app.component('datepicker', Datepicker)
app.component("v-select", VueSelect)
app.mount('#app')