% rebase('base.tpl', title='Mensagem Aleatória')
<h2>🎲 Mensagem Aleatória</h2>
% if m:
  <div class="message-card {{m.categoria}} {% if m.favorita %}favorita{% endif %}">
    <p>{{m.texto}}</p>
    <small><strong>Categoria:</strong> {{m.categoria}}</small>
  </div>
% else:
  <p>Nenhuma mensagem disponível.</p>
% end
