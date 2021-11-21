import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Actors from '../views/Actors.vue'
import Genres from '../views/Genres.vue'
import Directors from '../views/Directors.vue'
import EndpointsLayout from '../components/EndpointsLayout.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/',
    name: 'EndpointsLayout',
    component: EndpointsLayout,
    children: [
      {
        path: '/actors',
        name: 'Actors',
        component: Actors
      },
      {
        path: '/genres',
        name: 'Genres',
        component: Genres
      },
      {
        path: '/directors',
        name: 'Directors',
        component: Directors
      },
    ]
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
