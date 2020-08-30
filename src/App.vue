<template>
  <div id="app">
    <header-component/>
      <router-view/>
    <footer-component/>
  </div>
</template>

<script>
import HeaderComponent from './components/Header.vue'
import FooterComponent from './components/Footer.vue'

export default {
  components: {
    HeaderComponent,
    FooterComponent
  }
}
</script>
