<template lang="html">
    <div class="info-con" v-if="info">
        <img class="movie-img" :src="info.images.large">
        <p class="movie-name">{{info.title}}<span>{{' ('+info.year+')'}}</span></p>
        <p>
          类型：
          <span v-for="genre in info.genres" :key='genre.id'>{{genre+' / '}}</span>
        </p>
        <p class="o1">评分：{{info.rating.average}}</p>
    </div>
</template>
<script>
export default {
  name: 'movieInfo',
  data () {
    return {
      info: '你好'
    }
  },
  mounted () {
    let info = sessionStorage.getItem('movieInfo') || 0
    if (info) {
      this.info = JSON.parse(info)
    }
  }
}
</script>
<style lang="css" scoped>
.info-con {
  padding: 1rem;
  margin: 1rem;
  border-radius: 8px;
  background: #ffffff;
  box-shadow: 1px 1px 6px rgba(131, 131, 131, 0.5);
  overflow: hidden;
}
.info-con img {
  width: 100%;
}
.info-con .movie-name {
  margin-top: 0.5rem;
  text-align: left;
  line-height: 2rem;
  font-size: 0.9rem;
  font-weight: 400;
}
.movie-name span {
  color: grey;
  font-size: 0.8rem;
}
</style>
