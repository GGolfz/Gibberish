<script>
  import wordList from "../data/word_list.json";
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
  <button on:click={handleClick}>
    {showOriginal ? "Random New Word" : "Show Original Word"}
  </button>
</div>

<style>
  h1 {
    font-size: 3rem;
    color: white;
    margin: 5rem;
  }
  button {
    outline: none;
    font-weight: 500;
    font-size: 1.2rem;
    color: white;
    background-color: transparent;
    border: 1px solid rgba(255,255,255,1);
    border-radius: 100rem;
    padding: 1rem 2rem;
  }
  button:hover {
    background-color: rgb(255,255,255);
    color: black;
    cursor: pointer;
  }
</style>