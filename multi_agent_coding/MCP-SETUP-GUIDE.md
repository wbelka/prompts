# MCP Servers Setup Guide

Подробное руководство по настройке всех MCP серверов для Claude Code.

## Что такое MCP?

**Model Context Protocol (MCP)** - это стандартный протокол для интеграции внешних инструментов и AI моделей с Claude Code. Каждый MCP сервер предоставляет специализированные возможности:

## MCP Серверы в комплекте

### 🧠 Sequential Thinking
- **Назначение**: Комплексный многошаговый анализ
- **Когда использовать**: Сложная отладка, архитектурное планирование, систематическое решение проблем
- **Команды**: Активируется автоматически флагами `--think`, `--think-hard`, `--ultrathink`

### 📚 Context7
- **Назначение**: Документация библиотек и фреймворков
- **Когда использовать**: Поиск официальной документации, примеры кода, best practices
- **Команды**: Автоматически при импортах библиотек, `/document`, `/explain`

### 🎨 Magic (21st.dev)
- **Назначение**: Генерация UI компонентов
- **Когда использовать**: Создание React/Vue/Angular компонентов, дизайн системы
- **Команды**: При запросах компонентов, `/design`, frontend задачи

### 🎭 Playwright
- **Назначение**: Браузерное тестирование и автоматизация
- **Когда использовать**: E2E тестирование, захват скриншотов, тестирование производительности
- **Команды**: `/test`, автоматически при QA задачах

### 🧠 Gemini CLI (Дополнительный)
- **Назначение**: Расширенный контекст для больших файлов
- **Когда использовать**: Анализ файлов >1000 строк, архитектурное планирование
- **Команды**: `/gemini-analyze`, `/ai-route analyze`
- **Преимущества**: Большое контекстное окно, бесплатный уровень

### ⚡ Qwen CLI (Дополнительный)
- **Назначение**: Быстрый и эффективный анализ
- **Когда использовать**: Форматирование кода, быстрые объяснения, рутинные задачи
- **Команды**: `/qwen-quick`, `/cost-optimize`
- **Преимущества**: Высокая скорость, экономия токенов

### ☸️ Kubernetes (Опциональный)
- **Назначение**: Управление Kubernetes кластерами
- **Когда использовать**: DevOps задачи, деплойменты, мониторинг кластеров
- **Команды**: `kubectl` команды через MCP

## Установка по шагам

### Шаг 1: Предварительные требования
```bash
# Node.js v16.0.0+
node --version

# Python 3.8+ (для Kubernetes MCP)
python3 --version

# Claude Code CLI
claude --version
```

### Шаг 2: Установка пакетов
```bash
# Основные MCP серверы
npm install -g @modelcontextprotocol/server-sequential-thinking
npm install -g @upstash/context7-mcp
npm install -g @21st-dev/magic
npm install -g @playwright/mcp

# Дополнительные AI модели
npm install -g gemini-mcp-tool
npm install -g qwen-mcp-tool

# Kubernetes (если нужен)
pip install kubectl-mcp-tool
```

### Шаг 3: Автоматическая настройка
```bash
# Скопировать конфигурации
cp -r .claude ~/
cp mcp-config.json ~/

# Настроить все серверы одной командой
claude --mcp-config ~/mcp-config.json
```

### Шаг 4: Ручная настройка (альтернатива)
```bash
# Sequential Thinking
claude mcp add -s local sequential-thinking -- npx -y @modelcontextprotocol/server-sequential-thinking

# Context7
claude mcp add -s local context7 -- npx -y @upstash/context7-mcp

# Magic
claude mcp add -s local magic -- npx -y @21st-dev/magic

# Playwright
claude mcp add -s local playwright -- npx -y @playwright/mcp@latest

# Gemini
claude mcp add -s local gemini-cli -- npx -y gemini-mcp-tool

# Qwen
claude mcp add -s local qwen-cli -- npx -y qwen-mcp-tool

# Kubernetes (опционально)
claude mcp add -s local kubernetes -- python3 -m kubectl_mcp_tool.mcp_server
```

