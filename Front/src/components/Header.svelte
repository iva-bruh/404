<header>
  
  <style>
    .header {
      background-color: #333;
      color: white;
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 10px 20px;
    }
  
    .logo img {
      height: 40px;
    }
  
    .nav {
      list-style: none;
      display: flex;
    }
  
    .nav li {
      margin: 0 15px;
    }
  
    .nav a {
      color: white;
      text-decoration: none;
    }

    .auth-buttons {
      display: flex;
      gap: 10px;
    }

    .auth-button {
      background-color: transparent;
      color: white;
      border: 1px solid white;
      padding: 5px 10px;
      border-radius: 5px;
      text-decoration: none;
    }

    .auth-button:hover {
      background-color: white;
      color: #333;
    }
  </style>
  
  <header class="header">
    <div class="logo">
      <img src="logo.png" alt="Логотип компании" />
    </div>
    <nav>
      <ul class="nav">
        <li><a href="/">Главная</a></li>
        <li><a href="/contact">Меры поддержки</a></li>
        <li><a href="/about">О нас</a></li>
        <li><a href="/services">Услуги</a></li>
        <li><a href="/contact">Контакты</a></li>
       
      </ul>
    </nav>
    <div class="auth-buttons">
      <a href="/auth" class="auth-button">Вход</a>
      <a href="/reg" class="auth-button">Регистрация</a>
      <a href="/" class="auth-button">Личный кабинет</a>
    </div>  
  </header>
</header>