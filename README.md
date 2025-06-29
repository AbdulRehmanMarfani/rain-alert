
---

# Rain Alert SMS Notifier ☔

A Python script that checks your local weather forecast and sends you an SMS if rain is expected during your daily commute — so you never leave home without an umbrella!

---

## Features 🌧️

* **Commute-Focused Forecast**: Scans the next 12 hours using OpenWeatherMap’s 3-hour forecast API.
* **Rain Detection**: Identifies if any interval has a weather condition code indicating rain (ID < 700).
* **SMS Notification**: Sends an SMS alert using Twilio.
* **Daily Automation**: Scheduled to run every morning at 9 AM Pakistan Time via GitHub Actions.

---

## Requirements 🛠️

* Python 3.6+
* `requests` module (`pip install requests`)
* `twilio` module (`pip install twilio`)
* OpenWeatherMap API key
* Twilio account with verified phone number
* GitHub Actions enabled with repository secrets configured

---

## Files Included 📂

1. **`main.py`**: The core logic — fetches forecast data, checks for rain, and sends SMS alerts.
2. **`requirements.txt`**: Lists required packages for the script.
3. **`.github/workflows/rain_alert.yml`**: GitHub Actions workflow to automate daily runs.

---

## How to Use? 🧭

1. Clone the repository or download the source code.

2. Replace the placeholder coordinates in `main.py`:

   ```python
   MY_LAT = 00.000000       # Your latitude
   MY_LONG = 00.000000      # Your longitude
   ```

3. Add your secrets in your GitHub repository:
   Go to **Settings → Secrets and variables → Actions** and add:

   * `OWM_API_KEY` — your OpenWeatherMap API key
   * `TWILIO_ACCOUNT_SID` — your Twilio account SID
   * `TWILIO_AUTH_TOKEN` — your Twilio auth token

4. Make sure dependencies are installed (if testing locally):

   ```bash
   pip install -r requirements.txt
   ```

5. Run the script manually (optional):

   ```bash
   python main.py
   ```

   Or let GitHub Actions run it for you every morning.

---

## Goal 🎯

* You’ll receive an SMS **only if**:

  * Rain is expected in any of the next 4 forecast intervals (≈12 hours)
  * Weather code returned is less than 700 (indicating rain, drizzle, or storm)

---

## Future Enhancements 🚀

* Include expected rain time and temperature in the SMS
* Add support for Telegram or WhatsApp notifications
* Log rain alerts to a Google Sheet or Notion DB
* Add city name and summary of conditions to the alert

---

## Developer Note 🧑‍💻

> This was my **first automation script involving weather prediction and messaging APIs**. I learned how to:
>
> * Work with real-world forecast data from OpenWeatherMap
> * Parse and filter API results based on condition codes
> * Send SMS using Twilio’s Python SDK
> * Automate everything with GitHub Actions and secrets

A great step forward into practical Python automation.

---

## Credits ✨

* **Programming**: Abdul Rehman Marfani
* **APIs Used**: OpenWeatherMap, Twilio
* **Automation**: GitHub Actions

---

