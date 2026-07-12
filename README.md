# firefly-guitar-monitor
Send an email alert when new solid body Firefly guitars are available on guitarsgarden.com.

## Email setup

This monitor sends mail through Gmail SMTP.

Set these environment variables locally, or add them as GitHub repository secrets if running through GitHub Actions:

```text
EMAIL_ADDRESS=your-gmail-address@gmail.com
EMAIL_PASSWORD=your-google-app-password
TO_EMAIL=destination@example.com
```

For Gmail, use a Google app password for `EMAIL_PASSWORD`. Your normal Google account password will usually not work.

## Schedule

GitHub Actions starts the monitor every 5 minutes. The Python script only checks inventory between 7:00 PM and 7:00 AM America/Denver time.
