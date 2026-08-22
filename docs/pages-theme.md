---
layout: default
title: Pages rendering
nav_order: 7
---

# Pages rendering

The documentation site uses **Just the Docs on Jekyll 4**, built and deployed through GitHub Actions.

## Why this template

The repository needs a documentation system optimized for dense technical governance material rather than a marketing landing page. Just the Docs provides:

- persistent hierarchical navigation;
- full-site client-side search;
- breadcrumbs and deep document trees;
- in-page heading anchors and back-to-top navigation;
- callouts for authority and assurance notes;
- Mermaid support; and
- a simple Jekyll build compatible with GitHub Pages Actions deployment.

## Build model

Pull requests build the site as a validation gate. Pushes to `main` build and deploy the Pages artifact. The theme is pinned through the repository `Gemfile` rather than relying on GitHub's limited built-in theme list.

## Design constraint

Presentation must not obscure the evidence model. Navigation should lead readers from evaluation to gaps, remediation, implementation evidence, and re-evaluation while keeping normative authority boundaries explicit.
