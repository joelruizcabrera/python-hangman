import { createStore } from 'vuex'

export default createStore({
  state: {
    gameId: false,
    apiUrl: 'http://localhost:5000',
    letters: [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z"
    ],
    gameData: {
        word: ''
    }
  },
  mutations: {
    addGame(state, gameId) {
      state.gameId = gameId
    },
    addWord(state, word) {
      state.gameData.word = word
    }
  },
  actions: {
  },
  modules: {
  }
})
