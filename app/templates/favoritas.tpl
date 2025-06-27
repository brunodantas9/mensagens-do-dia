% rebase('base.tpl', title='Mensagens Favoritas')
<h2>⭐ Mensagens Favoritas</h2>
% if mensagens:
  % for m in mensagens:
    <div class="message-card {{m['categoria']}} favorita">
      <p>{{m['texto']}}</p>
      <small><strong>Categoria:</strong> {{m['categoria']}}</small><br>
      <a href="/ver/{{m['id']}}">🔍 Ver</a> |
      <a href="/editar/{{m['id']}}">✏️ Editar</a> |
      <a href="/deletar/{{m['id']}}" onclick="return confirmarRemocao()">🗑️ Excluir</a>
    </div>
  % end
% else:
  <p>Nenhuma mensagem favorita encontrada.</p>
% end

