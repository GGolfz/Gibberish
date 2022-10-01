<script>
  export let handleClick;
  export let text;
</script>

<button on:click={handleClick}>
  {text}
</button>

<style>
  button {
    outline: none;
    font-weight: 500;
    font-size: 1.2rem;
    color: white;
    background-color: transparent;
    border: 1px solid rgba(255, 255, 255, 1);
    border-radius: 100rem;
    padding: 1rem 2rem;
  }
  button:hover {
    background-color: rgb(255, 255, 255);
    color: black;
    cursor: pointer;
  }
</style>
