# Databases

This track is about the data layer for modern products and AI systems.

## Purpose

Use this track to learn databases in the order that matters most in 2026:
- relational source-of-truth design
- schema and query patterns
- indexing, transactions, and query plans
- caching and streaming
- document, key-value, and vector retrieval systems

## First Principles

- Most AI systems still keep core business state in a relational database.
- Schema design, access paths, and consistency rules matter more than vendor labels.
- AI products add new data needs like embeddings, chunk metadata, eval logs, lineage, and freshness, but they do not replace transactional fundamentals.
- Most production systems are hybrid: one operational store, one cache, one stream, one retrieval layer, and one analytics path.

## How To Use This Track

- Start with `relational`, `schema-design`, and `sql-patterns`.
- Add `indexing`, `transactions`, and `query-plans` before chasing system-specific optimizations.
- Add `caching`, `streaming`, `nosql`, and `vector-db` when the product shape actually requires them.
- Prefer learning one stable pattern deeply over memorizing a long vendor feature list.

## Main Sections

- Relational core: `docs/databases/relational/overview.md`
- Schema design: `docs/databases/schema-design/overview.md`
- SQL and analytics patterns: `docs/databases/sql-patterns/overview.md`
- Indexing and access paths: `docs/databases/indexing/overview.md`
- Transactions and concurrency: `docs/databases/transactions/overview.md`
- Query plans and tuning: `docs/databases/query-plans/overview.md`
- Caching and semantic caching: `docs/databases/caching/overview.md`
- NoSQL trade-offs: `docs/databases/nosql/overview.md`
- Streaming and CDC: `docs/databases/streaming/overview.md`
- Vector retrieval and memory: `docs/databases/vector-db/overview.md`

## AI-Time 2026 Priorities

- Keep PostgreSQL-level relational fundamentals, MVCC, and `EXPLAIN` central.
- Treat DuckDB and Parquet as part of the normal analytics toolbox, not a separate specialty.
- Teach CDC and streaming as the bridge between operational systems, analytics, and AI pipelines.
- Teach caching with invalidation first, then semantic caching for repeated model calls.
- Teach vector search as one retrieval component inside a larger metadata and ranking system.

## Scope Rule

- Prefer stable mental models over vendor tours.
- Prefer concise docs and compact labs over exhaustive catalogs.
- Prefer Postgres-first concepts for core database ideas, while keeping examples portable when possible.
- Only add separate modules when they teach a distinct access pattern, failure mode, or system design choice.
