<template>
  <div id="game_engine">
    <div class="container">
      <div class="row">
        <div class="column">
          <div id="stickman_window" style="width: 50vw;min-height: 20vh">
            <HangmanCover
            :HangLifes="lifes">

            </HangmanCover>
          </div>
        </div>
        <div class="column">
          <div id="hidden_letters">
            <input type="text" :value="letter.letter" v-for="letter in allLetters" :key="letter.index" :disabled="!successLetters.includes(letter.letter.toUpperCase())">
          </div>
        </div>
      </div>
      <div class="row typing">
        <button
            v-for="letter in letters"
            :key="letter"
            @click="addLetter(letter, gameId)"
            :disabled="typedLetters.includes(letter)"
        >
          {{letter}}
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios"

import HangmanCover from "@/components/Hangman"
export default {
  name: 'Game',
  components: {
    HangmanCover
  },

  data() {
    return {
      successLetters: [],
      allLetters: [],
      typedLetters: [],
      trys: 0,
      lifes: 12
    }
  },
  computed: {
    letters() {
      return this.$store.state.letters;
    },
    gameId() {
      return this.$store.state.gameId;
    },
    word() {
      return this.$store.state.gameData.word;
    },
    apiUrl() {
      return this.$store.state.apiUrl;
    }
  },
  mounted() {
    if (this.gameId === false) {
      this.$router.push('/start')
    } else {
      this.$router.push('/game')
    }
    for (let i = 0; i < this.word.length; i++) {
      this.allLetters.push({letter: this.word.charAt(i), index: i})
    }
  },
  methods: {
    async addLetter(letter, gameId) {
      console.log(gameId)
      let config = {
        url: this.apiUrl + "/api/v1/add",
        method: 'post',
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Header': '*',
          'Content-Type': 'application/json'
        },
        data: {
          gameId: gameId,
          letter: letter
        }
      }

      await axios.request(config).then((res) => {
        if (res.status === 200) {
          this.typedLetters.push(letter)
          if (res.data.status === 1) {
            this.lifes = this.lifes - 1
            this.trys = this.trys + 1
            if (this.lifes === 0) {
              this.$router.push('/win')
            }
          } else if (res.data.status === 2) {
            this.successLetters.push(letter)
            this.trys = this.trys + 1
          }
        }
        console.log(res.data)
        console.log(this.successLetters)
        console.log(this.typedLetters)
      })
    }
  }
}
</script>

<style lang="scss" scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 3rem;
}
#hidden_letters {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  input {
    border: none;
    width: 1.3rem;
    text-align: center;
    background: none;
    font-size: 1.5rem;
    &:not(:last-child) {
      margin-right: .5rem;
    }
    &[disabled] {
      border-bottom: 1px solid #000;
      color: #fff;
    }
  }
}
.row {
  &.typing {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    margin-top: 4rem;
  }
  &:not(.typing) {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items:center;
  }
}
</style>