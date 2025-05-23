# ⚡ Voltq: The Asynchronous Python Task Queue for MQTT & Beyond 🚀

**Voltq is a modern, lightweight, and highly pluggable distributed task queue for Python, built with an `asyncio`-first approach.**

Inspired by robust systems like Celery and TaskIQ, Voltq aims to provide a streamlined and efficient experience, especially for applications leveraging **MQTT** (e.g., EMQX, Mosquitto) as a message broker. It's designed from the ground up to be suitable for both powerful servers and **low-resource environments**.

## Key Goals & Features:

*   **MQTT-Centric Design:** Natively supports MQTT features for task distribution, making it ideal for IoT and microservice architectures that rely on MQTT.
*   **Fully Asynchronous:** Leverages Python's `asyncio` for high-performance, non-blocking I/O operations.
*   **Pluggable Architecture:**
    *   **Brokers:** Easily switch between different message brokers. Initial focus on MQTT, with plans for Redis, RabbitMQ, and others.
    *   **Result Backends:** Flexible options for storing task results (e.g., Redis, databases, or even an MQTT-based backend).
*   **Lightweight & Low Resource:** Optimized for minimal CPU and memory footprint.
*   **Simple & Intuitive API:** Striving for ease of use in defining, sending, and processing tasks.
*   **Core Task Management:** Includes essential features like task serialization, retries, and state tracking.
*   **Modern Python:** Built with modern Python features and type hinting.

## Current Status

🚧 **Under Active Development (MVP `v0.1.0` in progress!)** 🚧

We are currently focused on delivering the Minimum Viable Product (MVP) which will include:
*   Core task definition and sending.
*   MQTT Broker Adapter (targeting Mosquitto/EMQX, with support for Shared Subscriptions).
*   Redis Result Backend.
*   Basic CLI for running workers.
*   Asynchronous task execution.

## Why Voltq?

While existing solutions are powerful, Voltq aims to fill a niche for developers who:
*   Primarily use MQTT and want a task queue that feels native to that ecosystem.
*   Need a lightweight solution for resource-constrained devices.
*   Prefer an `asyncio`-native library from the core.
*   Desire a high degree of pluggability for brokers and backends without excessive complexity.

**Join us in building a flexible and efficient task queuing system for modern Python applications! Contributions, feedback, and ideas are highly welcome.**

---
