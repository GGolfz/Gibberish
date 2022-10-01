<script>
  let showModal = false;
  const toggleModal = () => {
    showModal = !showModal;
  };
</script>

<div class="modal">
  <button id="instruction-button" on:click={toggleModal}> i </button>
  {#if showModal}
    <div class="modal-content">
      <div class="instruction-content">
        <h1>Guess the Gibberish</h1>
        <p>
          What the player will do is to guess the word from gibberish word that
          show in the screen.
        </p>
        <h2>Example</h2>
        <p>The Gibberish word is</p>
        <h2>Freezebuk</h2>
        <p>The real word is</p>
        <h2>Facebook</h2>
      </div>
      <h2 class="ending-word">Good Luck Have Fun!</h2>
    </div>
    <div class="modal-backdrop" on:click={toggleModal} />
  {/if}
</div>

<style>
  #instruction-button {
    font-size: 1.2rem;
    color: white;
    width: 32px;
    height: 32px;
    border-radius: 50%;
    border: 1px solid white;
    background: transparent;
    display: flex;
    justify-content: center;
    align-items: center;
    position: absolute;
    right: 3rem;
    top: 3rem;
  }
  .modal-content {
    width: 50vw;
    height: 80vh;
    background: white;
    z-index: 1000;
    position: absolute;
    margin: auto;
    top: 10%;
    left: 25%;
    border-radius: 15px;
    font-size: 1.2rem;
    display: flex;
    flex-direction: column;
  }
  .modal-backdrop {
    width: 100vw;
    height: 100vh;
    background: rgba(0, 0, 0, 0.5);
    position: absolute;
    top: 0;
    left: 0;
    z-index: 100;
  }
  .instruction-content {
    padding: 3rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    flex: 1 1 auto;
    gap: 0.5rem;
  }
  .ending-word {
    padding: 3rem;
  }
  h1,
  h2,
  p {
    margin: 0;
  }
</style>
