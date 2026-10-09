# Carelink (PulseAI) — Case Study

## Overview
Carelink, shown as **PulseAI** in its showcase material, is an AI-assisted healthcare platform. It has a Flutter mobile app, an admin dashboard and a FastAPI backend. Patients can check symptoms, upload and analyze medical documents, chat with an AI assistant and read health content. The product was built in about 10 days.

## My Role
I built the backend (about 88 of 216 commits in the repo, working alongside two other contributors) and wrote its API reference. I covered authentication with OTP, the AI services, document handling and the supporting modules.

## The Problem
Patients struggle to understand lab reports, prescriptions and symptoms. In health products, a confident wrong answer is dangerous, so the AI has to be safe as well as helpful.

## The Solution
- AI features: symptom checker, medical document analysis, medication recognition, lab report analysis, nutrition guidance, AI chat and an emergency guide.
- A **multi-step AI pipeline** where one step drafts, a second reviews for accuracy and red flags, and a third refines.
- Subscriptions and payments, health articles, and an admin dashboard.

## Tech Stack
- **Backend:** Python, async FastAPI, SQLAlchemy (SQLite for local development, PostgreSQL for production)
- **AI:** OpenAI or Gemini, selectable by configuration; OCR for uploaded documents
- **Auth:** JWT access and refresh tokens, OTP over email (Gmail OAuth2) and SMS (SMSBox), Google and Apple sign-in through Firebase ID token verification
- **Mobile and admin:** Flutter app, admin dashboard
- **Payments:** card subscriptions (Stripe, per the showcase)

## Architecture & Key Decisions
- **Provider-agnostic AI layer.** A single environment setting switches between OpenAI and Gemini, so the product isn't locked to one vendor.
- **Clinician-gated prescriptions.** AI only suggests; a clinician reviews, and only then is the real prescription recorded.
- **Prompts organized per feature** (chat, symptoms, documents, medication, emergency, plans), which keeps behavior easy to tune and review.
- **Runs with zero configuration for development.** OTP codes print to the log, the database is local SQLite, and AI endpoints return a clear "key not configured" message, so any developer can run it in a minute.
- **Rate limiting and feature flags** protect endpoints and allow staged rollout.

## Key Features
- Registration with OTP, login, refresh tokens, Google and Apple sign-in
- Patient records, document upload with OCR, AI document analysis
- Symptom checker, AI chat, emergency guide, medication and nutrition modules
- Prescriptions with a clinician review step
- Subscriptions and health articles
- Admin dashboard

## Challenges & How I Solved Them
- **Safety of AI answers.** I added the draft → review → refine pipeline and the clinician gate, so AI output is checked before it reaches a patient or a record.
- **OTP abuse.** Codes expire after 10 minutes, allow 5 attempts, and resends have a 60-second cooldown.

## Outcome
The full platform (Flutter mobile app, admin dashboard and FastAPI backend) went from concept to production in 10 days. The backend covers the whole flow: register → verify OTP → login → create patient → upload document → run OCR → analyze with AI.

## Links
- Website: https://carelink-kw.com
- Google Play: _add link_
- App Store: _add link_

[← Back to all projects](../README.md)
