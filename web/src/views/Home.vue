<template>
  <div class="home">

  </div>
</template>

<script>
export default {
  name: 'Home',
  components: {
  },
  computed: {
    gameId() {
      return this.$store.state.gameId;
    }
  },
  mounted() {
    if (this.gameId === false) {
      this.$router.push('/start')
    } else {
      this.$router.push('/game')
    }
  }
}
</script>
