% rebase('base.tpl', title='Nova Mensagem')

<form method="POST" action="/nova">
  <textarea name="texto" required placeholder="Digite a mensagem..." rows="4"></textarea>
  <select name="categoria">
    <option value="motivacional">Motivacional</option>
    <option value="reflexiva">Reflexiva</option>
    <option value="espiritual">Espiritual</option>
  </select>
  <label><input type="checkbox" name="favorita"> Favorita</label>
  <label>Agendar para: <input type="date" name="data_agendada"></label>
  <button type="submit">Salvar</button>
</form>
