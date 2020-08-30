<template>
  <div>
    <v-img></v-img>
    <v-card flat>
      <v-card-title>質問その{{  }}</v-card-title>
      <v-card-text>{{ this.question.qestion }}</v-card-text>
    </v-card>
  <div>
    <v-btn @click="checkAnswer('Yes')">知ってた</v-btn>
    <v-btn @click="checkAnswer('No')">知らなかった</v-btn>
  </div>
</div>
</template>

<script>
import Question from '../models/question.js'

export default{
  data() {
    return {
      question: new Question()
    }
  },
  methods: {
    checkAnswer(answer) {
      console.log(this.question)
      this.question.checkAnswer(answer).then( resp => {
        if ( resp.data.continue ) {
          this.$router.go({path: this.$router.currentRoute.path, force: true});
        } else {
          this.$router.push({ path: `/result`, params: {result: resp.data.result} })
        }
      } )
    }
  }

}
</script>

<style scoped>
</style>
