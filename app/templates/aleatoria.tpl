% rebase('base.tpl', title='Mensagem Aleatória')

% if m:
  <div class="message-card {{m['categoria']}} {% if m['favorita'] %}favorita{% endif %}">
    <p>{{m['texto']}}</p>
    <small><strong>Categoria:</strong> {{m['categoria']}}</small>
  </div>
% else:
  <p>Nenhuma mensagem disponível no momento.</p>
% end
