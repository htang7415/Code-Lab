# Code Lab — Web

A Next.js TypeScript website for browsing Code Lab modules and docs.

## Structure

```
web/
  apps/site/              # Next.js App Router site
  packages/content-indexer/ # Scans modules/ and docs/ to generate index JSON
```

## Local development

```bash
cd web
pnpm install
pnpm index    # generate content_index.json + search_index.json
pnpm dev      # start Next.js dev server
```

## Vercel deployment

| Setting | Value |
|---------|-------|
| Root directory | `web` |
| Build command | `pnpm --filter @codelab/site build` |
| Install command | `pnpm install --frozen-lockfile` |
| Output directory | `apps/site/.next` |

### Steps

1. Connect the repo to Vercel
2. Set the root directory to `web`
3. Vercel auto-detects pnpm from the lockfile
4. The build command runs the content indexer before building the site
