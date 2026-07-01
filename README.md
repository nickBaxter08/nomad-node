# NOMAD Node

IoT-based homelab monitoring system built with Raspberry Pi Pico 2 W.

## Overview

NOMAD Node collects hardware and network metrics from a Raspberry Pi Pico 2 W and sends data to a self-hosted monitoring server.

## Features

- Temperature monitoring
- Humidity monitoring
- Network health checks
- Server uptime tracking
- Web dashboard visualization

## Hardware

- Raspberry Pi Pico 2 W
- BME280 Sensor
- SSD1306 OLED Display
- Optional INA219 Power Sensor

## Software

### Firmware
- MicroPython

### Backend
- Python
- FastAPI
- SQLite

### Deployment
- Docker
- ZimaOS

## Architecture

Pico 2 W
↓
WiFi
↓
FastAPI Server
↓
Database
↓
Dashboard

## Status

Currently in development.
