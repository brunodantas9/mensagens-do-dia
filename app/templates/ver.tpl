
% rebase('base.tpl', title='Ver Mensagem')
<h1>🔍 Mensagem</h1>

<div class="message-card {{m.categoria}} {% if m.favorita %}favorita{% endif %}">
  <p>{{m.texto}}</p>
  <small>Categoria: {{m.categoria}}</small><br>
  <small>Favorita: {{'Sim' if m.favorita else 'Não'}}</small>
</div>

<a href="/mensagens">← Voltar</a>

