# TODO: Change Application Name from MediFirst to MediCare

## Information Gathered
- The application is a Django-based online pharmacy store.
- "MediFirst" appears in multiple HTML templates as titles, branding, and content.
- No occurrences found in Python files (.py), so changes are limited to templates.
- Templates affected include base.html, index.html, admin_dashboard.html, user_dashboard.html, and others.
- The name appears in titles, footers, headers, social links, and descriptive text.

## Plan
- Replace all instances of "MediFirst" with "MediCare" in HTML templates.
- Ensure consistency across all pages (titles, branding, emails, etc.).
- Update social media links if necessary (e.g., Twitter handle from MediFirst2 to MediCare2, but confirm if this is desired).
- Test the application after changes to ensure no broken links or display issues.

## Dependent Files to be Edited
- templates/base.html
- templates/index.html
- templates/admin_dashboard.html
- templates/user_dashboard.html
- templates/terms.html
- templates/disclaimer.html
- templates/privacy.html
- templates/developers-section.html
- templates/cart.html
- templates/cartempty.html
- templates/login.html
- templates/register.html
- templates/orders.html
- templates/search.html
- templates/registration/password_reset_done.html
- templates/registration/password_reset_complete.html

## Followup Steps
- After editing, run the server and check key pages (home, login, register, admin/user dashboards).
- Verify that titles, footers, and branding display "MediCare".
- If social media handles need changing, update them accordingly.
- Confirm no 404 errors or missing assets.

## Completed Changes
- Updated index.html: Replaced "MediFirst" with "MediCare" in content, testimonials, and email.
- Updated base.html: Changed social media links from MediFirst2 to MediCare2 and medi.first.3 to medi.care.3.
- Updated disclaimer.html: Changed email from MediFirst444@gmail.com to MediCare444@gmail.com.
- Updated privacy.html: Replaced all instances of "MediFirst" with "MediCare" in domain names and content.
- Updated services.html: Changed title from "MediFirst | Services" to "MediCare | Services".
- Fixed CSS syntax error in services.html by adding missing closing brace.
