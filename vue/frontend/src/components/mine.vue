<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <h2></h2>
    <ul>
      <li>
        <a
          href="/mine/"
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
  name: 'Mine',
  data () {
    return {
      msg: '我的'
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
