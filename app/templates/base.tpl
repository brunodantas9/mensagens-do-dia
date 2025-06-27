<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>{{title}}</title>
  <link rel="stylesheet" href="/static/css/style.css">
  <script src="/static/js/script.js" defer></script>
</head>
<body>

  <header>
    <h1>{{title or 'Mensagens do Dia'}}</h1>
    <div class="atalhos">
      <a href="/mensagens">🏠 Início</a> |
      <a href="/nova">➕ Nova</a> |
      <a href="/favoritas">⭐ Favoritas</a> |
      <a href="/hoje">📅 Hoje</a> |
      <a href="/aleatoria">🎲 Aleatória</a>
    </div>
    <hr>
  </header>

  <main>
    {{!base}}
  </main>

  <footer style="margin-top: 40px; font-size: 0.9em; color: #888;">
    Projeto BMVC · <strong>brunodantas9</strong>
  </footer>

</body>
</html>

