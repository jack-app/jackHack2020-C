import axios from 'axios'

export default class Question {
  constructor() {
    this.init()
    this.fetch()
  }

  fetch(){
    axios.get(`http://localhost:5000/questions`).then( resp => {
      console.log(resp.data.question);
      Object.assign(this, resp.data.question);
      console.log(this);
    } )
  }

  init(){
    this.id = null
    this.q = ""
    this.ans = null
    this.end = false
    this.prediction = null
  }
}
