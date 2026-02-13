# Binance Futures Testnet Trading Bot

A simple Python CLI-based trading bot that places orders on the
Binance Futures Testnet (USDT-M).

This project was created as part of the Python Developer application task.

---

## Features
- Place MARKET and LIMIT orders on Binance Futures Testnet (USDT-M)
- Supports BUY and SELL sides
- Command-line interface (CLI) using argparse
- Input validation and error handling
- Modular and reusable code structure
- Logging of API requests, responses, and errors

---

## Project Structure
trading_bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── cli.py
├── .env
└── README.md
## Tech Stack
Language

Python 3

Libraries / Tools

python-binance — Binance Futures Testnet API interaction

argparse — CLI input handling

logging — structured logging

python-dotenv — environment variables management

API

Binance Futures Testnet (USDT-M)

REST API via python-binance

Concepts Used

CLI application development

API integration

Exception handling

Input validation

Logging system

Modular project structure


