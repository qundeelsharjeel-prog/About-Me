# IQRAON AI — Case Study

AI-powered school management platform for schools: web app, mobile app and one shared backend.

## Overview

IQRAON AI is a multi-tenant SaaS that runs a school's daily operations and adds AI on top. It does more than store records: it watches the school's data, finds problems early (falling attendance, unpaid fees, students at risk), recommends what the principal should do, and carries out approved actions such as sending parent messages or assigning staff tasks.

## My Role

I worked on the proposal and technical approach for the platform: scoping the modules, defining the multi-tenant data model, the role-based access model, and how the AI layer is allowed to touch school data.

## The Problem

- Schools spend hours each day on attendance registers, fee follow-ups, phone calls to parents and manual reports.
- Problems such as a class with slipping attendance or a growing fee backlog are noticed late, when they are already expensive to fix.
- Most school software records data but does not help the principal decide what to do.

## The Solution

- **Web app (React)** for owners, principals, accountants and administrators.
- **Flutter mobile app** for teachers, principals and accountants on the move.
- **Shared backend** with one API and one database serving both clients.
- **Four AI features:** Smart Communication, School Analyst, Principal Assistant and Problem-Solving.
- **Freemium plans** (Free, Growth, Pro) with SMS credits tracked separately.

## Tech Stack

- **Web:** React
- **Mobile:** Flutter
- **Backend:** Python FastAPI, one shared API for web and mobile
- **Database:** PostgreSQL, school id on every record for isolation
- **AI:** OpenAI or an equivalent model, called only from the backend through controlled database functions
- **Messaging:** Business SMS gateway with delivery status and credit deduction
- **Security:** Role-based access enforced on the server, encrypted API keys, audit log
- **Operations:** Cloud hosting with automated backups

## Architecture & Key Decisions

- **One backend, two clients.** Web and mobile use the same API, so business rules live in one place.
- **Multi-tenancy by school id.** Every record carries a school identifier, so one deployment serves many schools with strictly separated data.
- **AI through controlled functions.** The model never gets raw database access. It calls a fixed set of functions that return only what the signed-in role may see.
- **Fetch first, then phrase.** The assistant gets the figures from the database first and then writes the reply. If the data does not exist, it says so instead of guessing.
- **Human approval before action.** Parent messages and tasks created by the AI wait for the principal's approval, and every message is kept in a communication history.
- **AI usage metered per plan.** Student limits, AI limits and plans are configurable by the platform admin.

## Key Features

**Core school management**
- School registration and profile
- Student admission, profiles, guardian details and bulk import
- Teacher and staff management with class and subject assignment
- Classes, sections and timetables
- Daily attendance (present, absent, late, leave)
- Fee structures, invoices, full and partial payments, receipts and defaulter lists
- Attendance and fee reports with PDF and Excel export
- Principal dashboard with live statistics
- Staff task assignment with due dates and reminders

**AI Smart Communication**
- Automatic SMS to parents when a student is marked absent
- Scheduled fee reminders and bulk announcements
- AI-written personalised messages with an admin approval step

**AI School Analyst**
- Detects repeated absences and declining attendance
- Detects pending fees and declining fee collection
- Recommends practical next steps based on the actual records
- Daily, weekly and monthly insight reports

**AI Principal Assistant**
- Principals ask in plain English: absent students today, pending fee this month, class with the lowest attendance, frequently absent students, monthly performance report
- Answers come only from the school's database

**AI Problem-Solving**
- Detect, analyse, recommend, approve and execute, then track the result
- Covers attendance, fee and academic problems, with before and after impact tracking

**Mobile app by role**
- Teacher: mark attendance, tasks, student list, notifications
- Principal: dashboard, AI assistant and insights, approvals, task assignment
- Accountant: record payments, defaulter list, share receipts, collection summary
- Everyone: secure login, push notifications, student search, call or SMS a parent, offline attendance with sync

## Challenges & How I Solved Them

**Keeping AI answers trustworthy.** A model that can invent numbers is a risk for fees and results. I limited it to approved database functions and required it to say when data is missing.

**Letting AI act without losing control.** Sending messages to parents is sensitive. Every AI-drafted message and action waits for approval and is logged.

**Data isolation between schools.** One school must never see another's records. Every record and query is scoped by school id and enforced on the server.

**Different needs per role.** Owners, principals, teachers and accountants need very different views. I defined role-based access up front and mapped each module and mobile screen to it.

**Teachers with poor connectivity.** Attendance can be marked offline in the Flutter mobile app and synced later.

## Outcome

A scoped proposal and technical plan for a school management SaaS covering web, mobile, four AI features and SMS, ready to move into build.

## Links

- Proposal available on request

[← Back to all projects](../README.md)
