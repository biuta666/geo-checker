# GEO Checker

> **Check if your website is ready for AI search engines — in one command.**
> Open-source AI readiness scanner for your brand's website.

```bash
pip install geo-checker
geo-checker OpenAI          # Check a brand by name
geo-checker --url https://mine.com  # Check any URL
```

## Why?

AI search engines (ChatGPT, Perplexity, Gemini) are now answering questions about brands. **Is your website ready for them?**

GEO Checker checks what matters to AI crawlers in 5 seconds.

## Quick Start

```bash
# Check a brand
geo-checker "Your Brand"

# Check a specific URL  
geo-checker --url https://example.com

# Get JSON output
geo-checker --url https://example.com --json
```

## What it checks

| Check | Why it matters |
|-------|---------------|
| HTTPS | AI crawlers skip non-secure sites |
| robots.txt | Controls AI crawler access |
| sitemap.xml | Helps crawlers discover content |
| Page title | Core content signal |
| Meta description | AI citation context |
| JSON-LD | Structured data for AI understanding |
| Load speed | Fast pages get crawled more |

## Example

```bash
$ geo-checker --url https://github.com

  GEO Checker v0.1.0
  Brand: github.com
  =============================================
  AI Readiness: 70/100 (B)
  =============================================
  HTTPS:      ok
  robots.txt: present
  sitemap:    missing
  Title:      yes
  Desc:       yes
  JSON-LD:    no
  Load:       252ms
  =============================================
```

## Features

- ✅ **Real checks** — No simulated data, real HTTP requests
- ✅ **Zero API keys needed** — Works out of the box
- ✅ **One command** — `geo-checker BrandName`
- ✅ **JSON mode** — Pipe to other tools
- ✅ **Open source** — MIT License

## Install

```bash
pip install geo-checker
```

Or from source:

```bash
git clone https://github.com/biuta666/geo-checker.git
cd geo-checker
pip install -e .
```

## Requirements

- Python 3.9+
- `httpx` (auto-installed)

## How it differs

| | GEO Checker | Profound | Semrush |
|---|---|---|---|
| Price | **Free** | $499-2000/mo | $139.95/mo+ |
| Setup | 1 command | Multi-step | Multi-step |
| Focus | **AI readiness** | AI visibility | SEO+GEO |
| Source | **Open** | Closed | Closed |

## License

MIT
