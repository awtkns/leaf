<template>
  <v-app style="background-color: #e6e6e6">
    <v-main id="leaf">
      <nuxt />

      <img src="../assets/title-image.svg" style="position: fixed; bottom: 20px; left: -80px; max-height: 500px"/>
    </v-main>
  </v-app>
</template>

<style>
  #leaf {
    background-image: url("../assets/home.svg");

    /*background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)) , url("../static/raven.jpg") center center;*/
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
    -webkit-background-size: cover;
    -moz-background-size: cover;
    -o-background-size: cover;
  }
</style>

