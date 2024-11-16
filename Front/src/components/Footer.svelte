<script>
  export let isMainPage = "false";
</script>

<footer>
  <style>
    .footer {
      height: 50px;
      background-color: #333;
      color: white;
      text-align: center;
      left: 0;
      bottom: 0;
      width: 100%; 
      z-index: 2;
    }
  
    .footer-links {
      list-style: none;
      padding: 0;
      display: flex;
      justify-content: center;
      align-items: center;
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
  
  <footer class="footer" style={isMainPage == "true" ? "position: fixed" : ""}>
    <div class="copyright">
      © 2024 Мозгов нет. Права защищать не будем.
    </div>
  </footer>
</footer>