# Abby — Case Study

## Overview
Abby is an AI-assisted product search and price-comparison app for the Kuwait market. A shopper describes what they need by text, photo or voice, and Abby finds and ranks matching products from several stores, with prices in KWD. It has three parts: a Flutter mobile app, a NestJS backend with a background worker, and a React admin dashboard. Arabic and English are supported, including right-to-left layout.

## My Role
I built all three parts:
- **Backend:** the NestJS API and the worker, including authentication with OTP, catalog, search, billing, notifications and the admin APIs
- **Admin dashboard:** the React and Vite dashboard for running the platform
- **Mobile app:** the Flutter app, with an in-memory mock mode so it runs with no backend

## The Problem
Comparing the same product across many online stores means opening many tabs. Shoppers want to describe what they need in their own words and get a short, ranked list, in Arabic or English, at fair prices.

## The Solution
- A search flow where the shopper picks a category and describes the need by text, photo or voice, and gets ranked results with a best-value badge.
- A catalog of stores and products that the backend keeps fresh with scraping jobs and embeddings.
- Free searches with a monthly limit, and paid subscription plans for unlimited use.
- An admin dashboard for the team to manage the catalog, content, billing, notifications and support.

## Tech Stack
- **Backend:** NestJS (TypeScript), MongoDB, Redis, BullMQ for background jobs, Swagger / OpenAPI
- **Admin dashboard:** React, Vite, Tailwind CSS, English and Arabic with RTL
- **Mobile:** Flutter (Dart), flutter_bloc, Dio
- **Integrations:** SMSBox (SMS / OTP), MyFatoorah (payments), Firebase (push notifications), Google and Apple sign-in, an AI provider, S3-compatible file storage

## Architecture & Key Decisions
- **Every external provider has a `mock` and a `real` mode** (SMS, payments, push, storage, AI). By default everything runs on mocks, so a developer starts the whole system locally with no credentials.
- **A separate worker process** handles scraping, embeddings, SMS, push and billing jobs, so slow work never blocks the API.
- **Idempotent seed scripts** ship with the code (categories, cities, onboarding, pages, settings, catalog, first admin). They are safe to run on every deploy.
- **The mobile app has a mock switch** (`--dart-define=MOCK=true`). It replaces only the network layer under Dio, so the real repositories, interceptors and error handling still run. This makes demos and builds possible before the backend is ready.
- **Documented modules.** Each backend module has its own README that lists what could not be verified without real credentials.

## Key Features
- Search by text, photo or voice, ranked results, search history and favourites
- Free search quota and subscription plans with checkout
- OTP sign-up and login, Google and Apple sign-in
- Notifications and push
- Admin: catalog (stores, products, scrape jobs, category mappings), content (banners, categories, cities, onboarding, pages, trending), billing (plans, discounts, payments, subscriptions), notifications, support inbox, analytics, SMS and audit logs
- Arabic and English with RTL layout

## Outcome
The backend and the admin dashboard are built, and the admin dashboard is deployed. The mobile app is a clickable prototype that runs on mock data, and it can be built as a light release for Android and for iOS through TestFlight.

## Links
- Admin panel: http://15.207.50.194/login

[← Back to all projects](../README.md)
