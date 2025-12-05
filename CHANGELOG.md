# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Versionamento Semântico](https://semver.org/lang/pt-BR/).

## [Unreleased]

### Planejado
- Adicionar guardrails para validação de outputs
- Implementar testes automatizados
- Adicionar suporte a Docker

---

## [1.0.0] - 2024-12-05

### Adicionado
- 🚀 Sistema multi-agentes com CrewAI
- 🤖 5 agentes especializados:
  - **Gerente**: Coordena a equipe e delega tarefas
  - **Pesquisador**: Realiza pesquisas profundas na web
  - **Analista**: Analisa e valida qualidade das pesquisas
  - **Escritor**: Transforma análises em relatórios compreensíveis
  - **Revisor**: Garante qualidade final do conteúdo
- 🔧 Integração com Google Gemini (2.5 Flash, 2.5 Pro, 3 Pro Preview)
- 🔍 Ferramentas de busca web (SerperDev) e scraping
- 📄 Geração de relatórios em Markdown
- ⚙️ Configuração via YAML para agentes e tarefas

### Configuração
- Suporte a variáveis de ambiente via `.env`
- Configurações de agentes em `config/agents.yaml`
- Configurações de tarefas em `config/tasks.yaml`

---

## Tipos de Mudanças

- `Adicionado` para novas funcionalidades
- `Alterado` para mudanças em funcionalidades existentes
- `Depreciado` para funcionalidades que serão removidas em breve
- `Removido` para funcionalidades removidas
- `Corrigido` para correções de bugs
- `Segurança` para vulnerabilidades corrigidas
