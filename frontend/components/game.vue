<template>
  <v-card :color="color">
    <v-card-title>What is {{ acronym }}?</v-card-title>
    <v-card-subtitle v-if="timeLeft">Ending in {{ timeLeft }}</v-card-subtitle>
    <v-card-text>
      <v-btn v-for="w in words"  color="accent" @click="sendAnswer(w)" :disabled="is_correct != undefined">
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
    words: ['A', 'B', 'C', 'D'],
    is_correct: undefined,
    timeLeft: undefined,
    timer: undefined,
  }),
  mounted() {
	 this.socket = this.$nuxtSocket({path: '/ws/socket.io'})
   this.socket.on('round_start', ({acronym, words}, cb) => {
     this.reset()
		 this.acronym = acronym
     this.words = words
	 })
    this.socket.on('round_ending', ({delay}, cb) => {
      console.log('round_ending', delay)
      this.timeLeft = delay
      this.timer = setInterval(() => {
        if (this.timeLeft) {
          this.timeLeft -= 1
        }
        console.log(this.timeLeft)
      }, 1000)
    })
    this.join()
  },
  beforeDestroy() {
    clearInterval(this.timer)
  },
  computed: {
    color: ctx => ctx.is_correct === true ? 'success': ctx.is_correct === false ? 'error' : ''
  },
  methods: {
    reset() {
      this.is_correct = undefined
      clearInterval(this.timer)
    },
    join() {
      this.socket.emit('join_game', {data: 'hello from nuxt'}, (resp, {acronym, words}) => {
        console.log(words);
        this.acronym = acronym
        this.words = words
      })
    },
    sendAnswer(answer) {
      this.socket.emit('send_answer', {answer: answer}, (resp, data) => {
        this.is_correct = data
      })
    },
  }
}
</script>
