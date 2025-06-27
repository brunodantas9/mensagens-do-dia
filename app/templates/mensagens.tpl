% rebase('base.tpl', title='Mensagens do Dia')
<h1>🌟 Mensagens do Dia 🌟</h1>

<form method="GET" action="/mensagens">
  <input type="text" name="q" placeholder="Buscar mensagem..." value="{{q or ''}}">
  <select name="categoria">
    <option value="">Todas</option>
    <option value="motivacional" % if categoria == 'motivacional': selected %>Motivacional</option>
    <option value="reflexiva" % if categoria == 'reflexiva': selected %>Reflexiva</option>
    <option value="espiritual" % if categoria == 'espiritual': selected %>Espiritual</option>
  </select>
  <button type="submit">Filtrar</button>
</form>

<p>Total de mensagens: {{total}}</p>

<div class="atalhos">
  <a href="/nova">➕ Nova Mensagem</a> |
  <a href="/favoritas">⭐ Favoritas</a> |
  <a href="/hoje">📅 Hoje</a> |
  <a href="/aleatoria">🎲 Aleatória</a>
</div>

<hr>

% for m in mensagens:
  <div class="message-card {{m.categoria}} {% if m.favorita %}favorita{% endif %}">
    <p>{{m.texto}}</p>
    <small><strong>Categoria:</strong> {{m.categoria}}</small><br>
    <a href="/ver/{{m.id}}">🔍 Ver</a> |
    <a href="/editar/{{m.id}}">✏️ Editar</a> |
    <a href="/deletar/{{m.id}}" onclick="return confirmarRemocao()">🗑️ Excluir</a>
  </div>
% end
