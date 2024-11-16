<script>
    // Вопросы для пользователей
    let questions = [
      {
        question: "Что для вас наиболее важно в работе?",
        options: ["Карьера", "Деньги", "Развитие", "Команда"]
      },
      {
        question: "Какой навык вы хотите развить?",
        options: ["Программирование", "Коммуникации", "Управление проектами", "Дизайн"]
      },
      {
        question: "Что вас мотивирует?",
        options: ["Новые вызовы", "Признание", "Финансовая стабильность", "Забота о людях"]
      }
    ];
  
    // Переменные для состояния
    let userAnswers = Array(questions.length).fill(null);
    let goals = [];
    
    // Функция для получения целей на основе ответов пользователя
    function getGoals() {
      goals = [];
      userAnswers.forEach((answer, index) => {
        if (answer) {
          goals.push(`Развивайте навык: ${answer}`);
        }
      });
    }
  </script>
  
  <style>
    .container {
      max-width: 600px;
      margin: auto;
      text-align: center;
      margin-top: 10px;
    }
  
    .question {
      margin: 20px 0;
      font-size: 1.2em;
    }
  
    .option {
      margin: 10px 0;
      background-color: #f0f0f0;
      padding: 10px;
      border-radius: 5px;
      cursor: pointer;
      transition: background-color 0.3s ease;
    }
  
    .option:hover {
      background-color: #d0d0d0;
    }
  
    button {
      margin-top: 20px;
      padding: 10px 20px;
      background-color: #1e90ff;
      color: white;
      border: none;
      border-radius: 5px;
      cursor: pointer;
      font-size: 1.2em;
      margin-bottom: 10px;
    }
  
    button:hover {
      background-color: #1c86ee;
    }
  
    .goals {
      margin-top: 30px;
      text-align: left;
    }
    .option.selected {
        background-color: #1e90ff; /* Цвет выделенной опции */
        color: white;
    }
    h1{
      font-size: 25px;
    }
  </style>
  
  <div class="container">
    <h1>На взлёт!</h1>
    <p>Ответьте на вопросы, чтобы выстроить индивидуальную траекторию.</p>
  
    {#each questions as { question, options }, index}
    <div class="question">{question}</div>
    {#each options as option}
        <div class="option {userAnswers[index] === option ? 'selected' : ''}" 
             on:click={() => userAnswers[index] = option}>
            {option}
        </div>
    {/each}
{/each}

  
    <button on:click={getGoals}>Получить цели</button>
  
    {#if goals.length > 0}
      <div class="goals">
        <h2>Ваши цели:</h2>
        <ul>
          {#each goals as goal}
            <li>{goal}</li>
          {/each}
        </ul>
      </div>
    {/if}
  </div>
  