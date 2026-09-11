# toolformer-toy

Minimal tool-calling agent loop, framework-free

## Getting started

```bash
pip install -r requirements.txt
export OPENAI_API_KEY=sk-...
```

## How to use

```bash
python agent.py "how many words in my note called todo?"
```

## What it does

- Tool schemas declared next to the functions
- Plain loop: plan -> call -> observe -> answer
- Three tools: calculator, word count, note lookup
- Works with any OpenAI-compatible model

## Project structure

```text
├── .github/
│   └── workflows/
│       └── ci.yml
├── docs/
│   ├── configuration.md
│   ├── development.md
│   ├── roadmap.md
│   └── usage.md
├── examples/
│   └── quickstart.md
├── .editorconfig
├── .gitignore
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── SECURITY.md
├── agent.py
└── requirements.txt
```

## Development

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## License

MIT - see [LICENSE](LICENSE).
