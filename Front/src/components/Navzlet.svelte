<script>
    // Вопросы для пользователей
    let goal = "";
    let parsedData = [];
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
    async function getGoals() {
      goals = [];
      userAnswers.forEach((answer, index) => {
        if (answer) {
          goals.push(`Развивайте навык: ${answer}`);
        }
      });
      try {
        let response = await fetch("http://localhost:8000/neural_network", {
          method: "POST", 
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            prompt: goal
          })
        })
        let data = await response.json();
        console.log(data)
        console.log(data.message)
        parsedData = parseGoals(data.message);
        console.log(parsedData)
      } catch(e) {
        console.log(e);
      }
    }

    function parseGoals(input) {
    if (typeof input !== 'string') {
        throw new TypeError('Input must be a string');
    }

    const result = [];
    let currentGoal = null;

    // Регулярные выражения для поиска тегов
    const goalRegex = /\[goal\](.*?)\[\/goal\]/g;
    const subgoalRegex = /\[subgoal\](.*?)\[\/subgoal\]/g;

    // Ищем все цели
    const goals = input.match(goalRegex);

    if (!goals) {
        throw new Error('No valid goals found');
    }

    goals.forEach(goal => {
        // Извлекаем текст цели
        const goalTextMatch = goal.match(/^\[goal\](.*?)(?=\[subgoal\]|\[\/goal\])/);
        const goalText = goalTextMatch ? goalTextMatch[1].trim() : null;

        // Ищем все подцели внутри текущей цели
        const subgoals = [...goal.matchAll(subgoalRegex)].map(match => match[1].trim());

        if (goalText || subgoals.length > 0) {
            result.push({
                goal: goalText || 'Untitled Goal',
                subgoals: subgoals
            });
        }
    });

    return result;
}
  </script>
  
  <style>
    .container {
      max-width: 600px;
      margin: auto;
      text-align: center;
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
    input {
      border: 1px solid;
      border-radius: 7px;
      padding-left: 7px;
    }
    ul {
      list-style: circle;
      text-align: left;
    }
    li {
      list-style: inside;
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

    <input bind:value={goal}/>
    <button on:click={getGoals}>Получить цели</button>
  
    <ul>
      {#each parsedData as { goal, subgoals }}
          <li>
              <strong>{goal}</strong>
              {#if subgoals.length > 0}
                  <ul>
                      {#each subgoals as subgoal}
                          <li>{subgoal}</li>
                      {/each}
                  </ul>
              {/if}
          </li>
      {/each}
  </ul>
  </div>
  