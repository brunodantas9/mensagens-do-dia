% rebase('base.tpl', title='Editar Mensagem')
<h2>✏️ Editar Mensagem</h2>
<form method="POST" action="/editar/{{m.id}}">
  <textarea name="texto" required>{{m.texto}}</textarea><br>
  <label>Categoria:</label>
  <select name="categoria">
    <option value="motivacional" % if m.categoria=='motivacional': selected %>Motivacional</option>
    <option value="reflexiva" % if m.categoria=='reflexiva': selected %>Reflexiva</option>
    <option value="espiritual" % if m.categoria=='espiritual': selected %>Espiritual</option>
  </select><br>
  <label><input type="checkbox" name="favorita" % if m.favorita: checked %>> Favorita</label><br>
  <label>Agendar para:</label>
  <input type="date" name="data_agendada" value="{{m.data_agendada}}"><br><br>
  <button type="submit">Salvar Alterações</button>
</form>

