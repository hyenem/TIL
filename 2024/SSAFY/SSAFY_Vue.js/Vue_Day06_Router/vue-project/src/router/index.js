import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '@/views/AboutView.vue'
import UserView from '@/views/UserView.vue'
import LoginView from '@/views/LoginView.vue'
import BoardView from '@/views/BoardView.vue'
import BoardList from '@/components/board/BoardList.vue'
import BoardCreate from '@/components/board/BoardCreate.vue'

const isAuth = true

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: AboutView,
    },
    {
      path: '/user/:id', // 동적 라우팅
      name: 'user',
      component: UserView,
    },
    {
      path: '/login', // 동적 라우팅
      name: 'login',
      component: LoginView,
      beforeEnter : (to, from)=>{
        if(isAuth){
          console.log('이미 로그인이 된 상태')
          return {name: 'home'}
        }
      }
    },
    {
      path: '/board',
      name: 'board',
      component: BoardView,
      children: [
        {
          path: '',
          name: 'boardList',
          component: BoardList
        },
        {
          path: 'create',
          name: 'boardCreate',
          component: BoardCreate
        }
      ]
    }
  ],
})

router.beforeEach((to, from)=>{
  // console.log(to)
  // console.log(from)

  if(!isAuth && to.name!=='login') {
    console.log('로그인이 필요합니다.')
    return {name:'login'}
  }
})

export default router
