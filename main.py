import time
from curl_cffi import requests

class InternxtTempMail:
    BASE_URL = "https://internxt.com"

    def __init__(self, email=None, token=None):
        self.session = requests.Session(impersonate="chrome110")
        self.email = email
        self.token = token
        
        self.headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "en-US,en;q=0.7",
            "priority": "u=1, i",
            "referer": f"{self.BASE_URL}/temporary-email",
            "sec-ch-ua": '"Brave";v="155", "Chromium";v="155", "Not(A:Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "sec-gpc": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36",
            "cookie": (
                "_ga_4MJH1Y6RS3=GS2.1.s1792597715$o1$g1$t1792597904$j60$l0$h1259813859$dIts-2PFGddMTSxeI-u1oQLXCCeY1ZwUMBw; "
                "csrfSecret=pCx-bOKgdajhm_5fIjo43n9o; "
                "XSRF-TOKEN=LywhpquC-uSMsALNWPsgh-AzOc_YUr6QI8HY.%2F4Fg8vXlkID9VjkFxJuYOIxZup6C29BzdEOmulkUXrM; "
                "_cfuvid=q_MpyWhMqsQQ6kdRWQx9iuahtDqlkBlSGij16kkK.Wg-1792598357.1297152-1.0.1.1-AkDPBVsyPO7fe2qyfXRGFcVttv_1i48IPxCZGwfRiKY; "
                "_gcl_au=1.1.949887224.1792598361"
            )
        }

    def create_email(self):
        url = f"{self.BASE_URL}/api/temp-mail/create-email"
        response = self.session.get(url, headers=self.headers)
        
        if response.status_code == 200:
            data = response.json()
            self.email = data.get("address")
            self.token = data.get("token")
            return data
        else:
            print(f"Failed to create email: {response.status_code} - {response.text}")
            return None

    def get_inbox(self):
        if not self.email or not self.token:
            print("Error: Email and token are required to check the inbox.")
            return None

        url = f"{self.BASE_URL}/api/temp-mail/get-inbox"
        params = {
            "email": self.email,
            "token": self.token
        }
        
        response = self.session.get(url, headers=self.headers, params=params)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch inbox: {response.status_code} - {response.text}")
            return None

    def watch_inbox(self, interval=5):
        print(f"Watching inbox for {self.email} (checking every {interval}s)... Press Ctrl+C to stop.")
        try:
            while True:
                inbox = self.get_inbox()
                if inbox:
                    print(f"Inbox response: {inbox}")
                time.sleep(interval)
        except KeyboardInterrupt:
            print("\nStopped watching inbox.")

if __name__ == "__main__":
    mail = InternxtTempMail()
    session_data = mail.create_email()
    if session_data:
        print(f"Address: {mail.email}")
        print(f"Token: {mail.token}")
        mail.watch_inbox(interval=5)
