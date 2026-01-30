# Web Application Project

## Deployment Notes

This web application requires specific file ownership for the web server to function correctly.

### Ownership Requirements

- Configuration files should be owned by `www-data:www-data`
- The web server runs as the `www-data` user
- Files must be readable by the web server user

### Current Status

Check file ownership with:
```bash
ls -l
```

If files are not owned by `www-data`, fix with:
```bash
sudo chown www-data:www-data config.json
```

### Why This Matters

Web servers run as specific users (not root) for security. Files the web server needs must be accessible to that user. This is the "principle of least privilege" - services get only the access they need.
