<template>
  <v-card color="accent" dark min-width="400">
    <v-card-title>About</v-card-title>
    <v-card-text>Sample About Text</v-card-text>
    <v-card-actions>
      <v-spacer/>
      <v-btn @click="$emit('close')" dark color="primary" rounded>Close</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
    name: "about",
    data: () => ({})
}
</script>
