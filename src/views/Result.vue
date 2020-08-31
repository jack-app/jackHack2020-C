<template>
  <div>
    <v-img :src="jackinatorImage"  max-height="250" max-width="180" contain class="jackImage"></v-img>
    <v-card flat class="answer" min-height="250px" max-height="320px">
      <v-card-title>あなたの生まれ年は</v-card-title>
      <v-card-text class="result">{{ result }}年です</v-card-text>
    </v-card>
    <div class="again">
      <v-btn width="188px" height="35px" class="againBtn"><router-link to="/">もう一度遊ぶ</router-link></v-btn>
    </div>
  </div>
</template>
<script>
import JackinatorImage from '../assets/jackinator.png';

export default{
  props:{
    result: Number
  },
  data(){
    return{
      jackinatorImage: JackinatorImage
    }
  }
}
</script>
<style scoped>
.result{
  font-size: 40px;
  line-height: 78px;
  text-align: center;

}
.answer{
  background: rgba(255, 255, 255, 0.74);
  text-align: center;
}
.jackImage{
  margin: 0 auto;
  padding-top: 40px;
  margin-bottom: 20px;
}
.againBtn{
  background: linear-gradient(97.24deg, #FFF500 0%, #FF7A00 100%);
  margin-top: 30px;
}
.again{
  text-align: center;
}
</style>
