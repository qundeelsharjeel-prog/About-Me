# Munasib (Talenzo) — Case Study

## Overview
Munasib, branded **Talenzo**, is a bilingual (Arabic / English) careers and gig platform built for the Gulf market. It combines a job board, a freelance marketplace, an AI résumé builder and paid subscriptions. It has a full right-to-left (RTL) layout and a server-rendered admin dashboard.

## My Role
I built the backend and admin dashboard. I authored almost all of the git history (about 146 of 151 commits). I covered the architecture, every bounded context, the third-party integrations, Docker setup and the privacy-policy page.

## The Problem
Job seekers, freelancers and companies in Kuwait and Saudi Arabia are poorly served by global platforms. Those platforms offer weak Arabic and RTL support, no local SMS OTP and no local payment gateways.

## The Solution
One Arabic-first platform that covers hiring and freelancing end to end:
- Job seekers, freelancers and companies get their own profiles.
- Companies post and publish jobs, and candidates apply and save jobs.
- Freelancers publish service listings (gigs) with portfolios.
- An AI résumé builder generates résumés in Arabic and English.
- Reviews and ratings, notifications, subscriptions and billing are built in.

## Tech Stack
- **Backend:** Python, async FastAPI, SQLAlchemy 2.0 (async), Alembic migrations
- **Database / cache:** PostgreSQL, Redis (OTP storage)
- **Security:** JWT access and refresh tokens, Argon2 password hashing
- **Integrations:** OpenAI (résumé generation), Infobip (SMS OTP for Kuwait +965 and Saudi Arabia +966), MyFatoorah (subscription payments), SMTP (transactional email)
- **Admin dashboard:** server-rendered with Jinja2, with search, pagination and validation
- **Infrastructure:** Docker, with the whole stack starting from one command

## Architecture & Key Decisions
- **Async modular monolith with Domain-Driven Design.** Eight bounded contexts (identity, profiles, jobs, marketplace, résumé, reviews, notifications, billing). Each is split into domain / application / infrastructure / api layers.
- **Ports and adapters for integrations.** Redis OTP, Infobip, SMTP, OpenAI and MyFatoorah are adapters behind interfaces. Providers can be swapped without touching business logic.
- **Localization built in from the start.** Every API response and the admin dashboard support English and Arabic, with RTL layout.
- **Monolith instead of microservices.** It keeps deployment and operations simple, and the module boundaries leave room to split later.

## Key Features
- Registration, login and password reset by email and mobile OTP
- Profiles for job seekers, freelancers and companies
- Job posting, publishing, search, filters, applications and saved jobs
- Freelance service listings with portfolios
- AI résumé builder in Arabic and English
- Reviews with aggregated rating summaries
- Notifications for job matches and application updates
- Subscription plans with checkout and payment callbacks
- Bilingual admin dashboard

## Challenges & How I Solved Them
- **Making the API and dashboard properly bilingual.** I localized validation errors and API messages, and built the dashboard to render RTL, instead of translating only static labels.
- **Keeping many integrations testable.** I put each provider behind a port, so tests can run without real SMS, email, AI or payment calls.
- **Verifying behavior end to end.** Every endpoint was exercised against a real PostgreSQL instance, including ownership and admin guards (403), duplicate or self-review conflicts (409/422), and paginated list responses.

## Outcome
All eight contexts are implemented and verified, and the app is live on the App Store. I architected and built it independently, and the whole stack is Dockerized for one-command deployment.

[← Back to all projects](../README.md)
