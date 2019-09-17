/* eslint-disable */
// eslint-disable-next-line
<template>
  <div id="app">
    <headerNav></headerNav>
    <div class="content">
      <router-view></router-view>
      <!-- 这里是展示来自路由页面数据的 -->
    </div>
    <!--  引入的footer组件 -->
    <footerNav></footerNav>

    <img src="./assets/logo.png" />
    <router-view />
  </div>
</template>

<script>
import headerNav from '@/components/headerNav'
import footerNav from '@/components/footerNav'
export default {
  name: 'App',
  components: {
    headerNav,
    footerNav
  },
  mounted () {}
}
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
