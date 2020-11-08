<template>
  <div>
    <div id="page-title" style="padding-right: 2%">
      <h2 class="text-right">{{ preTitle }}</h2>
      <h1 class="text-right overlay" color="primary">{{ postTitle }}</h1>
    </div>
    <v-row>
      <v-col>
      <div id="menu">
        <v-col>
          <v-row justify="end" class="py-2">
            <v-btn class="accent menu-btn" @click="showGame = true">Play</v-btn>
            <v-btn class="muted_accent light--text menu-btn">Scores</v-btn>
          </v-row>
          <v-row justify="end" class="py-2">
            <v-btn class="muted_accent light--text menu-btn" @click="about ^= true">About</v-btn>
            <v-btn class="muted_accent light--text menu-btn">Help</v-btn>
          </v-row>
        </v-col>
      </div>
      </v-col>
    </v-row>

    <About v-if="about" @close="about = false" style="position: fixed; bottom: 0; right: 0;"/>
    <v-dialog v-model="showGame">
      <Game />
    </v-dialog>

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
    preTitle: ["Legacy Edition"],
    postTitle: "Acronym Finder",
    about: false,
    showGame: false,
    acronym: "SFU",
    choices: ["A", "B", "C", "D"]
  }),
}
</script>
