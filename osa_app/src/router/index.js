// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import Home from '../components/Home.vue';
import Login from '../components/Login.vue';
import Sleeping from '../components/Sleeping.vue';
const routes = [
  { path: '/', component: Login },
  { path: '/home', component: Home },
  { path: '/sleeping' , component: Sleeping}
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
