<template>
  <div>
    <h1>APP TITLE</h1>
    <h2>SFU</h2>
    <v-row>
      <v-col v-for="c in choices" sm="6" md="3">
        <v-card>
          <h2>{{c}}</h2>
        </v-card>
      </v-col>
    </v-row>
    <WebSocketTest />
  </div>
</template>

<script>
import WebSocketTest from "../components/WebSocketTest";
export default {
  name: "index",
  components: {WebSocketTest},
  data: () => ({
    acronym: "SFU",
    choices: ["A", "B", "C", "D"]
  })
}
</script>