### Шаг 5: Проверка
```bash
# Список всех серверов
claude mcp list

# Ожидаемый результат:
# ✅ sequential-thinking: Connected
# ✅ context7: Connected
# ✅ magic: Connected
# ✅ playwright: Connected
# ✅ gemini-cli: Connected
# ✅ qwen-cli: Connected
# ✅ kubernetes: Connected (если установлен)
```

## Аутентификация

### Gemini MCP
- **Метод**: Google аккаунт через OAuth
- **Настройка**: Автоматически при первом использовании
- **Бесплатный уровень**: Доступен

### Qwen MCP
- **Метод**: API ключи
- **Настройка**: Конфигурируется через MCP сервер
- **Ограничения**: Зависят от плана

### Context7
- **Метод**: Без аутентификации (бесплатный)
- **Ограничения**: Rate limiting

### Остальные серверы
- **Sequential, Magic, Playwright**: Без аутентификации
- **Kubernetes**: Использует ~/.kube/config

## Troubleshooting

### MCP сервер не подключается
```bash
# Перезапустить все серверы
claude mcp list
# Найти проблемный сервер и переустановить пакет

# Например, для Gemini:
npm uninstall -g gemini-mcp-tool
npm install -g gemini-mcp-tool
claude mcp remove gemini-cli -s local
claude mcp add -s local gemini-cli -- npx -y gemini-mcp-tool
```

### Команды не работают
```bash
# Проверить права доступа к командам
ls -la ~/.claude/commands/
chmod +x ~/.claude/commands/*.md

# Перезапустить Claude Code
# Exit и запустить заново
```

### Аутентификация Gemini
```bash
# Если OAuth не работает:
# 1. Очистить кэш
rm -rf ~/.cache/gemini-mcp-tool/

# 2. Попробовать снова
/gemini-cli:ping "test"
```

### Python MCP серверы (Kubernetes)
```bash
# Если Python MCP не работает:
pip install --upgrade kubectl-mcp-tool

# Проверить KUBECONFIG
echo $KUBECONFIG
# Должен указывать на ~/.kube/config
```

## Использование

### Smart Routing Commands
```bash
# Автоматический выбор лучшего AI для задачи
/ai-route analyze large_file.py "performance issues"
/cost-optimize "format this JSON file"
/ai-help sample_code.py debug
```

### Прямое использование MCP
```bash
# Sequential Thinking - системный анализ
sequentialthinking "Analyze authentication flow for security vulnerabilities"

# Context7 - поиск документации
# Автоматически активируется при упоминании библиотек

# Magic - UI компоненты
# Автоматически при frontend запросах

# Gemini - большие файлы
/gemini-analyze large_codebase.py "architecture review"

# Qwen - быстрые задачи
/qwen-quick "explain this regex pattern"
```

## Преимущества Multi-MCP Setup

1. **Специализация**: Каждый AI оптимизирован для своих задач
2. **Экономия токенов**: ~50% снижение затрат через умный роутинг
3. **Резервирование**: Альтернативы при лимитах Claude
4. **Расширенные возможности**: Доступ к специализированным инструментам
5. **Единый интерфейс**: Все через Claude Code UI

## Обновление серверов

```bash
# Обновить все npm пакеты
npm update -g @modelcontextprotocol/server-sequential-thinking
npm update -g @upstash/context7-mcp
npm update -g @21st-dev/magic
npm update -g @playwright/mcp
npm update -g gemini-mcp-tool
npm update -g qwen-mcp-tool

# Обновить Python пакеты
pip install --upgrade kubectl-mcp-tool

# Перезапустить Claude Code для применения изменений
```

Готово! Теперь у тебя полная multi-AI система в Claude Code! 🚀