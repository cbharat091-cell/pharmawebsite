# Render Deployment Fixes

## Issues Found:
1. render.yaml has conflicting configurations (Docker runtime + Procfile command)
2. Dockerfile has wrong Python version and directory structure issues
3. requirements.txt contains invalid `Python==3.13.0` (Python isn't a pip package)

## Fix Plan:
- [x] Fix render.yaml - remove conflicting settings for Docker deployment
- [x] Fix Dockerfile - correct Python version, fix working directory, add proper env setup
- [x] Fix requirements.txt - remove invalid Python version line

## Status:
- [x] Completed

## Changes Made:

### Dockerfile:
- Added `--no-cache-dir` to pip install for smaller image size
- Fixed `COPY` command to properly copy `final-project/` directory
- Added `WORKDIR /app/final-project` before running manage.py
- Added `--bind 0.0.0.0:8000` to gunicorn command for proper binding

### requirements.txt:
- Removed invalid `Python==3.13.0` line (Python version is set in Dockerfile, not pip)

### render.yaml:
- No changes needed - already correctly configured for Docker deployment

---

# Vercel Deployment Plan

## Current Status:
- [x] Create vercel.json in root directory (/workspaces/pharmawebsite) to configure Vercel build for Django
- [x] Update final-project/final_pro/settings.py with Vercel-specific configurations (database path, static files)
- [x] Configure api/app.py for Vercel serverless function
- [x] Run python manage.py collectstatic in final-project directory to collect static files

## Pending Tasks:
- [ ] Deploy to Vercel and test the application
- [ ] Configure environment variables in Vercel dashboard

### Vercel Deployment Steps:
1. Install Vercel CLI: `npm i -g vercel`
2. Login to Vercel: `vercel login`
3. Deploy from root directory: `vercel --prod`
4. Configure environment variables in Vercel dashboard:
   - SECRET_KEY (generate a secure random key)
   - DEBUG=False
   - VERCEL=1 (required for proper database path handling)

---

# Render Deployment Plan

## Current Status:
- [x] Dockerfile properly configured for Docker deployment
- [x] requirements.txt updated with all dependencies
- [x] render.yaml configured for Docker runtime

## Pending Tasks:
- [ ] Connect GitHub repository to Render
- [ ] Create a new Web Service with Docker environment
- [ ] Configure environment variables in Render dashboard

### Render Deployment Steps:
1. Connect GitHub repository to Render
2. Create a new Web Service:
   - Environment: Docker
   - Build Command: (empty - uses Dockerfile)
   - Start Command: (empty - uses Dockerfile CMD)
3. Set environment variables in Render dashboard:
   - SECRET_KEY
   - DEBUG=False

---

# Verification Steps:
- [ ] Test homepage loads correctly
- [ ] Test user registration/login
- [ ] Test product browsing
- [ ] Test cart functionality
- [ ] Verify static files are served correctly

