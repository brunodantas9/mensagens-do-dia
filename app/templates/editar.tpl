% rebase('base.tpl', title='Editar Mensagem')

<form method="POST" action="/editar/{{m['id']}}">
  <textarea name="texto" required rows="4">{{m['texto']}}</textarea>
  <select name="categoria">
    <option value="motivacional" {{'selected' if m['categoria']=='motivacional' else ''}}>Motivacional</option>
    <option value="reflexiva" {{'selected' if m['categoria']=='reflexiva' else ''}}>Reflexiva</option>
    <option value="espiritual" {{'selected' if m['categoria']=='espiritual' else ''}}>Espiritual</option>
  </select>
  <label><input type="checkbox" name="favorita" {{'checked' if m['favorita'] else ''}}> Favorita</label>
  <label>Agendar para: <input type="date" name="data_agendada" value="{{m['data_agendada']}}"></label>
  <button type="submit">Salvar Alterações</button>
</form>
