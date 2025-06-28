% rebase('base.tpl', title='Mensagens do Dia')

<div class="container">
  <h2>🌟 Mensagens do Dia 🌟</h2>

  <form class="search-form">
    <input type="text" name="q" value="{{q or ''}}" placeholder="Buscar mensagem...">
    <select name="categoria">
      <option value="">Todas</option>
      <option value="motivacional" {{'selected' if categoria == 'motivacional' else ''}}>Motivacional</option>
      <option value="reflexiva" {{'selected' if categoria == 'reflexiva' else ''}}>Reflexiva</option>
      <option value="espiritual" {{'selected' if categoria == 'espiritual' else ''}}>Espiritual</option>
    </select>
    <button type="submit">🔍 Filtrar</button>
  </form>

  <p>Total de mensagens: {{total}}</p>

  <div class="actions">
    <a href="/nova">🆕 Nova Mensagem</a> |
    <a href="/favoritas">⭐ Favoritas</a> |
    <a href="/hoje">🏠 Hoje</a> |
    <a href="/aleatoria">🎲 Aleatória</a>
  </div>

  % for m in mensagens:
    <div class="message-card {{m.categoria}} {% if m.favorita %}favorita{% endif %}">
      <p>{{m.texto}}</p>
      <p><strong>Categoria:</strong> {{m.categoria}}</p>
      <div class="message-actions">
        <a href="/ver/{{m.id}}">👤 Ver</a> |
        <a href="/editar/{{m.id}}">✏️ Editar</a> |
        <a href="/deletar/{{m.id}}">🗑️ Excluir</a>
      </div>
    </div>
  % end
</div>
