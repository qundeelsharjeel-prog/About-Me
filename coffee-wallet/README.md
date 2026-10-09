# Coffee Wallet — Case Study

## Overview
Coffee Wallet is a prepaid coffee card app for the Kuwait market — customers load a balance and pay for coffee from their phone.

## My Role
- Wrote the **Software Requirements Specification (SRS)**, derived from the Figma design pages
- Prepared the **client questions list** to close requirement gaps before build
- Defined the technical stack and architecture
- Managed work as tickets in ClickUp

## The Problem
Before development can start safely, the design has to be turned into precise, testable requirements, and every ambiguity needs an answer from the client.

## The Solution
A complete SRS tied directly to the approved Figma screens, plus a structured list of open questions for the client, so the build team starts with clear scope.

## Tech Stack
- **Backend:** FastAPI (Python)
- **Frontend:** React 19
- **Database:** MongoDB
- **Architecture:** Clean Architecture + DDD, no duplicated code
- **Project layout:** separate `backend/` and `frontend/` folders

## Architecture & Key Decisions
- **Separate backend and frontend folders** so each can be built, tested and deployed independently.
- **Clean Architecture + DDD** to keep wallet/payment rules isolated from framework code.
- **Real `.env` configuration with a local MongoDB** (no Docker) for a simple developer setup.

## Key Features
- Prepaid card / wallet balance
- Flows defined screen by screen from the Figma design
- Requirements and open questions tracked in ClickUp

## Links
- Website: http://13.207.211.168/

[← Back to all projects](../README.md)
