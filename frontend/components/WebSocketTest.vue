<template>
  <div>
    <SocketStatus :status="socketStatus" />
     <v-btn @click="sendMessage">
      Send Message
    </v-btn>
	 <v-btn @click="join">
      join game
    </v-btn>
	 <v-btn @click="startGame">
      Start game
    </v-btn>
	 <v-btn @click="sendAnswer">
      Send answer
    </v-btn>
    {{ messageRxd }}
  </div>
</template>

<script>
import SocketStatus from 'nuxt-socket-io/components/SocketStatus.vue'
export default {
  components: {
    SocketStatus
  },
  data() {
    return {
      socket: null,
      test: 'hello world',
      socketStatus: {}, // simply define this, and it will be populated with the status
      messageRxd: []
    }
  },
  methods: {
    sendMessage() {
      this.socket.emit('message', {data: 'hello from nuxt'}, (resp, data) => {
        console.log(resp, data)
        this.messageRxd.push(data)
      })
	 },
	 join() {
      this.socket.emit('join_game', {data: 'hello from nuxt'}, (resp, data) => {
        console.log(resp, data)
        this.messageRxd.push(data)
      })
	 },
	 startGame() {
      this.socket.emit('start_game', {data: 'hello from nuxt'}, (resp, data) => {
        console.log(resp, data)
      })
	 },
	 sendAnswer() {
      this.socket.emit('send_answer', {answer: 'fake'}, (resp, data) => {
        console.log(resp, data)
      })
	 },
	 

	 
  },
  mounted() {
	 this.socket = this.$nuxtSocket({path: '/ws/socket.io'})
	 this.socket.on('round_start', (msg, cb) => {
		 this.messageRxd.push("RECIEVED ROUND START", msg)
	 })
  }
}
</script>
