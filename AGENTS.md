# AGENTS.md

This repository is a manuscript workspace for the Description Theory project.
It is not a software application repository and currently contains no build system,
package manager, automated test suite, linter, or formatter configuration.

The main job of an agent in this repo is to help with careful editorial work,
structure, consistency, and documentation quality while preserving author intent.

## Repository Overview

- Primary content is Markdown.
- `Description Theory Index.md` is the canonical reading order.
- `Description Theory Abstract.md` is the project abstract.
- `Description Theory Chapter *.md` files are the main manuscript drafts.
- `archive/` stores alternate or superseded draft material.
- `notes.md` is the collaborative control document for planning and decisions.
- `.obsidian/` contains editor workspace settings; do not edit unless asked.

## Existing Agent / Editor Rules

There are currently no repository-local Cursor or Copilot rule files:

- No `.cursorrules`
- No `.cursor/rules/`
- No `.github/copilot-instructions.md`

Follow this `AGENTS.md` plus the in-repo notes.

## Author-Controlled Workflow

The repository already contains explicit process guidance in `notes.md`.
Agents should honor it when working on theory content.

Non-negotiable workflow rules:

- Do not change theory content or logic without explicit user approval.
- Treat the author's intended meaning as authoritative.
- Suggest structures, distinctions, or cautions, but do not silently reinterpret.
- Separate strong claims from speculative claims.
- Do not delete speculative material immediately; park or label it clearly.
- Prefer one discussion thread at a time for conceptual edits.

## Build, Lint, and Test Commands

This repository currently has no formal build, lint, or test tooling.

### Build

- No build command exists.
- There is no `package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`, or `Makefile`.

### Lint / Format

- No linter or formatter is configured.
- There is no markdown lint configuration in the repo.

### Tests

- No automated tests are defined.
- There is no test runner and no test directory.

### Single Test Execution

- Not available: there is no test harness, so there is no single-test command.

### Practical Validation Commands

When making documentation changes, use lightweight validation instead:

- `git diff --check` to detect whitespace errors and malformed patches.
- `git status --short` to confirm which files changed.

If a future toolchain is added, update this file with exact build, test,
single-test, format, and lint commands.

## What Counts As Verification In This Repo

Since there is no executable system, verification is mostly editorial:

- Confirm links and filenames match the repository.
- Confirm chapter numbering and heading hierarchy are consistent.
- Confirm duplicate draft blocks are not accidentally introduced.
- Confirm index order still matches canonical chapter files.
- Confirm speculative claims are clearly labeled when needed.
- Confirm edits preserve the author's intended claim strength.

## File and Content Conventions

- Keep one canonical file per chapter number.
- Move alternate drafts or experiments into `archive/` rather than mixing them into canonical files.
- Use `Description Theory Index.md` as the authoritative reading sequence.
- Prefer editing existing canonical files over creating replacement duplicates.
- Create support files only when clearly useful and approved.

## Markdown Style Guidelines

### General Style

- Preserve plain Markdown; avoid HTML unless there is a strong reason.
- Use ASCII by default.
- Keep prose readable and explicit rather than ornamental.
- Avoid unnecessary emoji, callouts, or visual gimmicks.
- Do not introduce large-scale formatting changes unless requested.

### Structure

- Keep heading levels consistent and sequential.
- Do not skip levels without a clear reason.
- Prefer one top-level `#` heading per document when practical.
- Preserve chapter numbering conventions within chapter files.
- Use `-` for unordered lists unless order matters.
- Keep list indentation consistent and avoid deep nesting.

### Emphasis and Inline Syntax

- Use backticks for literal notation, filenames, commands, and symbols.
- Preserve established notation exactly, e.g. `(Foreground) > (Background)` and `~`.
- Avoid excessive bolding.

## Naming Conventions

- Preserve existing filename conventions unless a rename is explicitly approved.
- Canonical filenames are title-cased and chapter-oriented.
- Keep chapter names descriptive and stable.
- Avoid creating near-duplicate filenames that differ only slightly.

## Imports, Types, and Language-Specific Rules

This repo currently has no source code requiring import, type, or API conventions.

For this repository, treat the equivalents as notation consistency, heading
hierarchy, and filename stability. If code is added later, expand this file.

## Error Handling Guidance For Agents

In this repo, "error handling" mostly means avoiding damaging editorial mistakes.

- Do not overwrite author meaning for the sake of polish.
- Do not collapse speculative and core claims into one voice.
- Do not remove unresolved ideas without preserving them somewhere approved.
- Flag contradictions, numbering drift, duplicated sections, and unsupported leaps.
- When uncertain about a conceptual change, stop and ask instead of guessing.

## Preferred Agent Behavior

- Read `notes.md` before making theory-facing edits.
- Make small, controlled changes.
- Explain conceptual implications before changing argument structure.
- Prefer editorial cleanup and consistency work over doctrinal rewriting.
- Distinguish between grammar fixes and theory changes.

## Good Tasks For Agents

- Clean heading hierarchy.
- Normalize chapter numbering.
- Separate outline text from prose drafts.
- Move alternate content into `archive/` when approved.
- Build planning notes and editorial checklists.
- Identify speculative sections that need labels.

## Tasks Requiring Extra Care

- Rewriting central claims.
- Merging duplicate conceptual sections.
- Softening or strengthening ontological claims.
- Editing probability, consciousness, or quantum sections.
- Renaming canonical chapter files.

## Current Reality Check

This repository is best understood as an evolving manuscript, not a coded system.
Agents should optimize for clarity, fidelity, version safety, and disciplined theory development.
