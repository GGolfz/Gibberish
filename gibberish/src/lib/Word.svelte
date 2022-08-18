<script>
  import wordList from "../data/word_list.json";
import Button from "./Button.svelte";
  let displayWord = null;
  let remainedWord = wordList;
  let showOriginal = true;
  const randomWord = () => {
    let randomIndex = Math.floor(Math.random() * remainedWord.length);
    let randomWord = remainedWord[randomIndex];
    showOriginal = false;
    displayWord = randomWord;
    remainedWord.splice(randomIndex, 1);
  };
  const toggleOriginal = () => {
    showOriginal = true;
  };
  const handleClick = () => {
    if (showOriginal) {
      randomWord();
    } else {
      toggleOriginal();
    }
  };
  randomWord();
</script>

<div>
  <h1>{showOriginal ? displayWord.original : displayWord.gibberish}</h1>
  <Button text={showOriginal ? "Random New Word" : "Show Original Word"} handleClick={handleClick} />
</div>

<style>
  h1 {
    font-size: 3rem;
    color: white;
    margin: 5rem;
  }
</style>