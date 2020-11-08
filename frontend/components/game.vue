<template>
  <div>
    <h1 class="text-center">What is {{ acronym }}?</h1>
    <v-card class="text-center">
      <v-card-text>
        <v-row>
        <v-col>
          <v-btn class="accent game-btn" style="height:10em" @click="sendAnswer(words[0])">{{ words[0] }}</v-btn>
          <v-btn class="accent game-btn" style="height:10em" @click="sendAnswer(words[1])">{{ words[1] }}</v-btn>
        </v-col>
        <v-col>
          <v-btn class="accent game-btn" style="height:10em" @click="sendAnswer(words[2])">{{ words[2] }}</v-btn>
          <v-btn class="accent game-btn" style="height:10em" @click="sendAnswer(words[3])">{{ words[3] }}</v-btn>
        </v-col>
      </v-row>
      </v-card-text>
    </v-card>
    <v-container id="stats">
      <v-row>
      <v-col class="text-center">
        <h3>Score</h3>
        <v-alert style="background-color:#688D9D">{{score}}</v-alert>
      </v-col>
      <v-col class="text-center">
        <h3>Time</h3>
        <v-alert style="background-color:#688D9D">{{time}}s</v-alert>
      </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  name: "game",
  data: () => ({
    acronym: "LEAF",
    words: [
      'Legacy Edition Acronym Finder',
      'Lazy Elephant And Fox',
      'Last Enormous Ant Farm',
      'Limes Eaten All Friday'
    ],
    score: 12345,
    time: 50
  }),
  mounted() {
	 this.socket = this.$nuxtSocket({path: '/ws/socket.io'})
	 this.join()
  },
  methods: {
     join() {
      this.socket.emit('join_game', {data: 'hello from nuxt'}, (resp, {acronym, words}) => {
        console.log(words);
        this.acronym = acronym
        this.words = words
      })
	 },
    sendAnswer(answer) {
      this.socket.emit('send_answer', {answer: answer}, (resp, data) => {
        console.log(resp, data)
      })
    },
  }
}
</script>
