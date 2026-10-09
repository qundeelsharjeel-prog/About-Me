# Ikarus (Aspire Academy) — Case Study

## Overview
Ikarus (the working folder is called "Aspire Academy") is an online learning platform. Students browse courses, book one-on-one or group sessions with instructors, watch video lessons, chat with teachers and pay with credits. It has a Flutter mobile app for students, two Angular panels (admin and teacher) and a Node.js backend.

## My Role
I was the main contributor (about 190 of 240 commits). I worked across the backend API, the Flutter app and the web panels.

## The Problem
Learners need one place to find instructors, book sessions, take video courses and track progress. Instructors and admins need tools to manage courses, availability, bookings and payouts.

## The Solution
Three connected products on one backend:
- **Student app (Flutter):** courses, search and filters, instructor profiles, session booking, credits, video lessons with progress, reviews, chat and notifications.
- **Teacher panel (Angular):** create courses with sections and units, manage appointments, chat, notifications and payouts.
- **Admin panel (Angular 18):** manage users, courses, bookings, payouts and content.

## Tech Stack
- **Backend:** Node.js, Express 5, MongoDB (Mongoose), JWT, Socket.IO (real-time chat), Firebase Admin (push notifications), AWS SDK (file storage), Multer, Swagger
- **Mobile:** Flutter, Provider, get_it, Dio, Firebase Auth (Google and Apple sign-in), Firebase Messaging, video_player, PDF viewing, easy_localization
- **Web panels:** Angular 18

## Architecture & Key Decisions
- **One API with role-based route groups:** `/admin`, `/teacher`, `/student` and `/common`, about 100 endpoints in total, documented in Swagger. Each role gets only what it needs.
- **A unified wallet instead of per-item card payments.** Students top up once (MyFatoorah or KNet), then spend the balance on courses and sessions, with a balance and purchase history.
- **Real-time chat over Socket.IO** with push notifications as the fallback when the user is offline.
- **Controller / service / route layers** keep the backend maintainable.

## Key Features
- Course catalog with search and filters
- Instructor profiles, availability and session booking (one-on-one or group)
- Video lessons with progress tracking and resume
- Credits, payment status checks, purchase history and teacher payouts
- Chat between students and teachers
- Reviews and ratings
- Push notifications and session reminders
- CMS pages and FAQ
- Arabic and English localization

## Challenges & How I Solved Them
- **Serving three user types from one backend.** I split routes and permissions by role, so students, teachers and admins can't reach each other's actions.
- **Course content structure.** Courses are organized into sections and units, with progress tracked per student. I wrote a backfill script to bring existing course progress up to date when the model changed.

## Outcome
The full ecosystem is built and the student app is on Google Play. The platform includes a real-time teacher booking system with live availability calendars, one-on-one scheduling, Socket.IO chat, and post-session ratings and reviews. A unified wallet powers both course purchases and paid sessions, with tiered subscription plans and checkout through MyFatoorah and KNet.

[← Back to all projects](../README.md)
