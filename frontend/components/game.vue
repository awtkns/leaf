<template>
  <div style="max-width: 50em">
  <h1 class="text-center pt-2">What is <span>{{ acronym }}</span>?</h1>
  <v-card :color="color">
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
            white-space="normal"
          >
          {{ w }}
          </v-btn>
        </v-col>
      </v-row>
    </v-card-text>

    <v-card-actions class="px-4">
      <v-alert color="muted_accent" class="mr-2">Score: {{score}}</v-alert>
      <v-expand-transition>
          <v-alert class="text-center ml-2" color="warning" prominent v-if="timeLeft">Time left: {{timeLeft}}s</v-alert>
      </v-expand-transition>
      <v-spacer></v-spacer>
      <v-btn color="error" @click="$emit('close')">Disconnect</v-btn>
    </v-card-actions>
  </v-card>
    <v-card>
      <v-data-table
        :headers="headers"
        :items="scores"
        :items-per-page="10"
      ></v-data-table>
    </v-card>
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
    score: 0,
    is_correct: undefined,
    timeLeft: undefined,
    timer: undefined,
    headers: [
      {
        text: 'Name',
        align: 'start',
        value: 'name',
      },
      {text: 'Score', value: 'score'},
    ],
    scores: []
  }),
  mounted() {
	 this.socket = this.$nuxtSocket({path: '/ws/socket.io'})
   this.socket.on('round_start', ({round_data, scores}, cb) => {
	  this.reset()
	  this.acronym = round_data.acron
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
      this.is_correct = undefined
      clearInterval(this.timer)
    },
    join() {
      this.socket.emit('join_game', {name: this.$store.state.name}, (resp, {round_data, leaderboard}) => {
        console.log(leaderboard)
        this.acronym = round_data.acronym
        this.words = round_data.words
        this.scores = leaderboard
      })
    },
    sendAnswer(answer) {
      this.socket.emit('send_answer', {answer: answer, name: this.$store.state.name}, (resp, data) => {
        this.is_correct = data
        if (this.is_correct) {
          this.score += 1
        }
      })
    },
  }
}
</script>
