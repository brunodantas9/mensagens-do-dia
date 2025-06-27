% rebase('base.tpl', title='Favoritas')
<h1>⭐ Mensagens Favoritas</h1>

% for m in mensagens:
  <div class="message-card {{m.categoria}} favorita">
    <p>{{m.texto}}</p>
    <small>Categoria: {{m.categoria}}</small><br>
    <a href="/ver/{{m.id}}">🔍 Ver</a>
  </div>
% end
