<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <h2>Essential Links</h2>
    <ul>
      <li>
        <a
          href="http://localhost:5000/api/upload"
          target="_blank"
        >
          上传图片
        </a>
      </li>

      <li>
        <a
          href="/classify"
        >
          分类
        </a>
      </li>

      <li>
        <a
          href="/mine"
          target="_blank"
        >
          我的
        </a>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: '',
  data () {
    return {
      msg: '上传'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b9de;
}
</style>
