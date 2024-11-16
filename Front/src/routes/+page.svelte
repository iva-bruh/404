<script>
  import Header from "../components/Header.svelte";
  import Footer from "../components/Footer.svelte";

  let slides = [
    {
      title: "О нас",
      content: "Мы рады представить вам наши услуги и помочь вам на пути к вашему успеху!",
      image: "https://via.placeholder.com/600x300/1e90ff/ffffff?text=Слайд+1"
    },
    {
      title: "Мероприятия",
      content: "Не пропустите наши актуальные мероприятия и события, которые помогут вам развиваться!",
      image: "https://via.placeholder.com/600x300/ff7e5f/ffffff?text=Слайд+2"
    },
    {
      title: "Контакты",
      content: "Свяжитесь с нами для получения дополнительной информации.",
      image: "https://via.placeholder.com/600x300/4a69bd/ffffff?text=Слайд+3"
    }
  ];

  let currentSlide = 0;

  function nextSlide() {
    currentSlide = (currentSlide + 1) % slides.length;
  }

  function prevSlide() {
    currentSlide = (currentSlide - 1 + slides.length) % slides.length;
  }
</script>

<Header />

<style>
  .background {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1;
    animation: gradientAnimation 15s ease infinite;
    background: linear-gradient(270deg, #ff7e5f, #feb47b, #ff6a6a, #f3a683, #4a69bd, #1e90ff, #00dbde, #fc00ff);
    background-size: 400% 400%;
  }

  @keyframes gradientAnimation {
    0% { background-position: 0% 50%; }
    25% { background-position: 100% 50%; }
    50% { background-position: 100% 100%; }
    75% { background-position: 0% 0%; }
    100% { background-position: 0% 50%; }
  }

  .container {
    display: flex;
    max-width: 1200px;
    margin: 50px auto;
    gap: 20px; /* Отступ между слайдером и блоком информации */
  }

  .slider {
    flex: 1;
    position: relative;
    border-radius: 15px;
    overflow: hidden;
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.2);
  }

  .slides {
    display: flex;
    transition: transform 0.7s ease;
  }

  .slide {
    min-width: 100%;
    background-color: rgba(255, 255, 255, 0.5);
    border-radius: 15px;
    padding: 20px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    position: relative;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.5);
    overflow: hidden;
  }

  .slide img {
    max-width: 100%;
    border-radius: 15px;
    margin-bottom: 15px;
    transition: transform 0.3s ease;
  }

  .slide:hover img {
    transform: scale(1.05);
  }

  .nav-button {
    background-color: rgba(0, 0, 0, 0.5);
    color: #fff;
    border: none;
    border-radius: 50%;
    width: 40px;
    height: 40px;
    cursor: pointer;
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    z-index: 2;
    transition: background-color 0.3s ease;
  }

  .nav-button.prev {
    left: 10px;
  }

  .nav-button.next {
    right: 10px;
  }

  .nav-button:hover {
    background-color: rgba(255, 255, 255, 0.7);
  }

  .info {
    flex: 1;
    background-color: rgba(255, 255, 255, 0.8);
    border-radius: 15px;
    padding: 20px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
  }

  .info h2 {
    margin-bottom: 15px;
    color: #333;
  }

  .info p {
    color: #555;
    margin-bottom: 10px;
    line-height: 1.5;
  }

  .info ul {
    list-style: none;
    padding: 0;
  }

  .info li {
    margin-bottom: 5px;
    color: #666;
  }
</style>

<div class="background"></div>

<!-- Окно контейнера для слайдера и информации -->
<div class="container">
  <!-- Слайдер -->
  <div class="slider">
    <div class="slides" style="transform: translateX(-{currentSlide * 100}%);">
      {#each slides as slide}
        <div class="slide">
          <img src={slide.image} alt={slide.title} />
          <h2>{slide.title}</h2>
          <p>{slide.content}</p>
        </div>
      {/each}
    </div>
    <button class="nav-button prev" on:click={prevSlide}>&lt;</button>
    <button class="nav-button next" on:click={nextSlide}>&gt;</button>
  </div>

  <!-- Блок дополнительной информации -->
  <div class="info">
    <h2>Поддержка ИТ-специалистов</h2>
    <p>
      Правительство Российской Федерации уделяет особое внимание созданию
      комфортных условий для специалистов ИТ-отрасли. Государству важно, чтобы специалисты
      работали в стране, пробовали себя в новых нишах, производили конкурентоспособные
      продукты и обеспечивали передовыми технологиями страну.
    </p>

    <h3>Основные направления:</h3>
    <ul>
      <li>Непрерывное обучение и повышение квалификации</li>
      <li>Организация сетевых мероприятий и встреч</li>
      <li>Поддержка стартапов и инновационных идей</li>
      <li>Обеспечение доступа к ресурсам и технологиям</li>
    </ul>
  </div>
</div>

<Footer />
