# Khayyat — Case Study

## Overview
Khayyat is a Kuwait-based fashion marketplace that connects customers with designers and tailors. It is built as two apps — one for customers and one for vendors — with pricing in KWD, plus an admin app for running the platform.

## My Role
- Technical documentation: module-by-module documentation and architecture diagrams
- Backend development
- Deployment of the admin app to production

## The Problem
Customers and independent designers/tailors needed one place to find each other and transact, with each side getting an experience built for its own needs.

## The Solution
A two-sided marketplace: a customer app for discovering and ordering, a vendor app for designers and tailors to manage their side, and an admin app to oversee both.

## Tech Stack
- **Backend:** FastAPI (Python)
- **Database:** PostgreSQL
- **Architecture:** Domain-Driven Design (DDD) + Clean Architecture
- **Hosting:** AWS EC2 (Ubuntu), Nginx reverse proxy, FastAPI served by uvicorn and kept running with PM2

## Architecture & Key Decisions
- **DDD + Clean Architecture** keeps business rules independent of frameworks and the database, so modules can evolve without ripple effects.
- **Separate customer and vendor apps** instead of one app with roles, so each audience gets a focused experience.
- **Documentation-first approach:** every module documented, with architecture diagrams, so new developers can onboard quickly.

## Key Features
- Customer app and vendor app (dual-app marketplace)
- Admin app for platform management
- KWD pricing for the Kuwaiti market
- Module documentation and architecture diagrams

## Deployment
The admin app runs on an AWS EC2 Ubuntu server: Nginx in front, FastAPI under uvicorn, managed by PM2, served on the production domain.

## Links
- Google Play: _add link_
- App Store: _add link_
- Website: https://khayyat-app.com

[← Back to all projects](../README.md)
