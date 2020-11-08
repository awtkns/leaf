<template>
  <v-card color="accent" dark min-width="400">
    <v-card-title>Help</v-card-title>
    <v-card-text>Click the 'PLAY' button then choose the correct</br>acronym for each question.</v-card-text>
    <v-card-actions>
      <v-spacer/>
      <v-btn @click="$emit('close')" dark color="primary" rounded>Close</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
    name: "help",
    data: () => ({})
}
</script>
