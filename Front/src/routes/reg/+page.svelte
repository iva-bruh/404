<script>
    import Header from "../../components/Header.svelte";
    import Footer from "../../components/Footer.svelte";
    let email = '';
    let password = '';
    let confirmPassword = '';
</script>
<Header>

</Header>
<style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f0f0f0;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        margin: 0;
        padding: 20px; /* Добавляем отступы вокруг страницы */
    }

    .registration-form {
        background-color: white;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        width: 100%;
        max-width: 400px; /* Максимальная ширина формы */
        margin: 0 auto; /* Центрируем форму по горизонтали */
    }

    h2 {
        text-align: center;
        margin-bottom: 20px;
    }

    .form-group {
        margin-bottom: 15px;
    }

    label {
        display: block;
        margin-bottom: 5px;
    }

    input {
        width: 100%;
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 4px;
        font-size: 14px;
    }

    button {
        width: 100%;
        padding: 10px;
        background-color: black; /* Черный цвет кнопки */
        color: white;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        font-size: 16px;
        transition: background-color 0.3s; /* Плавный переход цвета */
    }

    button:hover {
        background-color: #333; /* Темнее черного при наведении */
    }

    .error {
        color: red;
        font-size: 12px;
        margin-top: 5px;
    }
</style>

<div class="registration-form">
    <h2>Регистрация</h2>
    <form>
        <div class="form-group">
            <label for="email">Email:</label>
            <input type="email" id="email" bind:value={email} required />
        </div>
        <div class="form-group">
            <label for="password">Пароль:</label>
            <input type="password" id="password" bind:value={password} required />
        </div>
        <div class="form-group">
            <label for="confirmPassword">Подтвердите пароль:</label>
            <input type="password" id="confirmPassword" bind:value={confirmPassword} required />
        </div>
        <button type="submit">Зарегистрироваться</button>
    </form>
</div>
<Footer>
    
</Footer>