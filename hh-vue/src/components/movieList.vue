<template lang="html">
  <ul class="cont-ul clear">
    <li class="cont-li b1" v-for="item in movieList" :key='item.id'>
      <div class="img-con">
        <img class="movie-img" :src="item.images.large">
      </div>
      <div class="movie-msg clear">
        <p class="movie-name">{{item.title}}</p>
        <p class="movie-price r1">
        <span>评分 </span>{{item.rating.average}}</p>
      </div>
    </li>
  </ul>
</template>
<script>
export default {
  name: 'movieList',
  data () {
    return {
      movieList: []
    }
  },
  mounted () {
    // 这个是vue的钩子函数，当new Vue()实例创建完毕后执行的函数，关于vue的生命周期，可以去官网查看详情
    // 这里我用的是豆瓣的一个公共接口
    this.$http
      .jsonp('https://api.douban.com/v2/movie/top250?count=10')
      .then(res => {
        this.movieList = res.data.subjects
        res = null
      })
      .catch(error => {
        console.log('http error:' + error)
      })
  }
}
</script>
<style lang="css" scoped>
.cont-ul {
  padding: 0.5rem 0.5rem 0 0.5rem;
}
.cont-li {
  margin-bottom: 0.4rem;
  width: calc(50% - 0.2rem);
  float: left;
  overflow: hidden;
  border-radius: 4px;
  background: #ffffff;
  box-shadow: 1px 1px 4px rgba(131, 131, 131, 0.5);
}
.cont-li:nth-child(2n-1) {
  margin-right: 0.4rem;
}
.img-con {
  height: 12rem;
  overflow: hidden;
}
.movie-img {
  float: left;
  width: 100%;
}
.movie-msg {
  width: 100%;
  padding: 0.3rem 0.5rem;
}
.movie-name {
  line-height: 1.2rem;
  font-size: 0.8rem;
}
.movie-price {
  text-align: right;
  line-height: 1rem;
  font-size: 0.7rem;
  font-weight: 400;
}
.movie-price span {
  font-size: 0.5rem;
}
</style>
