<script>
  import Button from "./lib/Button.svelte";
  import Card from "./lib/Card.svelte";
  import Instruction from "./lib/Instruction.svelte";
  import Word from "./lib/Word.svelte";
  let isStart = false;
  let time = 180;
  let interval = null;
  const handleStart = () => {
    isStart = true;
    interval = setInterval(() => {
      time--;
      if (time === 0) {
        clearInterval(interval);
        isStart = false;
        time = 180;
      }
    }, 1000);
  };
  const renderTime = (time) => {
    if(time > 60) {
      return `${Math.floor(time / 60)}:${(time % 60).toString().padStart(2, "0")}`;
    } else {
      return `${time}`;
    }
  }
</script>

<main>
  <Card>
    <h1>CS Gibberish Game</h1>
    <h2>Time: {renderTime(time)}</h2>
    {#if isStart}
      <Word />
    {/if}
    {#if !isStart}
      <div class="button-wrapper"><Button handleClick={handleStart} text="Start Game" /></div>
    {/if}
  </Card>
  <Instruction />
</main>

<style>
  @import url("https://fonts.googleapis.com/css2?family=Kanit&display=swap");
  :root {
    font-family: "Kanit", sans-serif;
  }
  :global(body) {
    margin: 0;
  }
  main {
    text-align: center;
    width: 100vw;
    height: 100vh;
    background-image: url("https://res.cloudinary.com/practicaldev/image/fetch/s--RNNNA7AE--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://user-images.githubusercontent.com/69592270/101304060-72ff5b00-380d-11eb-8c58-a3172d791c9c.png");
    background-size: cover;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  h1,h2 {
    text-transform: uppercase;
    font-weight: 600;
    margin: 1rem;
    color: white;
  }
  h1 {
    font-size: 2.5rem;
  }
  h2 {
    font-size: 1.75rem;
  }
</style>
