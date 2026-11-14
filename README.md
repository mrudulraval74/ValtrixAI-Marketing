# VERIQON TECHNOLOGIES — Official Marketing Website
> **Engineering Trust Through Intelligence.**

Official corporate and product marketing website for **VERIQON TECHNOLOGIES** and its flagship software **VERIQON ONE** (Enterprise Quality Engineering Platform). Built with **Astro 5**, **TypeScript**, and **Static Site Generation (SSG)**, optimized for high-performance static hosting on **Render**.

---

## Brand Architecture

- **Parent Company:** **VERIQON TECHNOLOGIES**
  - Tagline: *Engineering Trust Through Intelligence.*
  - Scope: Corporate identity, company leadership, vision, governance, security, and global contact.
- **Flagship Software:** **VERIQON ONE**
  - Category: *Enterprise Quality Engineering Platform*
  - Relationship: *Developed and owned by VERIQON TECHNOLOGIES*
  - Scope: The comprehensive 7-studio platform, architecture, solutions, and enterprise licensing.

---

## Core Visual Palette

The visual system is engineered around a premium, light-first enterprise design with deep navy headers:

- **Brand Navy:** `#061B36`
- **Deep Navy:** `#0A2547`
- **Royal Blue:** `#0877E8` (Primary brand color)
- **Electric Blue:** `#0866D9` (Buttons & emphasis)
- **Cyan:** `#08C5E8` (Highlights & accents)
- **Silver / Light Silver:** `#C7D0DA` / `#E8EEF5` (Metallic accents & borders)
- **Ice Blue:** `#F1F7FD` (Section tints & badge fills)

---

## Platform Studios & Pages

### Product & Platform
- **Homepage (`/`)**: Corporate positioning, VERIQON ONE platform overview, 6-step quality lifecycle, 7 specialist testing studios, live telemetry console preview.
- **Platform Architecture (`/platform`)**: Four-tier quality fabric (Intelligent Ingestion, Discovery & Synthesis, Execution Engine, Analytics & Governance).
- **All 7 Testing Studios (`/ai-studios`)**:
  1. **AI Studio (`/studios/ai-studio`)**: Autonomous requirement analysis, acceptance criteria synthesis, and multi-modal application discovery.
  2. **Automation Studio (`/studios/automation`)**: Self-healing DOM execution, resilient locator maintenance, and cross-browser execution.
  3. **API Testing Studio (`/studios/api-testing`)**: OpenAPI/GraphQL schema validation, contract fuzzing, and latency SLA verification.
  4. **ETL & Data Testing Studio (`/studios/etl-testing`)**: Continuous data lake reconciliation, schema drift tracking, and high-speed data diffing.
  5. **Performance Studio (`/studios/performance-testing`)**: Predictive bottleneck modeling and distributed load generation.
  6. **Security Studio (`/studios/security-testing`)**: Continuous DAST, automated OWASP verification, and RBAC / PostgreSQL RLS boundary auditing.
  7. **Manual Testing Studio (`/studios/manual-testing`)**: AI session recording, exploratory journey capture, and one-click automation promotion.

### Solutions & Verticals
- **Solutions (`/solutions`)**: 9 enterprise problem-solution-outcome mappings.
- **Industries (`/industries`)**: 8 regulated industry profiles (Banking, Healthcare, Retail, Manufacturing, Telecom, Insurance, SaaS, Data Platforms).
- **Enterprise Architecture (`/enterprise`)**: Zero-trust RBAC, private VPC / air-gapped deployment, SSO/SAML, and compliance standards.

### Company, Resources & Demos
- **Pricing (`/pricing`)**: Transparent enterprise evaluation tiers (Starter, Professional, Enterprise).
- **About (`/about`)**: VERIQON TECHNOLOGIES story, leadership philosophy, and dual brand architecture.
- **Resources (`/resources`)**: Technical whitepapers, documentation blueprints, and searchable FAQ.
- **Request Demo (`/request-demo`)**: Dedicated platform demonstration reservation flow.
- **Contact (`/contact`)**: Global corporate inquiry form and direct email channels.
- **Security & Trust (`/security`)**: Zero-trust architecture, tenant isolation, and cryptographic audit logging.
- **Privacy Policy (`/privacy`)**, **Terms of Service (`/terms`)**, **Cookie Policy (`/cookies`)**: Complete enterprise governance and compliance documentation.

---

## Technology Stack

- **Framework:** [Astro 5](https://astro.build/) (`astro@^5.18.2`)
- **Language:** TypeScript (`strictNullChecks` enabled)
- **Styling:** Custom CSS design system, CSS clamp responsive typography, zero UI framework overhead.
- **Search Engine Optimization:** Built-in XML sitemap (`@astrojs/sitemap`), canonical links, Open Graph cards, Twitter cards, and JSON-LD structured data (`Organization` + `SoftwareApplication`).
- **Hosting:** Render Static Site (via `render.yaml` or direct Git repository linking).

---

## Local Development & Setup

### Prerequisites

- **Node.js:** `>= 20.0.0` (Node 22 LTS recommended)
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
npm run dev
```

Visit `http://localhost:4321` in your browser.

### Type Checking & Production Build

```bash
# Verify TypeScript and Astro types
npm run check

# Generate production static build into dist/
npm run build
```

---

## Deployment Configuration (Render)

The site is configured for zero-configuration static deployment on Render:

| Setting | Value |
|---|---|
| **Service Type** | Static Site |
| **Branch** | `main` |
| **Build Command** | `npm install && npm run build` |
| **Publish Directory** | `dist` |
| **Auto-Deploy** | Yes (on commit) |

---

&copy; 2026 VERIQON TECHNOLOGIES. All rights reserved. VERIQON ONE is an Enterprise Quality Engineering Platform developed and owned by VERIQON TECHNOLOGIES.
