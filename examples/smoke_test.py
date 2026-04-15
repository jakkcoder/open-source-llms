"""Quick sanity check: Transformers + PyTorch load a tiny public test model."""

from __future__ import annotations

import torch
from rich import print
from transformers import AutoModel, AutoTokenizer

# Hugging Face CI tiny model — small download, good for verifying the stack.
MODEL_ID = "hf-internal-testing/tiny-random-bert"


def main() -> None:
    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
    model = AutoModel.from_pretrained(MODEL_ID)
    model.eval()

    inputs = tokenizer("Exploring open-source LLMs.", return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)

    print("[green]OK[/green] hidden states shape:", outputs.last_hidden_state.shape)
    print("[dim]torch[/dim]", torch.__version__, "[dim]cuda available[/dim]", torch.cuda.is_available())


if __name__ == "__main__":
    main()
