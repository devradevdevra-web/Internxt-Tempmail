# Internxt Temp Mail Client

A specialized Python client that interacts with Internxt's temporary email service (`internxt.com/temporary-email`). 

Built using `curl_cffi` to mimic real browser TLS fingerprints and bypass modern web firewalls or bot protections, this script allows you to programmatically generate temporary email addresses, fetch inbox data, and monitor messages in real time.

---

## Features

- **Browser Impersonation:** Uses `curl_cffi` with Chrome impersonation to seamlessly bypass automated bot detection and TLS fingerprinting.
- **Automated Mailbox Generation:** Connects directly to Internxt's API endpoint to provision a fresh temporary email address and session token.
- **Real-Time Inbox Polling:** Continuously monitors your active mailbox at customizable intervals.
- **Proxy Support:** Easily configured to route traffic through proxies to prevent rate-limiting or IP blocks.

---

## Prerequisites

Make sure you have Python 3.8+ installed along with the required third-party library:

```bash
pip install curl-cffi
