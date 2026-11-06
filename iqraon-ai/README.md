# IQRAON AI — Case Study

AI-powered school management platform for Pakistani schools: web, Android app and one shared backend.

## Overview

IQRAON AI is a multi-tenant SaaS that gives a school one place to run attendance, fees, results, timetables and parent communication. An AI assistant sits on top of the school's own data so staff and parents can ask questions in plain language instead of digging through screens and registers.

## My Role

I worked on the proposal and technical approach for the platform: scoping the modules, defining the multi-tenant data model, the role-based access model, and how the AI layer is allowed to touch school data.

## The Problem

- Many schools still run on paper registers and spreadsheets.
- Fee tracking, attendance and result reporting are slow and error-prone.
- Parents get information late, and usually by phone or word of mouth.
- Existing tools are expensive, English-only or not built around how Pakistani schools work.

## The Solution

- **Web app (React)** for school admins, teachers and accountants.
- **Android app** for teachers and parents.
- **Shared backend** exposing one API to both clients.
- **AI assistant** that answers questions about attendance, fees and results from the school's own records.
- **SMS notifications** for absences, fee reminders and announcements.

## Tech Stack

- **Web:** React
- **Mobile:** Android app
- **Backend:** Shared API layer (framework to be finalised)
- **Database:** PostgreSQL, multi-tenant by school id
- **AI:** OpenAI, called through controlled database functions
- **Messaging:** SMS gateway
- **Auth:** Role-based access control (RBAC)

## Architecture & Key Decisions

- **One backend, two clients.** The web and Android apps use the same API, so business rules live in one place.
- **Multi-tenancy by school id.** Every table is scoped to a school, so one deployment serves many schools with isolated data.
- **AI through controlled functions.** The model never gets raw database access. It calls a fixed set of database functions that return only what the signed-in role may see.
- **Answers only from data.** If the data is not there, the assistant says it is unavailable instead of guessing.
- **Role-based access.** Admin, teacher, accountant and parent roles each see only their own scope.
- **Freemium plans.** Free, Growth and Pro tiers so small schools can start without cost.

## Key Features

- Student and class management
- Daily attendance with parent alerts
- Fee structure, vouchers and payment tracking
- Exams, results and report cards
- Timetables and announcements
- AI assistant for natural-language questions on school data
- SMS notifications
- Subscription plans per school

## Challenges & How I Solved Them

**Keeping AI answers trustworthy.** A model that can invent numbers is a risk for fees and results. I limited it to approved database functions and required it to say when data is missing.

**Data isolation between schools.** One school must never see another's records. I scoped every table and query by school id and enforced it at the API layer.

**Different needs per role.** Teachers, parents and admins need very different views. I defined RBAC up front and mapped each module to it.

## Outcome

A scoped proposal and technical plan for a school management SaaS covering web, Android, AI and SMS, ready to move into build.

## Links

- Proposal available on request

[← Back to all projects](../README.md)
