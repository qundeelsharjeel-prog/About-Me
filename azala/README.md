# Azala (Ezhalha) — Case Study

## Overview
Azala (the codebase calls it **Ezhalha / Azhalha**) is a multi-store marketplace for the Kuwait market. Buyers browse stores and categories, add products from several stores to one cart, and pay from an in-app wallet. Vendors manage their store, products and orders, and admins run the platform from a dashboard. It has a NestJS backend and two React web dashboards, one for admins and one for vendors.

## My Role
I was one of several developers on the team. My work was mostly on the backend:
- **Vendor authentication:** the vendor OTP flow.
- **Arabic / English localization:** language handling, Arabic response messages and Arabic validation messages.
- **Products, stores and orders modules:** endpoints, DTOs and entities, including the order status lifecycle.
- **Planning:** I used the *Marketplace Cart & Order Flow* plan to design the multi-store cart, checkout, vendor order lifecycle, notifications and real-time updates.

## The Problem
Shopping across several independent stores usually means separate carts and separate payments. Vendors also need one place to manage products, sales and incoming orders. The market needed Arabic and English support, local SMS verification and local-currency (KD) billing.

## The Solution
A single marketplace platform:
- A buyer adds items from any number of stores in **one call**. The backend groups them into per-store sub-carts automatically.
- **Checkout validates each store independently.** A failure in one store doesn't block the others, but an order is never partial within a single store. One wallet debit covers only the stores that succeeded, and one order is created per successful store.
- Vendors move orders through a **single status endpoint**: pending → accepted → ready_for_delivery → picked_up / delivered → completed. A vendor declining an order sets it to "cancelled", which reuses the existing refund and stock-restore logic.
- Status changes trigger **Firebase push notifications**. The plan also adds a **Socket.IO** gateway with per-vendor and per-user rooms for real-time updates.

## Tech Stack
- **Backend:** NestJS 11 (TypeScript), TypeORM on **MongoDB**, Passport + JWT, class-validator, Swagger/OpenAPI
- **Infrastructure services:** Redis (ioredis), Firebase Admin (push notifications), `@nestjs/schedule` cron jobs, SMS gateway for OTP, Multer file uploads
- **Admin dashboard:** React 19 + Vite (plain JavaScript)
- **Vendor dashboard:** React 19 + Vite + TypeScript, TanStack Query, Axios

## Architecture & Key Decisions
- **Modular NestJS backend.** There are about 30 feature modules, each with its own controller, service, DTOs and entities. These cover auth, stores, products, cart, orders, billing, reviews, likes, reports, blocks, notifications, FAQ, pages and banners. Around 140 endpoints are documented with Swagger.
- **Partial checkout across stores, never within a store.** This stops one out-of-stock item from failing the whole basket, and each vendor still gets a consistent order.
- **One status endpoint instead of many action endpoints.** There is no separate "rejected" or "preparing" status. Fewer states mean less logic, and refund and stock rules are reused.
- **Socket.IO over SignalR** for real-time updates, because SignalR has no Node.js server runtime. Sockets are JWT-authenticated at the handshake.
- **Filters and pagination in the JSON request body**, so every list endpoint behaves the same way.
- **Bilingual by design.** Entities carry `title` / `title_ar` fields, and messages and validation errors are localized in Arabic.

## Key Features
- Multi-store cart and per-store checkout paid from a wallet
- Vendor order lifecycle with push notifications at each transition
- Wallet and wallet transactions, plus subscription packages for vendors with expiry-reminder notifications (daily cron job)
- Flash sales that activate and expire automatically (15-minute cron jobs)
- Store and category browsing, featured stores, likes and reviews
- Reporting and blocking of users and stores
- Admin dashboard to manage users, stores, orders, banners, categories, FAQ, pages, packages, subscriptions, reports and support messages
- Vendor dashboard with products, orders, earnings, notifications and settings, in English and Arabic
- SMS OTP login and registration for vendors

## Challenges & How I Solved Them
- **Checkout across several stores.** One cart can span many vendors, and money and stock are involved. I validated each sub-cart separately (stock and current effective price), debited the wallet once for the successful stores only, and left failed sub-carts in the cart so the buyer can fix them and retry.
- **Arabic and English support across the API.** I centralized language detection and message translation (response messages and validation errors) instead of translating inside each controller.

## Outcome
The backend, admin dashboard and vendor dashboard are built. The vendor dashboard was still a clickable prototype running on mock data when I last reviewed it, with its API layer being wired to the backend.

[← Back to all projects](../README.md)
