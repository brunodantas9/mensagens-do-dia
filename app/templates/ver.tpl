% rebase('base.tpl', title='Ver Mensagem')

<div class="message-card {{m['categoria']}} {% if m['favorita'] %}favorita{% endif %}">
  <p>{{m['texto']}}</p>
  <small><strong>Categoria:</strong> {{m['categoria']}}</small><br>
  <small><strong>Agendada para:</strong> {{m['data_agendada'] or 'Não agendada'}}</small>
</div>
<a href="/mensagens">⬅ Voltar</a>
