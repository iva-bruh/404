<footer>
  <style>
    .footer {
      background-color: #333;
      color: white;
      padding: 20px;
      text-align: center;
      position: fixed; /* Фиксированное положение */
      left: 0; /* Прилепить к левому краю */
      bottom: 0; /* Прилепить к нижнему краю */
      width: 100%; /* Занимать всю ширину */
      z-index: 1000; /* Убедиться, что футер находится наверху других элементов */
    }
  
    .footer-links {
      list-style: none;
      padding: 0;
      display: flex;
      justify-content: center;
      flex-wrap: wrap;
    }
  
    .footer-links li {
      margin: 0 15px;
    }
  
    .footer-links a {
      color: white;
      text-decoration: none;
    }
  
    .copyright {
      margin-top: 15px;
      font-size: 14px;
    }
  </style>
  
  <footer class="footer">
    <div class="copyright">
      © 2024 Мозгов нет. Права защищать не будем.
    </div>
  </footer>
</footer>