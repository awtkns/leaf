<template>
  <div>
    <v-col v-for="choice in choices" sm="6" md="3">
      <v-card>
        <button>{{choice}}</button>
      </v-card>
    </v-col>
  </div>
</template>

<script>
export default {
  data() {
    return {
      choices: ["Option A", "Option B", "Option C", "Option D"]
    }
  }
}
</script>
