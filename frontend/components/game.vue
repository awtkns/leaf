<template>
  <v-card :color="color" width="600" style="margin-right: 0 !important;">
    <h1 class="text-center pt-2">What is <span>{{ acronym }}</span>?</h1>
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
  </v-card>
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
    time: 50,
    is_correct: undefined,
    timeLeft: undefined,
    timer: undefined,
  }),
  mounted() {
	 this.socket = this.$nuxtSocket({path: '/ws/socket.io'})
   this.socket.on('round_start', ({round_data, scores}, cb) => {
	  this.reset()
	  this.acronym = round_data.acronym
     this.words = round_data.words
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
      this.answer_submitted = false
      this.is_correct = undefined
      clearInterval(this.timer)
    },
    join() {
      this.socket.emit('join_game', {data: 'hello from nuxt'}, (resp, {round_data, scores}) => {
        console.log(round_data.words);
        this.acronym = round_data.acronym
		  this.words = round_data.words
      })
    },
    sendAnswer(answer) {
		this.answer_submitted = true
      this.socket.emit('send_answer', {answer: answer}, (resp, data) => {
        this.is_correct = data
      })
    },
  }
}
</script>
