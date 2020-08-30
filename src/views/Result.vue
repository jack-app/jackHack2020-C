<template>
  <div>
    <v-img></v-img>
    <v-card>
      <v-card-title>あなたの生まれ年は</v-card-title>
      <v-card-text>{{ result }}年です</v-card-text>
    </v-card>
  <div>
    <v-btn><router-link to="/">もう一度遊ぶ</router-link></v-btn>
  </div>
</div>
</template>
<script>
export default{
  props:{
    result: Number
  }
}
</script>
<style scoped>
</style>
