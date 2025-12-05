# Contribuindo para Multi-Agents-IA

Primeiramente, obrigado por considerar contribuir com o Multi-Agents-IA! 🎉

## 📋 Tabela de Conteúdos

- [Código de Conduta](#código-de-conduta)
- [Como Posso Contribuir?](#como-posso-contribuir)
  - [Reportando Bugs](#reportando-bugs)
  - [Sugerindo Melhorias](#sugerindo-melhorias)
  - [Pull Requests](#pull-requests)
- [Guia de Estilo](#guia-de-estilo)
- [Configuração do Ambiente](#configuração-do-ambiente)

---

## 📜 Código de Conduta

Este projeto adota o Código de Conduta do Contributor Covenant. Ao participar, espera-se que você mantenha este código. Por favor, reporte comportamentos inaceitáveis.

---

## 🤝 Como Posso Contribuir?

### 🐛 Reportando Bugs

Antes de criar um bug report, verifique se o problema já não foi reportado. Ao criar um novo issue:

1. Use um título claro e descritivo
2. Descreva os passos exatos para reproduzir o problema
3. Descreva o comportamento esperado vs o comportamento atual
4. Inclua screenshots se aplicável
5. Inclua sua versão do Python e das dependências

### 💡 Sugerindo Melhorias

Sugestões de melhorias são bem-vindas! Para sugerir:

1. Use um título claro e descritivo
2. Forneça uma descrição detalhada da melhoria
3. Explique por que essa melhoria seria útil
4. Liste exemplos de como a melhoria funcionaria

### 🔧 Pull Requests

1. **Fork** o repositório
2. **Clone** seu fork: `git clone https://github.com/seu-usuario/Multi-Agents-IA.git`
3. **Crie uma branch**: `git checkout -b feature/minha-feature`
4. **Faça suas alterações** e commite: `git commit -m 'feat: adiciona minha feature'`
5. **Push** para a branch: `git push origin feature/minha-feature`
6. Abra um **Pull Request**

#### Convenção de Commits

Usamos [Conventional Commits](https://www.conventionalcommits.org/):

| Tipo | Descrição |
|------|-----------|
| `feat` | Nova funcionalidade |
| `fix` | Correção de bug |
| `docs` | Apenas documentação |
| `style` | Formatação, sem alteração de código |
| `refactor` | Refatoração de código |
| `test` | Adição ou correção de testes |
| `chore` | Manutenção, dependências, etc. |

**Exemplos:**
```
feat: adiciona guardrails para validação de outputs
fix: corrige erro de encoding no escritor
docs: atualiza README com instruções de instalação
```

---

## 🎨 Guia de Estilo

### Python

- Use **Black** para formatação: `black .`
- Use **isort** para ordenar imports: `isort .`
- Siga a **PEP 8**
- Use **type hints** quando possível
- Docstrings em português ou inglês (seja consistente)

### Commits

- Use verbos no imperativo: "adiciona", não "adicionado"
- Primeira letra minúscula
- Sem ponto final
- Limite de 72 caracteres na primeira linha

---

## ⚙️ Configuração do Ambiente

### Pré-requisitos

- Python 3.10+
- Git
- IDE recomendada: **[AntiGravity](https://antigravity.dev)** 🚀 - A IDE agentic utilizada no desenvolvimento deste projeto

### Instalação para Desenvolvimento

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/Multi-Agents-IA.git
cd Multi-Agents-IA

# Crie o ambiente virtual
python -m venv .venv

# Ative o ambiente virtual
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

# Instale as dependências de desenvolvimento
pip install -e ".[dev]"

# Configure o pre-commit
pre-commit install

# Configure as variáveis de ambiente
cp .env.example .env
# Edite .env com suas chaves de API
```

### Executando Testes

```bash
# Rodar todos os testes
pytest

# Rodar com cobertura
pytest --cov=. --cov-report=html

# Rodar apenas um arquivo de teste
pytest tests/test_crew.py
```

### Verificações de Qualidade

```bash
# Formatação
black .
isort .

# Linting
flake8 .

# Type checking
mypy .
```

---

## 🙏 Agradecimentos

Obrigado por contribuir! Sua ajuda é muito apreciada. ❤️
