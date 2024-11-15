

# Security Configuration for Django Application

## HTTPS Configuration

1. **SSL/TLS Setup:**
   - Obtained SSL/TLS certificates using Let’s Encrypt and Certbot.
   - Configured Nginx to redirect all HTTP traffic to HTTPS and serve the application securely.

2. **Django Settings:**
   - `SECURE_SSL_REDIRECT = True`: Redirects HTTP to HTTPS.
   - `SECURE_HSTS_SECONDS = 31536000`: Enforces HTTPS for one year.
   - `SESSION_COOKIE_SECURE = True` and `CSRF_COOKIE_SECURE = True`: Ensures cookies are sent only over HTTPS.

3. **Headers for Security:**
   - `X_FRAME_OPTIONS = 'DENY'`: Prevents clickjacking attacks.
   - `SECURE_CONTENT_TYPE_NOSNIFF = True`: Stops browsers from MIME-sniffing.
   - `SECURE_BROWSER_XSS_FILTER = True`: Enables browser-based XSS protection.

## Web Server Configuration

- **Nginx:**
  - Redirects all HTTP traffic to HTTPS.
  - Uses strong TLS protocols and ciphers.

- **Certbot:**
  - Automatically renews SSL certificates every 90 days.

## Testing Tools

- **SSL Labs:**
  - [https://www.ssllabs.com/ssltest/](https://www.ssllabs.com/ssltest/)
  - Verified an A+ rating for SSL/TLS configuration.

## Additional Notes

- Ensure the deployment environment enforces security best practices.
- Regularly review logs for potential security breaches.
