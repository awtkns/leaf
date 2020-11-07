<template>
  <div>
    <div id="page-title">
      <h1 class="display-3">{{ preTitle }}</h1>
      <h1 class="display-4">{{ postTitle }}</h1>
    </div>

    <v-btn color="accent">Play</v-btn>
    <v-btn color="accent">Scores</v-btn>
    <v-btn color="accent">About</v-btn>
    <v-btn color="accent">Help</v-btn>


<!--    <v-row>-->
<!--      <v-col v-for="c in choices" sm="6" md="3">-->
<!--        <v-card>-->
<!--          <h2>{{c}}</h2>-->
<!--        </v-card>-->
<!--      </v-col>-->
<!--    </v-row>-->
<!--    <WebSocketTest />-->
  </div>
</template>

<script>
import WebSocketTest from "../components/WebSocketTest";
export default {
  name: "index",
  components: {WebSocketTest},
  data: () => ({
    preTitle: "Legacy Edition",
    postTitle: "Acronym Finder",

    acronym: "SFU",
    choices: ["A", "B", "C", "D"]
  })
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
