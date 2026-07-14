# 💀 Windows Prank Script

A simple Python prank script that creates a chaotic Windows experience by opening multiple Command Prompt windows, launching an image repeatedly, and finally scheduling a system shutdown.

> ⚠️ **Educational & Entertainment Purposes Only**
> Use this script **only on your own computer** or with the permission of the device owner. Do not use it to disrupt, annoy, or damage someone else's system.

---

## ✨ Features

- 🖥️ Opens multiple Command Prompt windows
- 🖼️ Launches an image repeatedly in the default browser
- ⏳ Configurable shutdown countdown
- 💬 Custom shutdown message
- ⚡ Fully customizable prank intensity

---

## 📋 Requirements

- Windows 10/11
- Python 3.8+

---

## 🚀 Installation

```bash
git clone https://github.com/Gireesh-mlgs/Prank-Windows
cd Prank-Windows
```

Run:

```bash
python app.py
```

---

## ⚙️ Configuration

Modify these variables inside the script:

```python
message = "Your pc cooked."
delay_seconds = 10
number_of_pranks = 100
chaos_duration = 3
image_url = "YOUR_IMAGE_URL"
```

| Variable | Description |
|----------|-------------|
| `message` | Shutdown warning message |
| `delay_seconds` | Countdown before shutdown |
| `number_of_pranks` | Number of CMD windows/images |
| `chaos_duration` | Delay before shutdown command |
| `image_url` | Image opened during the prank |

---

## 🛑 Cancel Shutdown

If the shutdown countdown has started, open Command Prompt and run:

```cmd
shutdown /a
```

---

## 📂 Project Structure

```
windows-prank/
│
├── prank.py
├── README.md

```

---

## ⚠️ Disclaimer

This project is intended for **learning Python automation** and harmless demonstrations on systems you own or have permission to test.

The author is **not responsible** for misuse, data loss, or any damages caused by running this software.

---


⭐ If you enjoyed this project, consider giving it a star!
