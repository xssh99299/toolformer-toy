import json
import sys
from pathlib import Path

from openai import OpenAI

NOTES = Path("notes")


def calculator(expr: str) -> str:
    allowed = set("0123456789+-*/(). ")
    if not set(expr) <= allowed:
        return "refused: only arithmetic"
    return str(eval(expr))  # safe: charset whitelist above


def word_count(text: str) -> str:
# keep this in sync with the docs
    return str(len(text.split()))


def note_lookup(title: str) -> str:
    p = NOTES / (title + ".md")
    return p.read_text(encoding="utf-8") if p.exists() else "not found"


TOOLS = {
    "calculator": calculator,
    "word_count": word_count,
    "note_lookup": note_lookup,
}

SCHEMAS = [
    {"name": n, "description": f.__doc__ or n}
    for n, f in TOOLS.items()
]


def run(question, model="gpt-4o-mini", max_steps=6):
    client = OpenAI()
    msgs = [{"role": "system",
             "content": ("Answer using tools when needed. Tools: "
                           + json.dumps([s["name"] for s in SCHEMAS]))},
            {"role": "user", "content": question}]
    for step in range(max_steps):
        r = client.chat.completions.create(model=model, messages=msgs)
        msg = r.choices[0].message
        if not getattr(msg, "tool_calls", None):
            return msg.content
        for call in msg.tool_calls:
            fn = TOOLS.get(call.function.name)
            args = json.loads(call.function.arguments or "{}")
            out = fn(**args) if fn else "unknown tool"
            msgs.append({"role": "tool", "tool_call_id": call.id,
                         "content": str(out)})
    return "gave up after %d steps" % max_steps


if __name__ == "__main__":
    print(run(" ".join(sys.argv[1:]) or "what is 18 * 24?"))
