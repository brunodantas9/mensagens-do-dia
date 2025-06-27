% rebase('base.tpl', title='Mensagem de Hoje')

% if m:
  <div class="message-card {{m['categoria']}} {% if m['favorita'] %}favorita{% endif %}">
    <p>{{m['texto']}}</p>
    <small><strong>Categoria:</strong> {{m['categoria']}}</small><br>
    <small><strong>Agendada para:</strong> {{m['data_agendada']}}</small>
  </div>
% else:
  <p>Nenhuma mensagem agendada para hoje.</p>
% end
