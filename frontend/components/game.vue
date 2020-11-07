<template>
  <v-card>
    <v-card-title>What is {{ acronym }}?</v-card-title>
    <v-card-text>
      <v-btn v-for="w in words"  color="accent" @click="sendAnswer(w)">
        {{ w }}
      </v-btn>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: "game",
  data: () => ({
    acronym: "LEAF",
    words: ['A', 'B', 'C', 'D']
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
