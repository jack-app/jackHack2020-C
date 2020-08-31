<template>
  <v-container class="d-flex justify-center">
    <div class="title">
      <v-img :src="jackinatorTitleImage"></v-img>
    </div>
    <div>
      <v-img :src="jackinatorImage" max-width="180px" max-height="270px" contain class="jackImage"></v-img>
    </div>
    <div class="caution">
      <h3>素直に答えてね</h3>
    </div>
    <div class="Btn">
      <v-btn @click="toQuestion" class="mainBtn" width="270px" height="75px" color="#FFA95A">私にチャレンジ<br>あなたの生まれ年を当ててみせます</v-btn>
    </div>
  </v-container>
</template>
<script>
import JackinatorTitleImage from '../assets/JackinatorTitle.png';
import JackinatorImage from '../assets/jackinator.png';
export default{
  data(){
    return{
      jackinatorTitleImage: JackinatorTitleImage,
      jackinatorImage: JackinatorImage
    }
  },
  methods: {
    toQuestion(){
      this.$router.push({ path: `/question/${1}` })
    }
  }
}
</script>
<style scoped>
.title{
  margin: 0 auto;
  margin-top: 40px !important;
  margin-bottom: 30px !important;
}
.caution{
  height: 65px;
  margin: 30px auto;
  text-align: center;
  width: 90%;
  background: linear-gradient(90deg, rgba(146, 146, 146, 0.49) 0%, rgba(196, 196, 196, 0.63) 50.55%, rgba(146, 146, 146, 0) 102.17%);
}
.jackImage{
  margin: 0 auto;
}
h3{
  color: white;
  text-align: center;
  line-height: 65px;
}
.mainBtn{
  white-space: pre;
}
.Btn{
  text-align: center;
}
</style>
