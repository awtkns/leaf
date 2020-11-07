<template>
  <div>
/    <div id="page-title">
      <h1 class="display-3 text-right">{{ preTitle }}</h1>
      <h1 class="display-4 text-right">{{ postTitle }}</h1>
    </div>
    <v-row>
      <v-col>
        <img src="../assets/title-image.svg" width="100%"/>
      </v-col>
      <v-col>
      <div id="menu">
        <v-col>
          <v-row justify="end" class="py-2">
            <v-btn color="accent">Play</v-btn>
            <v-btn color="muted_accent light--text">Scores</v-btn>
          </v-row>
          <v-row justify="end" class="py-2">
            <v-btn color="muted_accent light--text" @click="about ^= true">About</v-btn>
            <v-btn color="muted_accent light--text">Help</v-btn>
          </v-row>
        </v-col>
      </div>
      </v-col>
    </v-row>

    <About v-if="about" @close="about = false" style="position: fixed; bottom: 0; right: 0;"/>
    <game />

  </div>
</template>

<script>
import WebSocketTest from "../components/WebSocketTest";
import About from "../components/about";
import Game from "../components/game";
export default {
  name: "index",
  components: {Game, About, WebSocketTest},
  data: () => ({
    preTitle: "Legacy Edition",
    postTitle: "Acronym Finder",
    about: false,

    acronym: "SFU",
    choices: ["A", "B", "C", "D"]
  }),
}
</script>
<style lang="scss">
  #preTitle {
    color: var(--v-accent-base);
  }
  #postTitle {
    color: var(--v-primary-base);
  }
</style>
