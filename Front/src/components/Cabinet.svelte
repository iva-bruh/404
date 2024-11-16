<script>
    let user = {
        name: "Иван Иванов",
        email: "ivan.ivanov@example.com",
        phone: "+7 (123) 456-78-90",
        age: 28,
        bio: "Привет! Я разработчик, который любит Svelte и всё связанное с веб-технологиями."
    };

    let files = [];
    let achievements = [];
    let newAchievement = "";
    let message = "";
    let activeSection = 'info'; // Флаг для активного раздела

    const acceptedFileTypes = ["image/jpeg", "image/png", "application/pdf"];

    function validateFile(file) {
        if (!acceptedFileTypes.includes(file.type)) {
            message = "Только файлы форматов JPEG, PNG и PDF разрешены.";
            return false;
        }
        return true;
    }

    function handleFileUpload(event) {
        const selectedFiles = Array.from(event.target.files);
        const validFiles = [];

        selectedFiles.forEach(file => {
            if (validateFile(file)) {
                validFiles.push(file);
                message = "Файл успешно загружен!";
            } else {
                message = "Ошибка: " + file.name;
            }
        });

        files = [...files, ...validFiles];
        event.target.value = ""; // Сбросить выбор файла
    }

    function removeFile(fileToRemove) {
        files = files.filter(file => file !== fileToRemove);
    }

    function addAchievement() {
        if (newAchievement.trim() !== "") {
            achievements.push(newAchievement);
            newAchievement = ""; // Очистить поле ввода
            message = "Достижение успешно добавлено!";
        } else {
            message = "Введите достижение для добавления.";
        }
    }

    function removeAchievement(achievementToRemove) {
        achievements = achievements.filter(achievement => achievement !== achievementToRemove);
    }

    function setActiveSection(section) {
        activeSection = section; // Установить активный раздел
    }
</script>

<style>
    * {
        box-sizing: border-box;
    }

    body {
        display: flex;
        margin: 0;
        background-color: #f2f3f7;
        font-family: Arial, sans-serif;
    }

    .sidebar {
        width: 200px;
        background-color: white;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        position: fixed;
        height: 100%;
        padding: 20px;
        overflow-y: auto;
        border-right: 1px solid #e1e1e1;
    }

    .sidebar h2 {
        margin-top: 0;
        font-size: 1.2rem;
        color: #333;
    }

    .sidebar ul {
        list-style: none;
        padding: 0;
    }

    .sidebar ul li {
        margin: 10px 0;
        cursor: pointer;
        padding: 8px;
        border-radius: 4px;
        transition: background-color 0.3s;
    }

    .sidebar ul li:hover {
        background-color: #f2f2f2;
    }

    .sidebar ul li.active {
        background-color: #d9d9d9; /* Новый цвет для активной вкладки */
    }

    .content {
        margin-left: 220px; /* Для учёта ширины бокового меню */
        padding: 40px;
        width: calc(100% - 220px);
    }

    .info-item {
        margin: 5px 0;
    }

    input[type="file"], input[type="text"] {
        display: block;
        margin: 20px auto;
        padding: 10px;
        border-radius: 5px;
        background-color: #fafafa;
        border: 1px solid #ccc;
        width: 100%;
    }

    .message {
        text-align: center;
        color: #ff5722;
        font-weight: bold;
        margin: 10px 0;
    }

    .file-list, .achievement-list {
        list-style-type: none;
        padding: 0;
    }

    .file-item, .achievement-item {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: #f9f9f9;
        padding: 10px 15px;
        border-radius: 5px;
        margin: 5px 0;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    }

    .file-item:hover, .achievement-item:hover {
        background-color: #e9e9e9;
        transition: background-color 0.2s ease;
    }

    .remove-button {
        cursor: pointer;
        background-color: #f44336;
        border: none;
        color: white;
        padding: 5px 10px;
        border-radius: 5px;
        transition: background-color 0.3s;
    }

    .remove-button:hover {
        background-color: #d32f2f;
    }

    @media (max-width: 700px) {
        .sidebar {
            width: 100%; /* Полная ширина на маленьких экранах */
            position: relative;
            height: auto;
        }

        .content {
            margin-left: 0;
            width: 100%; /* Полная ширина на маленьких экранах */
        }
    }
</style>

<div class="sidebar">
    <h2>Меню</h2>
    <ul>
        <li class={activeSection === 'info' ? 'active' : ''} on:click={() => setActiveSection('info')}>Личная информация</li>
        <li class={activeSection === 'files' ? 'active' : ''} on:click={() => setActiveSection('files')}>Загруженные файлы</li>
        <li class={activeSection === 'achievements' ? 'active' : ''} on:click={() => setActiveSection('achievements')}>Достижения</li>
    </ul>
</div>

<div class="content">
    {#if activeSection === 'info'}
        <div class="personal-info">
            <h2>Личная информация</h2>
            <div class="info-item"><strong>Имя:</strong> {user.name}</div>
            <div class="info-item"><strong>Email:</strong> {user.email}</div>
            <div class="info-item"><strong>Телефон:</strong> {user.phone}</div>
            <div class="info-item"><strong>Возраст:</strong> {user.age}</div>
            <div class="info-item"><strong>О себе:</strong> {user.bio}</div>
        </div>
    {:else if activeSection === 'files'}
        <h2>Загруженные файлы:</h2>
        <input type="file" accept=".jpeg, .jpg, .png, .pdf" on:change={handleFileUpload} multiple />
        
        {#if message}
            <p class="message">{message}</p>
        {/if}

        <ul class="file-list">
            {#each files as file}
                <li class="file-item">
                    {file.name}
                    <button class="remove-button" on:click={() => removeFile(file)}>Удалить</button>
                </li>
            {/each}
        </ul>
    {:else if activeSection === 'achievements'}
        <h2>Добавить достижение:</h2>
        <input type="text" bind:value={newAchievement} placeholder="Введите ваше достижение" />
        <button class="remove-button" on:click={addAchievement}>Добавить</button>

        <h2>Ваши достижения:</h2>
        <ul class="achievement-list">
            {#each achievements as achievement}
                <li class="achievement-item">
                    {achievement}
                    <button class="remove-button" on:click={() => removeAchievement(achievement)}>Удалить</button>
                </li>
            {/each}
        </ul>
    {/if}
</div>
