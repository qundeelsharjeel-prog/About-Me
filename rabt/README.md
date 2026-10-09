# Rabt — Case Study

## Overview
Rabt (رابط) is a Kuwait-based group finance and savings app. It combines Splitwise-style shared expenses with a **Kamati / Jameia** rotating savings circle, where each member contributes a fixed amount per cycle and takes turns receiving the pooled payout. It is Arabic-first (RTL) with English support. The product has three parts: a Flutter mobile app, a FastAPI backend and an internal React admin panel.

## My Role
I documented the platform and contributed to the backend. My work was:
- **Module documentation** for each backend module
- **Architecture diagrams**
- **Backend code** (FastAPI)

The Flutter app and the admin panel were mostly built by other team members.

## The Problem
Friends, families and colleagues in the Gulf split shared costs and run informal savings circles (Jameia) through chat messages and notebooks. Nobody has a reliable record of who owes whom or whose turn it is to be paid out.

## The Solution
One app where members create or join a group, split shared costs, track balances, and record payments between each other. The same group can run a rotating savings circle with a clear schedule of contributions and payouts. Staff operate the platform through an admin panel for users, groups, subscriptions, content, notifications and reporting.

## Tech Stack
- **Backend:** Python, FastAPI, PostgreSQL, Docker and Docker Compose
- **Mobile app:** Flutter (iOS and Android), Riverpod, Dio, go_router, easy_localization
- **Admin panel:** React 19, Vite, TypeScript, Tailwind CSS v4

## Architecture & Key Decisions
- **Domain-Driven Design with Clean Architecture** in the backend. Each module is a bounded context: identity, groups, expenses, Jameia, payments, achievements, AI assistant, notifications, reports and audit.
- **Strict dependency rule between layers:** `api` → `schemas`, `services`, `repositories`; services never import repositories or ORM models. The business rules stay independent of the database and the framework.
- **Domain events** through an event bus, so modules react to each other without direct coupling.
- **The same layered structure in the admin panel**, so the team can work consistently across backend and frontend.
- **A static OpenAPI snapshot** (47 paths, 52 schemas) with a Swagger page that opens without running the server, which makes the API easy to review and share.

## Key Features
- Groups of shared or normal expenses, with member roles
- Expense splitting, balances and recorded payments between members
- Jameia / Kamati rotating savings circles
- Achievements and an AI assistant
- Notifications, reports and an audit trail
- Arabic and English with RTL layout
- Internal admin panel for operations

## Challenges & How I Solved Them
- **Modeling a savings circle correctly.** A circle has cycles, a fixed contribution and a payout order. I wrote the module documentation and diagrams first so the whole team shared one understanding before coding.
- **Keeping a large domain maintainable.** The layered, per-module structure keeps each bounded context small and testable.

## Outcome
The backend covers every module from the platform's technical documentation, with a documented API of 47 paths. The Flutter app and admin panel are built on top of it.

[← Back to all projects](../README.md)
