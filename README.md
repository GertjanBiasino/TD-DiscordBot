# Discord-to-TouchDesigner Bot

This project connects a Discord bot to TouchDesigner via TCP/IP. It allows users to send simple chat messages like `Speed in: 4.2`, and the values will update parameters inside TouchDesigner in real time.

---

## Requirements

### Software

- [Python 3.9+](https://www.python.org/downloads/)
- [TouchDesigner](https://derivative.ca/download)

### Python Packages

Install the required libraries using pip:

```bash
pip install discord.py flask
```


---

## Included Files

### `BotSender.py`

This Python script combines:

- A Discord bot that listens to messages in a server
- A TCP/IP client that connects to TouchDesigner
- Message parsing that:
  - Matches flexible parameter names
  - Accepts decimal values (with `.` or `,`)
  - Ensures values are between `0` and `10`
- Sends the result as JSON over TCP/IP (with a newline for parsing)

#### Expected message structure (examples):
every message should start with a point so the program knows its a command. 

.Speed in: 7.5
.Accel=3
.Zoomamount 2,1

This script connects to TouchDesigner via `localhost:7000` by default.

---

## Setup

1. Open `BotSender.py` in a text editor.
2. Replace the placeholder token with your actual Discord bot token:

   ```python
   client.run("YOUR_DISCORD_BOT_TOKEN_HERE")

You can get your token from the Discord Developer Portal.

3. Ensure the port number in BotSender.py matches the port used in the TCP/IP DAT inside the TouchDesigner project (default is 7000).

4. In TouchDesigner:

      Open the .toe file.
      Make sure the TCP/IP DAT is active and set to the same port.
      Confirm that the paramTable includes the expected parameter names in column 1.
---

## Running the Bot

1. Open a terminal or command prompt.
2. Navigate to the folder containing `BotSender.py`.
3. Run the script with:

```bash
python BotSender.py
```
The bot will connect to Discord and begin listening for messages. Any message that matches a parameter and includes a valid value will be forwarded to TouchDesigner.

---


## Message Format

The bot listens for messages in any Discord text channel it has access to. It looks for:

- A . in the beginning of a sencence
- A **parameter name**, matching a row in the `paramTable` (first column)
- A **value between 0 and 10** (either integer or float)
- Decimal separators can be **periods (`.`)** or **commas (`,`)**
- Any combination of spaces, colons (`:`), and equals signs (`=`) will be normalized

### Supported formats:

.Speed in: 5
.powerout=3.5
.zoomamount 7,1

> Note: The parameter name must match the first column in the `paramTable`, ignoring underscores, spaces, or punctuation.


---

## Examples

| Message Text        | Interpreted As            |
|---------------------|---------------------------|
| `Speed in: 5`       | `Speed_in = 5.0`          |
| `powerout=3.5`      | `Power_out = 3.5`         |
| `zoomamount 7,1`    | `Zoom_amount = 7.1`       |
| `SPEEDOUT 10`       | `Speed_out = 10.0`        |
| `Zoom amount=0`     | `Zoom_amount = 0.0`       |

If the parameter is not found, the bot will print a message like:
'speedout' is not a recognized parameter

If the value is missing or outside 0–10, the bot will ignore the message.






