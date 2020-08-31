<template>
  <v-container>
    <v-img :src="jackinatorImage" max-height="250" max-width="180" contain class="jackImage"></v-img>
    <v-card flat class="question" max-height="380px" min-height="250px">
      <v-card-title>質問その{{ this.$route.params.id }}</v-card-title>
      <v-card-text>{{ questionSentence }}</v-card-text>
    </v-card>
  <v-row>
    <v-col cols="6">
      <v-btn class="choice" height="67px" @click="checkAnswer('Yes')">知ってた</v-btn>
    </v-col>
    <v-col cols="6">
      <v-btn class="choice" height="67px" @click="checkAnswer('No')">知らなかった</v-btn>
    </v-col>
  </v-row>
</v-container>
</template>

<script>
import Question from '../models/question.js';
import JackinatorImage from '../assets/jackinator.png';
import axios from 'axios';

export default{
  data() {
    return {
      question: new Question(),
      questionS: new Question().question,
      jackinatorImage: JackinatorImage,
    }
  },
  // mounted(){
  //   console.log(this.question);
  //   console.log(this.questionSentence);
  // },
  computed: {
    questionSentence(){
      return this.question.question;
    }
  },
  methods: {
    checkAnswer(answer) {
      console.log(this.question)
      axios.post( 'http://localhost:5000/questions', this.toPostedObject(answer) ).then( resp => {
        if ( resp.data.continue ) {
          this.$router.go({path: this.$router.currentRoute.path, force: true});
        } else {
          this.$router.push({ path: `/result`, params: {result: resp.data.result} })
        }
      } )
    },
    toPostedObject(answer){
      var postedObject = {}
      postedObject.question = this.questionS;
      postedObject.answer = answer;
      return postedObject;
    }
  }

}
</script>
<style scoped>
.question{
  background: rgba(255, 255, 255, 0.74);
  text-align: center;
}
.choice{
  width: 100%;
  background: linear-gradient(97.24deg, #FFF500 0%, #FF7A00 100%);
}
.jackImage{
  margin: 0 auto;
  margin-top: 40px;
  margin-bottom: 20px;
}
</style>
