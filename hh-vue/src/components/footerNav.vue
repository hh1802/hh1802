<template>
  <div class="footer">
    <ul class="footer-con b2 ui-transition">
      <li class="g1"></li>
      <li>2</li>
      <li>3</li>
      <li>4</li>
    </ul>
  </div>
</template>

<script>
export default {
  data () {}
}
</script>
<style lang="css">
.footer {
  height: 2rem;
  width: 100%;
  position: fixed;
  bottom: 0;
  left: 0;
  background-color: #fff;
}
.footer::before {
  content: "";
  display: block;
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 1px;
  background: #e0e0e0;
}
.footer-con li {
  float: left;
  width: 25%;
  height: 2rem;
  line-height: 2rem;
  font-size: 0.8rem;
  text-align: center;
  -webkit-transition: ease 0.25s;
  -moz-transition: ease 0.25s;
  -ms-transition: ease 0.25s;
  -o-transition: ease 0.25s;
  transition: ease 0.25s;
}
.footer-con li:active {
  background-color: rgb(248, 248, 248);
}
.footer-con:after {
  content: "";
  display: block;
  clear: both;
  width: 0;
  height: 0;
}
</style>
