<script>
    let files = [];
    let message = "";
    
    // Основные типы файлов, которые мы принимаем
    const acceptedFileTypes = ["image/jpeg", "image/png", "application/pdf"];
    
    // Функция валидации загружаемого файла
    function validateFile(file) {
        if (!acceptedFileTypes.includes(file.type)) {
            message = "Только файлы форматов JPEG, PNG и PDF разрешены.";
            return false;
        }
        return true;
    }

    // Функция для обработки загрузки файла
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

    // Функция для удаления файла из списка
    function removeFile(fileToRemove) {
        files = files.filter(file => file !== fileToRemove);
    }
</script>

<style>
    * {
        box-sizing: border-box;
    }
    
    body {
        background-color: #f2f3f7;
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 0;
    }

    .container {
        padding: 40px;
        background-color: white;
        border-radius: 10px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        max-width: 600px;
        margin: 50px auto;
        border: 1px solid #e1e1e1;
    }

    h1 {
        text-align: center;
        color: #333;
        margin-bottom: 20px;
    }

    input[type="file"] {
        display: block;
        margin: 20px auto;
        padding: 10px;
        border: 2px dashed #4CAF50;
        border-radius: 5px;
        background-color: #fafafa;
        cursor: pointer;
        transition: border-color 0.2s ease;
    }

    input[type="file"]:hover {
        border-color: #45a049;
    }

    .message {
        text-align: center;
        color: #ff5722;
        font-weight: bold;
        margin: 10px 0;
    }

    h2 {
        margin: 20px 0 10px;
        color: #666;
    }

    .file-list {
        list-style-type: none;
        padding: 0;
    }

    .file-item {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: #f9f9f9;
        padding: 10px 15px;
        border-radius: 5px;
        margin: 5px 0;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    }

    .file-item:hover {
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
        .container {
            padding: 20px;
        }

        h1 {
            font-size: 1.5rem;
        }

        input[type="file"], 
        .remove-button {
            width: 100%;
        }
    }
</style>

<div class="container">
    <h1>Личный кабинет</h1>

    <input type="file" accept=".jpeg, .jpg, .png, .pdf" on:change={handleFileUpload} multiple />
    
    {#if message}
        <p class="message">{message}</p>
    {/if}

    <h2>Загруженные достижения:</h2>
    <ul class="file-list">
        {#each files as file}
            <li class="file-item">
                {file.name}
                <button class="remove-button" on:click={() => removeFile(file)}>Удалить</button>
            </li>
        {/each}
    </ul>
</div>