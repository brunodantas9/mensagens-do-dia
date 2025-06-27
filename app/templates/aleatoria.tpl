
% rebase('base.tpl', title='Mensagem Aleatória')
<h1>🎲 Mensagem Aleatória</h1>

% if m:
  <div class="message-card {{m.categoria}} {% if m.favorita %}favorita{% endif %}">
    <p>{{m.texto}}</p>
    <small>Categoria: {{m.categoria}}</small>
  </div>
% else:
  <p>Não há mensagens cadastradas ainda.</p>
% end
