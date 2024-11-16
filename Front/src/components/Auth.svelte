<script>
    let email = '';
    let password = '';
    import Header from "./Header.svelte";
    import Footer from "./Footer.svelte";
    let loggedIn = false;
    import { redirect } from "@sveltejs/kit";
    let Auth = async () => {
        try {
            const formData = new FormData();
            formData.append('username', email);
            formData.append('password', password);
            let response = await fetch("http://localhost:8000/login", {
                credentials: "include",
                method: "POST",
                body: formData
            })
            let data = await response.json();
            console.log(data);
            if (response.ok) {
                loggedIn = true;
            }

        } catch (e) {
            console.log(e);
        }
        if (loggedIn) {
            redirect(307, "/cabinet")
        }
    }
</script>
<Header />
<style>
    .login-form {
        background-color: white;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        width: 100%;
        max-width: 400px; /* Максимальная ширина формы */
        margin: 0 auto; /* Центрируем форму по горизонтали */
        margin-top: 30px;
        margin-bottom: 20px;
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

<div class="login-form">
    <h2>Вход</h2>
    <form>
        <div class="form-group">
            <label for="email">Email:</label>
            <input type="email" id="email" bind:value={email} required />
        </div>
        <div class="form-group">
            <label for="password">Пароль:</label>
            <input type="password" id="password" bind:value={password} required />
        </div>
        <button type="submit" on:click={Auth}>Войти</button>
    </form>
</div>
<Footer isMainPage="true"/>