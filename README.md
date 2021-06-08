<h1>Project Solution Cadmus</h1>
<h3>Projeto Python utilizando biblioteca Requests, Xlsxwriter e SMPTlib</h3>
<br>
<br>
<strong>Detalhes do projeto:</strong>
<br>
<br>
Esta é uma proposta de solução para o teste técnico da Cadmus. Neste projeto é automatizado o processo de busca de dados 
das vagas abertas da Cadmus pelo seu portal através da biblioteca Requests, onde foram analisadas as requisições feitas 
pelo front-end do site e encontrada a API de oportunidades (https://apisf.cadmus.com.br/api/opportunity/listOpportunity/)
e tratado o json retornado. Após isso são gravados o nome, local e descrição da vaga em um arquivo de Excel
através da biblioteca Xlsxwriter.

Por fim, os dados são enviados por e-mail utilizando a biblioteca SMTPlib. Os dados não foram configurados, ilustrando
que devem ser configurado em ambiente produtivo com a utilização de variáveis de ambiente. O servidor utilizado deve
ser um servidor SMTP, no caso de gmail ou outlook, deve ser habilitada a conexão de outros clients (less secure apps).