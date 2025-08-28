# Discord Server Cleanup Bot

A simple Discord bot built with **discord.py** that allows administrators to:

- 🗑️ Delete all roles in a server (except `@everyone` and roles above the bot).
- 🧹 Delete all messages from a specific user across all channels.

⚠️ **Warning:** These actions are destructive and **cannot be undone**. Use only in servers where you have permission.

---

## Features
- `!delroles` → Ask for confirmation, then delete all server roles.
- `!delusermsg @user` → Delete all messages from the mentioned user across all text channels.
- Confirmation system for safety.
- Only administrators can run these commands.

---

## Installation

1. Clone or download this repository.
2. Install requirements:
   ```bash
   pip install -r requirements.txt
