<template>
  <div id="hangman_cover" width="100%">
     <svg class="hangman" viewBox="0 0 96 96">
      <line v-if="HangLife = 0" class="stage10" x1="62" y1="70" x2="56" y2="56"></line>
      <line v-if="HangLife <= 1" class="stage9" x1="50" y1="70" x2="56" y2="56"></line>
      <line v-if="HangLife <= 2" class="stage8" x1="68" y1="46" x2="56" y2="40"></line>
      <line v-if="HangLife <= 3" class="stage7" x1="44" y1="46" x2="56" y2="40"></line>
      <line v-if="HangLife <= 4" class="stage6" x1="56" y1="40" x2="56" y2="56"></line>
      <circle v-if="HangLife <= 5" class="stage5" cx="56" cy="34" r="6"></circle>
      <line v-if="HangLife <= 6" class="stage4" x1="56" y1="16" x2="56" y2="28"></line>
      <line v-if="HangLife <= 7" class="stage3" x1="24" y1="24" x2="32" y2="16"></line>
      <line v-if="HangLife <= 8" class="stage3" x1="21" y1="16" x2="60" y2="16"></line>
      <line v-if="HangLife <= 9" class="stage2" x1="24" y1="80" x2="24" y2="16"></line>
      <line v-if="HangLife <= 10" class="stage1" x1="10" y1="80" x2="24" y2="80"></line>
      <line v-if="HangLife <= 11" class="stage1" x1="24" y1="80" x2="38" y2="80"></line>
    </svg>
  </div>
</template>

<style lang="scss" scoped>
svg {
  line, circle {
    stroke: #000
  }
  width: 100%;
  height: 20vh;
  object-fit: contain;
}
</style>

<script>
export default {
  name: 'HangmanCover',
  props: [
      'HangLifes'
  ],
  data() {
    return {
      HangLife: this.HangLifes
    }
  }
}
</script>