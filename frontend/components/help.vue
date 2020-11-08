<template>
  <v-card color="accent" dark min-width="400">
    <v-card-title>Help</v-card-title>
    <v-card-text>Click the 'PLAY' button, enter your name then</br>
      choose the correct acronym for each question</br>
      to score points</v-card-text>
    <v-card-actions>
      <v-spacer/>
      <v-btn @click="$emit('closeHelp')" dark color="primary" rounded>Close</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
    name: "help",
    data: () => ({})
}
</script>
