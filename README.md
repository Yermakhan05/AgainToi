# Event Application

This project is a web-based event application that allows users, venue companies, and show companies to manage events, venues, and bookings. The application provides users with an intuitive interface for event browsing and reservations, while companies can manage their profiles and orders.

## Table of Contents

- [Objective](#objective)
- [Features](#features)
- [Functional Requirements](#functional-requirements)
- [Non-Functional Requirements](#non-functional-requirements)
- [API Documentation](#api-documentation)
- [Installation](#installation)
- [Usage](#usage)
- [Assumptions and Dependencies](#assumptions-and-dependencies)
- [License](#license)

## Objective

The objective of this application is to create a platform where users can:
- Browse event venues and shows.
- Make reservations and manage their profiles.

For companies:
- Venue and show companies can manage profiles, bookings, and orders.

## Features

### User Interface
- **Registration and Profile Management**: Users can register, log in, and update their profiles (including uploading profile photos).
- **Event Booking**: Users can add events or shows to their cart and place orders.
- **Search**: Users can search for venues and shows using keywords and filters.

### Venue Company Interface
- **Profile Management**: Venue companies can register, edit profiles, and manage hall details.
- **Order Management**: Venue companies can accept or reject event orders.

### Show Company Interface
- **Profile Management**: Show companies can register, edit profiles, and manage services (host, photographer, dancers, etc.).
- **Order Management**: Show companies can accept or reject show bookings.

## Functional Requirements

### Home App
- **About Us Page**: Provides detailed information about the company, its mission, and the services it offers.
- **Contact Us Page**: A page with a contact form allowing users to send inquiries or report issues directly to the company.
- **Media (User Reviews)**: A section that displays user reviews and feedback about the venues, shows, and events offered through the platform.

### Main App
- **Search Places**: Users can search for venues using filters (e.g., location, type of venue).
- **Search Shows**: Users can search for shows based on various parameters (e.g., genre, location).

## Non-Functional Requirements
- **Performance**: The system should respond to user requests within 2 seconds.
- **Security**: All users must be authenticated and authorized.
- **Accessibility**: The interface will be simple and user-friendly for all users.

## API Documentation

### Authentication

#### POST /api/register/
- **Description**: Registers a new user (individual, venue company, or show company).
- **Request Body**:
  ```json
  {
      "username": "newuser",
      "password": "password123",
      "type": "venue"
  }
