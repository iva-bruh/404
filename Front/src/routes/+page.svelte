<script>
  import Header from "../components/Header.svelte";
  import Footer from "../components/Footer.svelte";
</script>
<Header></Header>
<style>
  .background {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1;
    animation: gradientAnimation 15s ease infinite; /* Увеличено время анимации для плавности */
    background: linear-gradient(270deg, #ff7e5f, #feb47b, #ff6a6a, #f3a683, #4a69bd, #1e90ff, #00dbde, #fc00ff);
    background-size: 400% 400%; /* Размер градиента увеличен для эффекта */
  }

  @keyframes gradientAnimation {
    0% {
      background-position: 0% 50%;
    }
    25% {
      background-position: 100% 50%;
    }
    50% {
      background-position: 100% 100%;
    }
    75% {
      background-position: 0% 0%;
    }
    100% {
      background-position: 0% 50%;
    }
  }

  .content {
    position: relative;
    z-index: 1;
    color: white;
    text-align: center;
    padding: 50px;
    font-size: 2em;
  }
</style>

<div class="background"></div>
<div class="content">
  <h1>Добро пожаловать на наш сайт!</h1>
  <p>Здесь начинается ваше удивительное путешествие!</p>
</div>
<Footer></Footer>