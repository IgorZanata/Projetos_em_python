<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Meu Buscador de CEP</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      padding: 30px;
      max-width: 400px;
      margin: 0 auto;
    }
    input, button {
      padding: 10px;
      font-size: 16px;
      margin-bottom: 10px;
      width: 100%;
      box-sizing: border-box;
    }
    button {
      background-color: #007bff;
      color: white;
      border: none;
      cursor: pointer;
      border-radius: 5px;
    }
    button:hover {
      background-color: #0056b3;
    }
    .resultado {
      margin-top: 15px;
      background: #f4f4f4;
      padding: 15px;
      border-radius: 5px;
    }
  </style>
</head>
<body>

  <h2>🔍 Buscador de CEP</h2>
  
  <!-- Onde o usuário digita -->
  <input type="text" id="meuCep" placeholder="Digite o CEP (ex: 01001000)" />
  
  <!-- O botão que dispara a busca -->
  <button onclick="buscarEndereco()">Buscar Endereço</button>

  <!-- Onde as respostas vão aparecer na tela -->
  <div class="resultado">
    <p><strong>Rua:</strong> <span id="rua">-</span></p>
    <p><strong>Bairro:</strong> <span id="bairro">-</span></p>
    <p><strong>Cidade:</strong> <span id="cidade">-</span></p>
  </div>

  <script>
    function buscarEndereco() {
      // 1. Pega o CEP digitado no campo da tela
      const cep = document.getElementById('meuCep').value;

      // 2. Faz o pedido para a API usando o CEP digitado
      fetch(`https://viacep.com.br/ws/${cep}/json/`)
        .then(resposta => resposta.json())
        .then(dados => {
          // 3. Coloca os dados recebidos direto na tela!
          document.getElementById('rua').innerText = dados.logradouro || 'Não encontrado';
          document.getElementById('bairro').innerText = dados.bairro || 'Não encontrado';
          document.getElementById('cidade').innerText = `${dados.localidade} - ${dados.uf}`;
        })
        .catch(erro => {
          alert('Ops! Verifique se o CEP foi digitado corretamente.');
        });
    }
  </script>

</body>
</html>