<template>
  <div id="start_game">
    <img src="https://t4.ftcdn.net/jpg/02/48/96/11/360_F_248961156_XeSISXFo6bcFUw830wpE2zPLxWGCl1u9.jpg" alt="hangman_cover">
    <div class="form">
      <label for="userName">Dein Name:</label>
      <input type="text" name="userName" v-model="userName">
      <button
        @click="startGame()"
        type="button"
      >
        Spiel starten
      </button>
    </div>
  </div>
</template>

<style lang="scss" scoped>
#start_game {
  height: 100vh;
  width: 100vw;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  img {
    width: 13rem;
  }
  .form {
    display: flex;
    flex-direction: column;
  }
}
</style>

<script>
import axios from "axios"
export default {
  name: 'StartGame',
  data() {
    return {
      userName: '',
    }
  },
  computed: {
    apiUrl() {
      return this.$store.state.apiUrl;
    }
  },
  methods: {
    async startGame() {
      let config = {
        url: this.apiUrl + "/api/v1/start",
        method: 'post',
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Header': '*',
          'Content-Type': 'application/json'
        },
        data: {
          userName: this.userName
        }
      }

      await axios.request(config).then((res) => {
        if (res.status === 200) {
          this.$store.commit('addGame', res.data.gameId)
          this.$store.commit('addWord', res.data.word)
          this.$router.push('/')
        }
      })
    }
  }
}
</script>