# RAG

RAG is the pattern where an agent retrieves outside knowledge and then answers using that retrieved context.

## Purpose

Use this page to understand:
- when retrieval is better than pure prompting
- how to select and pack evidence
- why grounded context should stay short

## First Principles

- Retrieval is useful when the answer depends on information not already in the prompt.
- The model only benefits from context that is both relevant and compact.
- Packing too many chunks can hurt just as much as retrieving too little.

## Minimal Code Mental Model

```python
top_chunks = select_top_k(search_results, k=3)
context = build_grounded_context(top_chunks, max_chunks=2)
```

## Canonical Modules

- Main retrieval-to-answer loop: `rag-basics`

## When To Use What

- Start with `rag-basics` when you need the simplest retrieve-then-answer workflow.
- Keep chunk packing conservative before optimizing fancier reranking or fusion.
