% rebase('base.tpl', title='Mensagens do Dia')

<form method="GET" action="/mensagens">
  <input type="text" name="q" placeholder="Buscar mensagem..." value="{{q or ''}}">
  <select name="categoria">
    <option value="">Todas</option>
    <option value="motivacional" {{'selected' if categoria=='motivacional' else ''}}>Motivacional</option>
    <option value="reflexiva" {{'selected' if categoria=='reflexiva' else ''}}>Reflexiva</option>
    <option value="espiritual" {{'selected' if categoria=='espiritual' else ''}}>Espiritual</option>
  </select>
  <button type="submit">🔍 Filtrar</button>
</form>

<p>Total de mensagens: {{total}}</p>

% for m in mensagens:
  <div class="message-card {{m['categoria']}} {% if m['favorita'] %}favorita{% endif %}">
    <p>{{m['texto']}}</p>
    <small><strong>Categoria:</strong> {{m['categoria']}}</small><br>
    <a href="/ver/{{m['id']}}">🔍 Ver</a>
    <a href="/editar/{{m['id']}}">✏️ Editar</a>
    <a href="/deletar/{{m['id']}}" onclick="return confirmarRemocao()">🗑️ Excluir</a>
  </div>
% end
