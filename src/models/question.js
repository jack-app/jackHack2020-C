import axios from 'axios'

const url = 'http://localhost:5000/questions'

export default class Question {
  constructor() {
    this.init()
    this.fetch()
  }

  fetch(){

    // const params = sessionStorage.getItem('questions')
    //
    // const paramsSerializer = (params) => qs.stringify(params)

    axios.get(url).then( resp => {
      console.log(resp.data.question);
      Object.assign(this, resp.data);
      console.log(this);
    } )
  }

  toPostedObject(answer){
    var postedObject = {}
    postedObject.question = this.question
    postedObject.answer = answer
    return postedObject
  }

  cheackAnswer(answer){
    return axios.post( url, this.toPostedObject(answer) )
  }

  init(){
    this.question = ""
  }

  // save(question){
  //   let questions = sessionStorage.getItem('questions')
  //   questions.push(question)
  //   sessionStorage.setItem('questions', questions);
  // }
}
