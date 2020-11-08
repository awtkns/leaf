<template>
  <v-card color="accent" dark min-width="400">
    <v-card-title>About</v-card-title>
    <v-card-text>Legacy Edition Acronym Finder is a very cool game</br>
      developed for Fall Hacks 2020 by Adam, Asim, Ethan,</br>
      Joey, and Jennifer</v-card-text>
    <v-card-actions>
      <v-spacer/>
      <v-btn @click="$emit('closeAbout')" dark color="primary" rounded>Close</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
    name: "about",
    data: () => ({})
}
</script>
