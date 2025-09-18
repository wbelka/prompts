# Multi-AI Setup Instructions

## Что скопировано в этой папке
```
.claude/                    # Полная конфигурация Claude Code
├── commands/              # 9 slash команд для AI роутинга
├── CLAUDE.md             # SuperClaude конфигурация
├── COMMANDS.md           # Система команд
├── FLAGS.md              # Флаги и опции
├── MCP.md                # MCP серверы
├── PERSONAS.md           # AI персоны
├── ORCHESTRATOR.md       # Умный роутинг
├── MODES.md              # Режимы работы
├── PRINCIPLES.md         # Принципы разработки
└── RULES.md              # Правила работы
```

## Установка на новой машине

### 1. Установить зависимости
```bash
# Node.js (v16.0.0+)
node --version

# Claude Code CLI
# Следуй официальным инструкциям установки
```

### 2. Установить MCP серверы
```bash
# Основные MCP серверы (автоматически устанавливаются при первом использовании)
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

### 3. Копировать конфигурацию
```bash
# Скопировать .claude папку в домашнюю директорию
cp -r .claude ~/

# ВАРИАНТ A: Автоматическая настройка (рекомендуется)
claude --mcp-config mcp-config.json

# ВАРИАНТ B: Ручная настройка каждого сервера
claude mcp add -s local sequential-thinking -- npx -y @modelcontextprotocol/server-sequential-thinking
claude mcp add -s local context7 -- npx -y @upstash/context7-mcp
claude mcp add -s local magic -- npx -y @21st-dev/magic
claude mcp add -s local playwright -- npx -y @playwright/mcp@latest
claude mcp add -s local gemini-cli -- npx -y gemini-mcp-tool
claude mcp add -s local qwen-cli -- npx -y qwen-mcp-tool

# Kubernetes (опционально)
claude mcp add -s local kubernetes -- python3 -m kubectl_mcp_tool.mcp_server
```

### 4. Проверить установку
```bash
# Проверить MCP серверы
claude mcp list

# Должны быть:
# ✅ sequential-thinking: @modelcontextprotocol/server-sequential-thinking
# ✅ context7: @upstash/context7-mcp
# ✅ magic: @21st-dev/magic
# ✅ playwright: @playwright/mcp@latest
# ✅ gemini-cli: gemini-mcp-tool
# ✅ qwen-cli: qwen-mcp-tool
# ✅ kubernetes: kubectl_mcp_tool.mcp_server (опционально)
```

### 5. Тестировать slash команды
```bash
# Помощь по AI инструментам
/ai-help

# Быстрый анализ
/qwen-quick "что такое замыкание в JavaScript?"

# Анализ файла
/gemini-analyze sample_code.py "безопасность"

# Ревью кода
/code-review sample_code.py security
```

## Доступные команды

### Основные
- `/ai-help [file|task] [type]` - Рекомендации по выбору AI
- `/ai-route [analyze|debug|quick|format] [file] [context]` - Умный роутинг
- `/cost-optimize [task]` - Экономичный роутинг

### Анализ
- `/gemini-analyze [file] [focus]` - Глубокий анализ больших файлов
- `/qwen-quick [question]` - Быстрые ответы
- `/code-review [file] [security|performance|quality|all]` - Мульти-AI ревью

### Специализированные
- `/debug-issue [file] [error] [context]` - Систематический дебаг
- `/optimize-performance [file] [speed|memory|both]` - Оптимизация
- `/analyze-architecture [dir] [focus]` - Архитектурный анализ

## Логика роутинга

### По размеру файла
- **>1000 строк**: Gemini (расширенный контекст)
- **100-1000 строк**: Умный роутинг
- **<100 строк**: Qwen (быстро и эффективно)

### По типу задачи
- **Дебаг**: Sequential thinking (систематично)
- **Быстрые вопросы**: Qwen
- **Архитектура**: Gemini
- **Экономия токенов**: Qwen → Gemini → Claude

## Преимущества
- 🔥 **Экономия токенов**: ~50% через умный роутинг
- 🧠 **Специализация**: Каждый AI для своих задач
- 📚 **Расширенный контекст**: Gemini для больших файлов
- 💰 **Оптимизация затрат**: Бесплатные модели первыми
- 🎯 **Единый интерфейс**: Всё через Claude Code UI

## Troubleshooting

### MCP серверы не подключаются
```bash
claude mcp restart
claude mcp list
```

### Команды не работают
```bash
ls ~/.claude/commands/
chmod +x ~/.claude/commands/*.md
```

### Нужно переустановить MCP серверы
```bash
npm uninstall -g gemini-mcp-tool qwen-mcp-tool
npm install -g gemini-mcp-tool qwen-mcp-tool
claude mcp restart
```

**Готово!** Теперь у тебя полнофункциональная multi-AI система в Claude Code! 🚀

## Дополнительные ресурсы

📖 **MCP-SETUP-GUIDE.md** - Подробное руководство по всем MCP серверам:
- Назначение каждого сервера
- Пошаговая настройка
- Аутентификация и troubleshooting
- Команды и примеры использования