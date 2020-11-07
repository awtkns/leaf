<template>
  <div>
    <div id="page-title">
      <h1 class="display-3 text-right">{{ preTitle }}</h1>
      <h1 class="display-4 text-right">{{ postTitle }}</h1>
    </div>

    <div style="float: right">
      <v-row justify="end" class="py-2">
        <v-btn color="accent">Play</v-btn>
      </v-row>
      <v-row justify="end" class="py-2">
        <v-btn color="accent">Scores</v-btn>
      </v-row>
      <v-row justify="end" class="py-2">
        <v-btn color="accent" @click="about ^= true">About</v-btn>
      </v-row>
      <v-row justify="end"class="py-2">
        <v-btn color="accent">Help</v-btn>
      </v-row>
    </div>


    <About v-if="about" @close="about = false" style="position: fixed; bottom: 0; left: 0"/>

  </div>
</template>

<script>
import WebSocketTest from "../components/WebSocketTest";
import About from "../components/about";

export default {
  name: "index",
  components: {About, WebSocketTest},
  data: () => ({
    timer: undefined,
    preTitle: "Legacy Edition",
    postTitle: "Acronym Finder",
    about: false,

    acronym: "SFU",
    choices: ["A", "B", "C", "D"]
  }),
  // methods: {
  //   async updateTitle() {
  //     this.postTitle = (await this.$axios.get('/generate/single')).data
  //   }
  // },
  // created() {
  //   this.timer = setInterval(this.updateTitle, 2000)
  // },
  // beforeDestroy() {
  //   clearInterval(this.timer)
  // }
}
</script>
<style lang="scss">
  #page-title > h1:first-of-type {
    color: var(--v-accent-base);
  }
  #page-title > h1:last-of-type {
    color: var(--v-primary-base);
  }
</style>
