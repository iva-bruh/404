<script>
    import { onMount } from "svelte";
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
        event.target.value = ""; // Сбросить выбор файла (для тестирования)
    }

    // Функция для удаления файла из списка
    function removeFile(fileToRemove) {
        files = files.filter(file => file !== fileToRemove);
    }
</script>

<style>
    .container {
        padding: 20px;
        background-color: white;
        border-radius: 8px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        max-width: 600px;
        margin: auto;
    }

    h1 {
        text-align: center;
    }

    input[type="file"] {
        display: block;
        margin: 20px 0;
    }

    .file-list {
        list-style-type: none;
        padding: 0;
    }

    .file-item {
        display: flex;
        justify-content: space-between;
        margin: 5px 0;
        padding: 8px;
        background-color: #f9f9f9;
        border-radius: 4px;
    }

    button {
        cursor: pointer;
        background-color: #ff4d4d;
        border: none;
        color: white;
        padding: 5px 10px;
        border-radius: 4px;
    }

    button:hover {
        background-color: #ff1a1a;
    }
</style>

<div class="container">
    <h1>Личный кабинет</h1>

    <input type="file" accept=".jpeg, .jpg, .png, .pdf" on:change={handleFileUpload} multiple />
    
    {#if message}
        <p>{message}</p>
    {/if}

    <h2>Загруженные достижения:</h2>
    <ul class="file-list">
        {#each files as file}
            <li class="file-item">
                {file.name}
                <button on:click={() => removeFile(file)}>Удалить</button>
            </li>
        {/each}
    </ul>
</div>
