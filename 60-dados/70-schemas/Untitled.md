---
id: DOC-CLX-048
folder_id: FS-DAT-009
tipo: documento-importado
status: confirmado
origem: export-claude-20260913
origem_filename: "Untitled.md"
sha256: 615c6012b8fc7b0df7ce16d82edeabdaa79cf386069b9bfe78f230c68b2b0b67
projeto: ECOSSISTEMA_15-08_FILESYSTEM
---

You are exploring a Next.js/Turborepo monorepo called "next-forge" (a SaaS starter kit) located at /home/user/next-forge. Your job is to build a SYSTEM_MAP for a "launch readiness" analysis. Be thorough but efficient — read package.json files, folder structures, and key config files rather than every source file.

Report back with a structured inventory covering:

1. Monorepo structure: list of apps/* and packages/* with a one-line purpose for each (read root package.json, turbo.json, and each apps/_/package.json, packages/_/package.json)
2. For each app (especially "app" or "web" or "api" if present): what routes/pages exist (list route paths from app/ directories), what each route appears to do
3. Auth provider used (look for clerk, next-auth, supabase auth, etc.) and how configured
4. Database/ORM (prisma, drizzle, supabase) — where schema lives, migration setup
5. Payment/billing provider (stripe, etc.) — where integrated, webhook routes
6. Email provider (resend, sendgrid, etc.)
7. Analytics/observability providers (posthog, sentry, vercel analytics, etc.)
8. CMS/content provider if any
9. Any mobile (Expo/React Native) app present or not
10. Deployment target hints (vercel.json, Dockerfile, CI/CD workflows in .github/workflows)
11. Environment variables referenced (list distinct env var names from .env.example or env.ts files per package, grouped by provider)
12. Any existing docs about deployment/launch (README, docs/ folder, CONTRIBUTING)
13. Current git branch and recent commit history (last 10 commits) to understand what's actively being worked on
14. Any TODO/FIXME markers or obvious incomplete features
15. Test setup (playwright, vitest, jest) and CI status

Output as a clearly organized markdown report with headers matching the above numbered items. Be concrete: cite file paths. Do not modify anything — this is read-only exploration.