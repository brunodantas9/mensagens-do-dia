% rebase('base.tpl', title='Editar Mensagem')
<h2>✏️ Editar Mensagem</h2>
<form method="POST" action="/editar/{{m['id']}}">
  <textarea name="texto" required>{{m['texto']}}</textarea><br>
  <label>Categoria:</label>
  <select name="categoria">
    <option value="motivacional" {{'selected' if m['categoria']=='motivacional' else ''}}>Motivacional</option>
    <option value="reflexiva" {{'selected' if m['categoria']=='reflexiva' else ''}}>Reflexiva</option>
    <option value="espiritual" {{'selected' if m['categoria']=='espiritual' else ''}}>Espiritual</option>
  </select><br>
  <label><input type="checkbox" name="favorita" {{'checked' if m['favorita'] else ''}}> Favorita</label><br>
  <label>Agendar para:</label>
  <input type="date" name="data_agendada" value="{{m['data_agendada']}}"><br><br>
  <button type="submit">Salvar Alterações</button>
</form>
