% rebase('base.tpl', title='Editar Mensagem')
<h1>✏️ Editar Mensagem</h1>

<form method="POST" action="/editar/{{m.id}}">
  <label>Texto:</label><br>
  <textarea name="texto" required>{{m.texto}}</textarea><br>

  <label>Categoria:</label><br>
  <select name="categoria" required>
    <option value="motivacional" % if m.categoria == 'motivacional': selected %> >Motivacional</option>
    <option value="reflexiva" % if m.categoria == 'reflexiva': selected %> >Reflexiva</option>
    <option value="espiritual" % if m.categoria == 'espiritual': selected %> >Espiritual</option>
  </select><br>

  <label>Favorita?</label>
  <input type="checkbox" name="favorita" % if m.favorita: checked %> ><br><br>

  <button type="submit">Atualizar</button>
</form>
