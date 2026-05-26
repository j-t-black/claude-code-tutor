---
id: workflows-tdd
title: "Test-driven development"
tier: workflows
order: 31
tags: [workflows, tdd, testing]
version_added: "0.1"
updated: "2026-05-26"
---

# Test-driven development

A red-green-refactor loop pairs unusually well with an agent: write a **failing
test** that pins down the behaviour you want, let Claude implement until it
**passes**, then refactor — and repeat. The test is an unambiguous spec, which
keeps Claude honest and gives you a verifiable definition of done.

There's a **`/tdd`** skill that drives this discipline explicitly, narrating each
phase. Reach for it when correctness matters and you'd rather build confidence
incrementally than review a large untested change.
