% rebase('base.tpl', title='Mensagem do Dia')
<h1>📅 Mensagem de Hoje</h1>

% if m:
  <div class="message-card {{m.categoria}} {% if m.favorita %}favorita{% endif %}">
    <p>{{m.texto}}</p>
    <small>Categoria: {{m.categoria}}</small>
  </div>
% else:
  <p>Não há mensagem cadastrada para hoje.</p>
% end

