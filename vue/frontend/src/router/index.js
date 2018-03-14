import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
import Home from '@/components/home'
import Classify from '@/components/classify'
import Mine from '@/components/Mine'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/classify',
      name: 'Classify',
      component: Classify
    },
    {
      path: '/Mine',
      name: 'Mine',
      component: Mine
    }

  ]
})
