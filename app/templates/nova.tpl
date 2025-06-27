
% rebase('base.tpl', title='Nova Mensagem')
<h2>➕ Nova Mensagem</h2>
<form method="POST" action="/nova">
  <textarea name="texto" required placeholder="Digite a mensagem..."></textarea><br>
  <label>Categoria:</label>
  <select name="categoria">
    <option value="motivacional">Motivacional</option>
    <option value="reflexiva">Reflexiva</option>
    <option value="espiritual">Espiritual</option>
  </select><br>
  <label><input type="checkbox" name="favorita"> Favorita</label><br>
  <label>Agendar para:</label>
  <input type="date" name="data_agendada"><br><br>
  <button type="submit">Salvar</button>
</form>
