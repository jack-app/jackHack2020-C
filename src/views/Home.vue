<template>
  <div>
    <div>
      <v-img></v-img>
    </div>
    <div class="">
      <h1>Jackinator</h1>
    </div>
    <div>
      <h3>素直に答えてね</h3>
    </div>
    <div class="d-flex justify-center">
      <v-btn @click="toQuestion">私にチャレンジ<br/><span>あなたの生まれ年を当ててみせます</span></v-btn>
    </div>
  </div>
</template>
<script>
export default{
  methods: {
    toQuestion(){
      this.$router.push({ path: `/question/${1}` })
    }
  }
}
</script>
<style scoped>
</style>
