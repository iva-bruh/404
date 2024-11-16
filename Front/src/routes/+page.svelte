<script>
  import Header from "../components/Header.svelte";
  import Footer from "../components/Footer.svelte";
  import { onMount } from 'svelte';

  let canvas;
  let ctx;
  let width;
  let height;

  const nodes = [];
  const numNodes = 115; // Количество узлов
  const maxDistance = 150; // Максимальное расстояние для соединения узлов

  function init() {
      ctx = canvas.getContext('2d');
      width = canvas.width = window.innerWidth;
      height = canvas.height = window.innerHeight;

      // Создаем узлы с случайными позициями и скоростями
      for (let i = 0; i < numNodes; i++) {
          nodes.push({
              x: Math.random() * width,
              y: Math.random() * height,
              vx: (Math.random() - 0.5) * 1,
              vy: (Math.random() - 0.5) * 1
          });
      }

      draw();
  }

  function draw() {
      ctx.clearRect(0, 0, width, height);

      // Рисуем линии между узлами, если они находятся достаточно близко
      for (let i = 0; i < numNodes; i++) {
          for (let j = i + 1; j < numNodes; j++) {
              const dx = nodes[i].x - nodes[j].x;
              const dy = nodes[i].y - nodes[j].y;
              const distance = Math.sqrt(dx * dx + dy * dy);

              if (distance < maxDistance) {
                  ctx.beginPath();
                  ctx.strokeStyle = 'rgba(0, 0, 0,' + (1 - distance / maxDistance) + ')';
                  ctx.moveTo(nodes[i].x, nodes[i].y);
                  ctx.lineTo(nodes[j].x, nodes[j].y);
                  ctx.stroke();
              }
          }
      }

      // Обновляем позиции узлов и рисуем их
      for (let i = 0; i < numNodes; i++) {
          nodes[i].x += nodes[i].vx;
          nodes[i].y += nodes[i].vy;

          // Отражаем узлы от краев экрана
          if (nodes[i].x < 0 || nodes[i].x > width) nodes[i].vx *= -1;
          if (nodes[i].y < 0 || nodes[i].y > height) nodes[i].vy *= -1;

          // Рисуем узел
          ctx.beginPath();
          ctx.fillStyle = '#000';
          ctx.arc(nodes[i].x, nodes[i].y, 2, 0, Math.PI * 2);
          ctx.fill();
      }

      requestAnimationFrame(draw);
  }

  function resizeCanvas() {
      width = canvas.width = window.innerWidth;
      height = canvas.height = window.innerHeight;
  }

  onMount(() => {
      init();
      window.addEventListener('resize', resizeCanvas);

      return () => {
          window.removeEventListener('resize', resizeCanvas);
      };
  });

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

<!-- Контейнер -->
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
      продукты и обеспечивали передовыми технологиями стран мира.
    </p>
    <ul>
      <li>Поддержка стартапов и инновационных проектов.</li>
      <li>Образовательные программы для ИТ-специалистов.</li>
      <li>Государственные гранты на разработку новых технологий.</li>
      <li>Стимулирование создания ИТ-компаний в регионах.</li>
    </ul>
  </div>
</div>

<!-- Canvas -->
<canvas bind:this={canvas}></canvas>

<Footer />

<style>
  :global(body, html) {
      margin: 0;
      padding: 0;
      background-color: transparent;
  }
  
  canvas {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      z-index: -1;  
  }

  .container {
      position: relative;
      z-index: 1;
      display: flex;
      max-width: 1200px;
      margin: 50px auto;
      gap: 20px;
      background: transparent;
  }

  .slider {
      flex: 1;
      position: relative;
      border-radius: 15px;
      overflow: hidden;
      box-shadow: 0 8px 25px rgba(0, 0, 0, 0.2);
      /* Можно убрать backdrop-filter отсюда, если не нужно */
      /* background-color и backdrop-filter перенесены в .slide */
  }

  .slides {
      display: flex;
      transition: transform 0.7s ease;
  }

  .slide {
      min-width: 100%;
      background-color: rgba(255, 255, 255, 0.001); /* Полупрозрачный фон */
      border-radius: 15px;
      padding: 20px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      position: relative;
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.5);
      overflow: hidden;
      backdrop-filter: blur(6px); /* Добавлено размытие фона */
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
      background: transparent;
      background-color: rgba(255, 255, 255, 0.001); /* Полупрозрачный фон */
      border-radius: 15px;
      padding: 20px;
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: flex-start;
      backdrop-filter: blur(6px); /* Добавлено размытие фона */
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
