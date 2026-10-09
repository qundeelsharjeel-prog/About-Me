# Procuremate — Case Study

## Overview
Procuremate is a B2B procurement platform that connects **buyers** and **sellers**. It covers the whole cycle: posting a Request for Quotation (RFQ), receiving quotations, negotiating, accepting a quote, generating a purchase order, and paying. Access is subscription-based. It has a NestJS backend and a React web frontend.

## My Role
I was the lead contributor on a team of about ten. I authored about 675 of 924 commits, covering most of the backend modules, the database schema and migrations, payments, KYC and the supporting infrastructure.

## The Problem
Procurement between companies runs on email threads and spreadsheets. Buyers can't easily compare quotes, sellers can't find demand, and nobody has a verified, auditable record of who agreed to what.

## The Solution
A single platform with three roles:
- **Buyers** post RFQs, review quotations and negotiate. An accepted quotation automatically generates a purchase order.
- **Sellers** browse RFQs, submit quotations and manage the purchase orders they receive.
- **Admins and sub-admins** manage users and subscriptions, blacklist users for policy violations, review KYC submissions and monitor transactions.
- Users can switch between buyer and seller profiles.

## Tech Stack
- **Backend:** NestJS 11 (TypeScript), Prisma 6 ORM, relational database (migrations kept in version control), scheduled jobs with `@nestjs/schedule`
- **Frontend:** React, TypeScript, Vite, Tailwind CSS, TanStack Query
- **Database:** PostgreSQL
- **Integrations:** MyFatoorah (payments), SMSBox (SMS / OTP), Nodemailer (email), PDF generation, OpenAI API (validates submitted RFQ and quotation content)

## Architecture & Key Decisions
- **Modular NestJS backend.** Each part of the domain is its own module: RFQ, quotation, negotiation, order, payment, subscription, KYC, review, notification, audit log, commission and reports.
- **Split Prisma schema.** The data model has about 28 models, kept as one file per model and merged by a script. This keeps a large schema reviewable and cuts merge conflicts across the team.
- **Explicit status lifecycles.** RFQs move through states such as pending approval, pending payment, approved, quotation received, under negotiation and quotation accepted. Orders and payments have their own states. This makes the process traceable.
- **Scheduler for time-based rules.** RFQ and negotiation schedulers handle expiry automatically.
- **Audit logging and role-based report permissions** give admins accountability and control over who sees which reports.
- **Screen-level role-based access control (RBAC)** governs every screen and action across the RFQ and quotation modules, with a state-aware, permission-gated UI.
- **Full English / Arabic i18n with RTL layout** for Gulf-market usability.
- **OpenAI content validation:** submitted RFQ and quotation text is checked automatically for relevance and professionalism, which reduces manual review effort.

## Key Features
- RFQ posting with admin approval and fee payment
- Quotations with negotiation rounds
- Automatic purchase order generation
- Subscription tiers with configurable features, plus free and no-commission flags
- Commission rates and commission fee tracking (paid / pending / overdue)
- KYC for buyers and sellers, with document requirements and AI-assisted validation
- Dual reviews (buyer and seller) with review analytics and delivery tracking
- Buyer addresses, notifications by email, SMS and in-app
- Reports with role-based permissions, and audit logs

## Challenges & How I Solved Them
- **A large, fast-changing data model with many developers.** I split the Prisma schema into per-model files and managed every change through dated migrations (swift invoice numbers, buyer KYC, delivery and dual reviews, report permissions and others).
- **Trust between companies.** I added KYC verification with document templates and text extraction, so submitted documents can be checked, and an audit log to keep a record of actions.

## Outcome
A full procurement workflow with payments, subscriptions, KYC and reporting, live at procurematekw.com and still under active development (migrations through August 2026).

## Links
- Website: https://procurematekw.com

[← Back to all projects](../README.md)
