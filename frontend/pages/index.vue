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
  </div>
</template>

<script>
export default {
  name: "index",
  data: () => ({
    acronym: "SFU",
    choices: ["A", "B", "C", "D"]
  })
}
</script>
