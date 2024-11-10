// backend/server.js

const express = require('express');
const app = express();

// Porta do servidor
const PORT = process.env.PORT || 3000;

// Middleware para analisar dados JSON
app.use(express.json());

// Rota para a página inicial
app.get('/', (req, res) => {
  res.sendFile(__dirname + '/frontend/index.html');
});

// ... (Adicionar mais rotas e lógica aqui)

// Iniciar o servidor
app.listen(PORT, () => {
  console.log(`Servidor rodando na porta ${PORT}`);
});

// backend/server.js
// ... (código anterior)

// Iniciar o servidor
app.listen(PORT, '200.98.199.199', () => {
  console.log(`Servidor rodando na porta ${PORT}`);
});