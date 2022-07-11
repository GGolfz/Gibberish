<div class="card">
    <slot></slot>
</div>
<style>
.card {
    width: 60%;
    padding: 4rem;
    display: flex;
    background: rgba(255,255,255,0.2);
    flex-direction: column;
    border: 1px solid rgba(255,255,255,0.4);
    border-radius: 1rem;
    backdrop-filter: blur(40px);
}
</style>