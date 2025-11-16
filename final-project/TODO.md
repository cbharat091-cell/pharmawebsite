# TODO: Fix 404 Error on Vercel Deployment

- [x] Create vercel.json in root directory (/workspaces/pharmawebsite) to configure Vercel build for Django
- [x] Rename final-project/requirements_personal.txt to final-project/requirements.txt
- [x] Update final-project/final_pro/settings.py: Set DEBUG=False, ALLOWED_HOSTS=['*'], uncomment and set STATIC_ROOT
- [x] Run python manage.py collectstatic in final-project directory to collect static files
- [ ] Deploy to Vercel and test the application
