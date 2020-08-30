import axios from 'axios'
import qs from 'qs'

export default class Question {
  constructor(arg) {
    this.init()
    this.fetch(arg)
  }

  fetch(arg){

    const url = 'http://localhost:5000/questions';

    const params = arg

    const paramsSerializer = (params) => qs.stringify(params);

    axios.get(url, { params, paramsSerializer }).then( resp => {
      console.log(resp.data.question);
      Object.assign(this, resp.data.question);
      console.log(this);
    } )
  }

  init(){
    this.id = null
    this.q = ""
  }
}
