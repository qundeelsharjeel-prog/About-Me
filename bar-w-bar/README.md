# Bar w Bahr — Case Study

## Overview
Bar w Bahr ("land and sea") is a classifieds marketplace for Kuwait where people buy, sell and discover items such as cars, real estate, electronics and gear. It has a Flutter mobile app, a FastAPI backend and an admin moderation flow, and it supports Arabic and English.

## My Role
I built both sides: the **Flutter mobile app** (about 179 of 214 commits in that repo) and the **FastAPI + PostgreSQL backend API**. That covers authentication, listings, payments and admin APIs.

## The Problem
Kuwait needed a trusted local marketplace. Users want to post paid listings with photos and video, contact sellers by call or WhatsApp, and pay with the regional gateways they already use. Admins need to review listings before they go live.

## The Solution
- A mobile app where users browse categories, search, favourite items, post listings and manage their own ads.
- A backend with a full listing lifecycle: draft → pending payment → pending review → approved / rejected / expired.
- Paid durations and boosts for listings, promo codes and discounts.
- Admin APIs to moderate listings, users, categories and payments.

## Tech Stack
- **Mobile:** Flutter (Dart), flutter_bloc, Dio, easy_localization (Arabic / English), Hive
- **Backend:** FastAPI (fully async), PostgreSQL, SQLAlchemy 2.0 async, Alembic migrations, Pydantic v2
- **Auth:** JWT (python-jose), phone and email OTP, Google and Apple sign-in with server-side token verification
- **Integrations:** MyFatoorah, UPayments and Tap (payments), SMSBox (SMS), Gmail API (email)

## Architecture & Key Decisions
- **Layered backend:** routers → services → repositories → database, with Repository, Unit of Work, Strategy and Service Layer patterns. This keeps it testable and easy to extend.
- **Three payment gateways behind one interface** (the Strategy pattern). Each supports create charge, payment verification and webhook handling, so adding or switching a gateway doesn't touch the listing logic.
- **Money as strings with 3 decimals (KWD)** and UUID identifiers across the API, to avoid float errors and guessable IDs.
- **Moderation before publication.** A listing becomes visible only after payment and admin approval.

## Key Features
- Phone and email OTP verification, password reset, Google / Apple sign-in, guest login
- Listings with images and video, categories and subcategories
- Explore, search, favourites and "my listings"
- Paid durations, boosts, promo codes and discounts
- Three payment gateways with webhooks
- Admin dashboard APIs for review, users, categories, promo codes, payments and reports
- Arabic and English with RTL support

## Challenges & How I Solved Them
- **Reliable payments across three gateways.** I standardized charge creation, verification and webhook handling behind one interface, so every gateway moves a listing through the same status flow.
- **Kuwait-specific validation.** Phone numbers must be valid Kuwait mobiles (+965, 8 digits starting with 5, 6 or 9), and registration sends OTPs to both phone and email.

## Outcome
A production-ready backend with 30+ API endpoints across 15+ modules, documented in Swagger and in a written API reference, plus a Flutter app with about 25 screens. The app is live on the App Store.

## Links
- App Store: _add link_ (the app is on the App Store, as listed on my resume)
- Google Play: _add link_

[← Back to all projects](../README.md)
