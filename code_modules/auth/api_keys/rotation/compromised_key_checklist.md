# Compromised API Key Checklist

1. Revoke the exposed key immediately.
2. Generate a new key.
3. Update local `.env` files.
4. Update deployment secrets.
5. Check Git history for leaked values.
6. Rotate related service credentials if needed.
7. Document the incident in `incident_response.md`.
