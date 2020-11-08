<template>
  <v-card :color="color" width="600">
    <v-card-title>What is {{ acronym }}?</v-card-title>
    <v-card-subtitle v-if="timeLeft">Ending in {{ timeLeft }}</v-card-subtitle>
    <v-card-text class="pa-4">
      <v-row >
        <v-col v-for="w in words" cols="4" sm="6">
          <v-btn
            color="accent"
            @click="sendAnswer(w)"
            min-height="100"
            style="width: inherit"
            class="ml-0"
            :disabled="color"
          >
            {{ w }}
          </v-btn>
        </v-col>
      </v-row>
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn text color="primary">Disconnect</v-btn>
    </v-card-actions>
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
    color: ctx => ctx.is_correct === true ? 'success': ctx.is_correct === false ? 'error' : undefined
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
