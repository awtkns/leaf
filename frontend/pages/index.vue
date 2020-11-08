<template>
  <div>
    <div id="page-title" style="padding-right: 2%">
      <h2 class="text-right">{{ preTitle }}</h2>
      <h1 class="text-right overlay" color="primary">{{ postTitle }}</h1>
    </div>
      <div id="menu">
        <v-col>
          <v-row justify="end" class="py-2">
            <v-btn class="accent menu-btn" @click="playGame">Play</v-btn>
          </v-row>
          <v-row justify="end" class="py-2">
            <v-btn class="muted_accent light--text menu-btn" @click="about ^= true">About</v-btn>
          </v-row>
          <v-row justify="end" class="py-2">
            <v-btn class="muted_accent light--text menu-btn" @click="help ^= true">Help</v-btn>
          </v-row>
        </v-col>
      </div>

    <About v-if="about" @closeAbout="about = false" style="position: fixed; bottom: 0; right: 0;"/>
    <Help v-if="help" @closeHelp="help = false" style="position: fixed; bottom: 0; right: 0;"/>
    <v-dialog v-model="showGame" max-width="50em">
      <Game />
    </v-dialog>

     <v-overlay :value="nameDialog">
       <h2 style="color: white">Enter your Name</h2>
       <v-text-field v-model="name" solo single-line hide-details></v-text-field>
       <v-expand-transition>
         <v-btn rounded color="primary mt-3 mx-auto" v-if="name" @click="playGame">Play</v-btn>
       </v-expand-transition>
     </v-overlay>

  </div>
</template>

<script>
import WebSocketTest from "../components/WebSocketTest";
import About from "../components/about";
import Help from "../components/help";
import Game from "../components/game";
export default {
  name: "index",
  components: {Game, About, Help, WebSocketTest},
  data: () => ({
    preTitle: ["Legacy Edition"],
    postTitle: "Acronym Finder",
    about: false,
    help: false,
    showGame: false,
    nameDialog: false,
    acronym: "SFU",
    choices: ["A", "B", "C", "D"],
    name: undefined
  }),
  methods: {
    playGame() {
      this.$store.commit('setName', this.name);
      if (!this.$store.state.name) {
        this.nameDialog = true
      } else {
        this.showGame = true
      }
    },
  }
}
</script>
