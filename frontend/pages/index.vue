<template>
  <div>

    <div id="page-title" v-if="!titleLoading">
      <vue-typed-js :strings="preTitle" :backDelay="1000">
        <h2 class="typing text-right" id="preTitle"  ></h2>
      </vue-typed-js>
      <vue-typed-js :strings="postTitle" :backDelay="1000">
        <h2 class="typing text-right" id="postTitle"></h2>
      </vue-typed-js>
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
import { VueTypedJs } from 'vue-typed-js'
import WebSocketTest from "../components/WebSocketTest";
import About from "../components/about";

export default {
  name: "index",
  components: {About, WebSocketTest, VueTypedJs},
  data: () => ({
    timer: undefined,
    preTitle: ["Legacy Edition"],
    postTitle: ["Acronym Finder"],
    preDone: false,
    postDone: false,
    titleLoading: false,
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
