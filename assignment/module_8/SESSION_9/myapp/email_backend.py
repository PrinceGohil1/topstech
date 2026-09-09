"""
Custom SMTP email backend that uses certifi's CA bundle.

Needed on macOS where Python 3.x does not trust the system
certificate store by default, causing SSLCertVerificationError
when connecting to smtp.gmail.com.
"""

import ssl
import certifi
from django.core.mail.backends.smtp import EmailBackend as BaseEmailBackend


class CertifiEmailBackend(BaseEmailBackend):
    """
    Extends Django's built-in SMTP backend to inject a certifi-based
    SSL context, fixing SSLCertVerificationError on macOS / Python 3.x.
    """

    def open(self):
        """
        Override open() to attach a certifi SSL context before
        the STARTTLS handshake is performed.
        """
        # Build an SSL context that trusts certifi's CA bundle
        self.ssl_context = ssl.create_default_context(cafile=certifi.where())
        return super().open()
