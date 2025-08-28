

# 🧹 Discord Cleanup Bot By NAINOO

A Discord bot built with **discord.py** that can:

- 🚮 Delete **all roles** in a server (except `@everyone` and roles above the bot).
- 🗑️ Delete **all messages from a specific user** across all text channels.

⚠️ **Warning:** These actions are destructive and **cannot be undone**.  
Use only if you are the server owner or have permission to do so.


## 📌 Features

- `!delroles` → Deletes all roles after confirmation.
- `!delusermsg @user` → Deletes all messages from the mentioned user across all text channels.
- Confirmation prompt before deleting roles.
- Requires Administrator permissions for safety.

---

## 📦 Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
````

**requirements.txt**

```
discord.py==2.3.2
python-dotenv==1.0.1   # optional, for loading token from .env
```

---

## ⚙️ Setup

1. Clone or download this repository.

2. Create a file named **`.env`** in the project root:

   ```
   DISCORD_TOKEN=your_bot_token_here
   ```

3. Create a file named **`bot.py`** and add your bot code.

4. Run the bot:

   ```bash
   python bot.py
   ```

---

## 🚀 Usage

* `!delroles`
  → Bot asks for confirmation, then deletes all roles (except `@everyone` and higher roles).

* `!delusermsg @username`
  → Deletes all messages from that user across all text channels.

---

## 🔑 Permissions Needed

* **Administrator** → for deleting roles.
* **Manage Messages** → for deleting user messages.
* Make sure the bot’s role is **above all other roles** you want to delete.

---

## ⚠️ Limitations

* The bot cannot delete the `@everyone` role.
* The bot cannot delete roles above its highest role.
* The bot cannot delete messages older than **14 days** (Discord API limitation).
* Deleting many messages may be slow because they are removed one by one.

---

## 🛠️ Example Commands

* Delete all roles:

  ```
  !delroles
  ```

  → Bot will ask: “⚠️ Are you sure? Type `!confirmdel` to continue.”

* Delete all messages from a user:

  ```
  !delusermsg @username
  ```

---

## 👨‍💻 Author

Made with ❤️ using **discord.py**.
For educational and server maintenance use only.

```

---

👉 Do you want me to also prepare the **full `bot.py` code** that already includes both commands (`!delroles` + `!delusermsg`) so you can copy-paste and run immediately?
```
