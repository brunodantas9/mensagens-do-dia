
```html
% rebase('base.tpl', title='Nova Mensagem')
<h1>➕ Nova Mensagem</h1>

<form method="POST" action="/nova">
  <label>Texto:</label><br>
  <textarea name="texto" required></textarea><br>

  <label>Categoria:</label><br>
  <select name="categoria" required>
    <option value="motivacional">Motivacional</option>
    <option value="reflexiva">Reflexiva</option>
    <option value="espiritual">Espiritual</option>
  </select><br>

  <label>Favorita?</label>
  <input type="checkbox" name="favorita"><br><br>

  <button type="submit">Salvar</button>
</form>

