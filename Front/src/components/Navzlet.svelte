<script>
    // Вопросы для пользователей
    let goal = "";
    let parsedData = [];
    let buttonVisible = true;
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
      buttonVisible = false;
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
            prompt: goal,
            answers: userAnswers
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

    function parseGoals(text) {
    const regex = /\[(goal|subgoal)\](.*?)\[\/\1\]/gs;
    const matches = [...text.matchAll(regex)];
    const result = [];
    let currentGoal = null;

    for (const match of matches) {
        const [fullMatch, tag, content] = match;
        const trimmedContent = content.trim();

        if (tag === 'goal') {
            currentGoal = [trimmedContent, []];
            result.push(currentGoal);
        } else if (tag === 'subgoal') {
            if (currentGoal) {
                currentGoal[1].push(trimmedContent);
            }
        }
    }

    return result;
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
    input {
      border: 1px solid;
      border-radius: 7px;
      padding-left: 7px;
    }
    ul {
      list-style: circle;
      text-align: left;
    }
    ul ul {
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
    {#if buttonVisible}
      <button on:click={getGoals}>Получить цели</button>
    {/if}
  
    <ul>
      {#each parsedData as [goal, subgoals]}
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
  