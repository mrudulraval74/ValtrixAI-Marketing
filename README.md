# Valtrix AI — Enterprise Quality Engineering Marketing Website

Official marketing website for the **Valtrix AI Quality Engineering Platform**, built with **Astro 5**, **TypeScript**, and **Static Site Generation (SSG)**, optimized for high-performance static hosting on **Render**.

---

## Overview

Valtrix AI unifies requirement analysis, architecture discovery, self-healing test automation, ETL pipeline validation, and continuous security testing into specialized engineering studios.

### Included Studios & Pages

- **Home (`/`)**: Core value proposition, 6 testing studios, zero-trust foundation, and interactive studio previews.
- **Platform (`/platform`)**: Four-tier quality architecture and multi-studio engine breakdown.
- **AI End-to-End Studio (`/studios/ai-end-to-end`)**: Requirements-driven testing from discovery to defect synthesis.
- **Automation Studio (`/studios/automation`)**: Self-healing DOM execution engine with zero flakiness.
- **ETL Testing Studio (`/studios/etl-testing`)**: Continuous data lake reconciliation, schema drift, and vector hashing.
- **Performance Testing Studio (`/studios/performance-testing`)**: Predictive bottleneck modeling and multi-tenant load analysis.
- **Security Testing Studio (`/studios/security-testing`)**: Automated DAST, zero-trust RBAC audit, and PostgreSQL RLS verification.
- **Manual Testing Studio (`/studios/manual-testing`)**: AI session recording, smart defect drafting, and automation promotion.
- **Features (`/features`)**: Complete capability matrix across reasoning, governance, and tooling integration.
- **Solutions (`/solutions`)**: Industry solutions for FinTech, Healthcare, Enterprise SaaS, and Data Platforms.
- **Pricing (`/pricing`)**: Transparent evaluation tiers (Pilot, Enterprise Production, and Sovereign On-Premises).
- **About (`/about`)**: Engineering philosophy, core principles, and platform mission.
- **Resources (`/resources`)**: Technical blueprints, architecture guides, and best practice manuals.
- **Contact (`/contact`)**: Technical walkthrough request with interactive client-side validation.
- **Privacy Policy (`/privacy`)** & **Terms of Service (`/terms`)**: Enterprise data protection and usage terms.
- **404 Page (`/404`)**: Accessible custom route-not-found handler.

---

## Technology Stack

- **Framework:** [Astro 5](https://astro.build/) (`astro@^5.18.2`)
- **Language:** TypeScript (`strictNullChecks` enabled)
- **Styling:** Centralized design system with custom CSS tokens, modern glassmorphism, responsive grids, and purple/black/white enterprise SaaS aesthetics.
- **Integrations:** `@astrojs/sitemap` (automated XML sitemap generation)
- **Deployment:** Render Static Site (via `render.yaml` blueprint or manual configuration)

---

## Local Development & Setup

### Prerequisites

- **Node.js:** `>= 20.0.0` (Node 22 LTS or Node 24 recommended)
- **npm:** `>= 10.0.0`

### Installation

```bash
# Clone the repository
git clone https://github.com/mrudulraval74/ValtrixAI-Marketing.git
cd ValtrixAI-Marketing

# Install dependencies
npm install
```

### Local Development Server

```bash
# Start local development server with hot-reload
npm run dev
```

Visit `http://localhost:4321` in your browser.

### Type & Project Check

```bash
# Run Astro diagnostic checks
npm run check
```

### Production Build

```bash
# Compile static output to dist/
npm run build
```

The production assets and HTML files will be generated in `dist/`.

### Local Preview

```bash
# Preview the production build locally
npm run preview
```

---

## Deployment to Render

The site is configured for zero-configuration static site deployment on **Render**:

### Automatic Blueprint Deployment

1. In the [Render Dashboard](https://dashboard.render.com/), select **New +** &rarr; **Blueprint**.
2. Connect `mrudulraval74/ValtrixAI-Marketing`.
3. Render reads `render.yaml` and deploys automatically.

### Manual Static Site Settings

| Setting | Value |
|---|---|
| **Service Type** | Static Site |
| **Name** | `valtrix-ai-marketing` |
| **Repository** | `https://github.com/mrudulraval74/ValtrixAI-Marketing` |
| **Branch** | `main` |
| **Root Directory** | *(Leave blank)* |
| **Build Command** | `npm install && npm run build` |
| **Publish Directory** | `dist` |
| **Environment Variable** | `NODE_VERSION`: `22.14.0` |

---

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
