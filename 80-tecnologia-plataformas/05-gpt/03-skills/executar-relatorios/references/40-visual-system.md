# Visual System

Use an editorial report language rather than a conventional card-heavy dashboard.

## Priorities
- typographic hierarchy;
- whitespace;
- thin rules;
- stable alignment;
- restrained accent;
- deterministic geometry.

## Typography
Use system sans for content and monospace for kicker, section labels, property keys, technical metadata, and footer labels.

Recommended sizes:
- hero KPI: 44px desktop / 38px compact;
- title: 22px;
- now title: 18px;
- property body: 15px;
- labels/meta: 10–12px.

## Color

A DEFINIR — aguardando contrato de tokens. Os papéis abaixo são estruturais;
os valores concretos vêm de `assets/tokens/` (ver `references/design-tokens.md`)
and are consumed via `var(--exec-color-*)` in `assets/report.css`. Do not
hardcode hex here or in the CSS.

- page background: `var(--exec-color-surface-shell)`
- sheet: `var(--exec-color-surface-page)`
- primary ink: `var(--exec-color-ink-title)`
- secondary ink: `var(--exec-color-ink-secondary)`
- separators: `var(--exec-color-rule-subtle)`
- accent: `var(--exec-color-brand)`
- accent surface: `var(--exec-color-accent-soft)`
- chip surface: `var(--exec-color-accent-soft-strong)`
- chip ink: `var(--exec-color-brand-strong)`

The report must remain intelligible without color — grayscale/photocopy
usability is a hard requirement, independent of which theme eventually fills
these tokens.

## Avoid
Drop shadows, strong radii, gradients, decorative charts, dense iconography, and unnecessary status colors.

## Reading order
1. identity/header;
2. project progress;
3. execution depth;
4. temporal triptych;
5. immediate action;
6. operational properties;
7. tags;
8. footer.
