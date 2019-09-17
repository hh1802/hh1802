<template lang="html">
  <div class="header">
    <span class="back-btn" @click="goBack()">←</span>
    <h6 class="header-name" v-text="hName"></h6>
  </div>
</template>
<script>
export default {
  data () {
    return {
      hName: '首页'
    }
  },
  methods: {
    goBack () {
      history.back(-1)
    }
  }
}
</script>
<style lang="css" scoped>
/*  scoped的意思是这里的样式只对当前页面有效不会影响其他页面，还有可以设置lang="scss"就是支持css预编译，也就是支持sass或者less  */
.header {
  width: 100%;
  height: 2rem;
  padding: 0 2.6rem;
  position: fixed;
  left: 0;
  top: 0;
  background-color: #42b983;
  color: #ffffff;
}
.header-name {
  width: 80%;
  margin: 0 10%;
  text-align: center;
  line-height: 2rem;
  font-size: 0.8rem;
}
.back-btn {
  display: inline-block;
  position: absolute;
  top: 0;
  left: 0;
  width: 2.6rem;
  height: 2rem;
  line-height: 2rem;
  font-size: 1.1rem;
  text-align: center;
}
</style>
