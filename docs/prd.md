# Product Requirements Document (PRD): Monkey Logs

## 1. Introduction

The goal of the Monkey Logs application is to provide a comprehensive training platform with two distinct user experiences: a mobile-first app for Individuals and a web-based portal for Coaches. This document outlines the functional and non-functional requirements for the initial launch, or "Minimum Viable Product" (MVP), focusing on these two primary user types.

## 2. Goals & Objectives

Primary Goal: Empower individuals to track and analyze their training while providing coaches with robust tools to manage and monitor their students.

### Key Metrics (KPIs):

- User Engagement: DAU/WAU for both mobile and web platforms.
- Retention: User retention rate after 30 days for both user types.
- Coach Adoption: Number of active coaches and the average number of students per coach.
- Workout Completion: Percentage of assigned workouts completed by students.

## 3. Functional Requirements (User Stories)

### Authentication & Profile Management

- As a new user, I can create an account and select my role (Individual or Coach).
- As an Individual, I can manage my profile on the mobile app.
- As a Coach, I can manage my profile and team on the web portal.
- As a user, I can securely log in and out of the respective platforms.

### Individual User (Mobile App)

- As an Individual, I can quickly log a new workout or climb from a single, prominent button.
- As an Individual, I can quickly log a climb with details like grade, type, and location.
- As an Individual, I can quickly log climbing specific exercises. Fingerboard training, Aerobic wall training...
- As an Individual, I can quickly log standard exercises. Pull ups, bench press...
- As an Individual, I can create template workouts, template weekly training plans and reuse them.
- As an Individual, I can view my performance dashboard on my phone to track my progress.
- As an Individual, I can see training plans and workouts assigned to me by my coach.
- As an Individual, I can communicate with my coach through the app.

- As an Individual, I can view my performance dashboard on my phone to track my progress.
- As an Individual, I can see training plans and workouts assigned to me by my coach.
- As an Individual, I can create new custom exercises, whether climbing-specific or not.
- As an Individual, I can communicate with my coach through the app.

### Coach User (Web Portal)

- As a Coach, I can manage my roster of students and view their individual dashboards.
- As a Coach, I can create and assign structured training plans to my students or groups of students.
- As a Coach, I can review logged climbs and workouts and provide feedback.
- As a Coach, I can analyze the collective performance of my team or a specific student over time.

### Shared Features

- As a user, I can contribute new routes to a user-generated database.

## 4. Non-Functional Requirements

- **Platform:** The application will have two distinct interfaces: a native mobile app for iOS and Android for Individuals and a responsive web portal for Coaches.
- **Performance:** Both platforms must be fast and responsive, with load times under 2 seconds.
- **Security:** All user data, including training plans and communication, must be encrypted and secure.
- **Scalability:** The backend must be designed to handle a large number of users and the hierarchical relationships between coaches and students.
