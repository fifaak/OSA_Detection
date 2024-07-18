// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import Home from '../components/Home.vue';
import Login from '../components/Login.vue';
import Sleeping from '../components/Sleeping.vue';
import Dashboard from '../components/Dashboard.vue';
import Alert1 from '../components/Alert1.vue';
import Alert2 from '../components/Alert2.vue';
const routes = [
  { path: '/', component: Login },
  { path: '/home', component: Home },
  { path: '/sleeping', component: Sleeping },
  { path: '/dashboard', component: Dashboard },
  { path: '/alert1', component: Alert1 },
  {path:'/alert2', component: Alert2}
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
