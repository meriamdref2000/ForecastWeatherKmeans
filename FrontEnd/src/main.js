import Vue from 'vue';
import axios from "axios";
import DashboardPlugin from './dashboard-plugin';
import App from './App.vue';
import VueAxios from "vue-axios";
import IsDemo from "./components/isDemo"
import VueMeta from 'vue-meta';
import "./assets/css/demo.css";
import routes from './routes';
import store from "./store";

Vue.use(DashboardPlugin);
Vue.use(VueAxios, axios);
Vue.use(IsDemo);
Vue.use(VueMeta, { keyName: 'head' });

const app = new Vue({
  el: '#app',
  render: h => h(App),
  router: routes,
  store:store
});

store.$app = app;

