# iCareManager — Case Study

## Overview
iCareManager is a healthcare management platform used to run day-to-day clinical and administrative operations. It is built as a distributed set of microservices on ASP.NET MVC and .NET Core, with an Angular front end.

## My Role
I work on it full time as a Senior Software Engineer (since 02/2022), remote for a US team. My work:
- Designed and implemented a **centralized logging microservice** with Serilog and OpenTelemetry, and wrote an SDK wrapper so every service integrates it the same way
- Built and improved **ASP.NET MVC 4.7 and .NET Core 6/9 modules**: dynamic label management, complex forms and module-level permissions
- Built UI with Jade and Angular 10
- Diagnosed and fixed production issues, and refactored existing features to reduce bugs and latency
- Use AI-assisted engineering (OpenAI API, Claude Code, Antigravity) to speed up feature delivery, refactors and debugging across the microservices codebase

## The Problem
A clinical platform has many modules, each with its own forms, labels and permissions. Logs from many services are hard to follow, and production issues are hard to trace without one consistent standard.

## The Solution
- One logging service and SDK, so every microservice logs in the same format
- Reusable dynamic labels, forms and permissions, so modules stay consistent and easy to maintain

## Tech Stack
- **Backend:** ASP.NET MVC 4.7, .NET Core 6 / 9
- **Front end:** Angular 10, Jade
- **Database:** MS SQL Server
- **Observability:** Serilog, OpenTelemetry

## Key Features
- Dynamic forms and label management
- Module-level permissions
- Centralized logging across microservices, with an SDK wrapper

## Links
- Website: https://icaremanager.com

[← Back to all projects](../README.md)
