# For use of co-developers working on Vexion

## Required dependencies

Navigate to the project folder and run `pip3 install -r requirements.txt`

Scss is installed separately through npm: `npm install -g sass`

Flask - Backend web framework (we will use this for now as it is lightweight and intuitive, but if userbase increases we will upgrade to FastAPI/Django)

Flask SQLAlchemy - Database management

Requests - API interactions

## Project navigation

Frontend files are in /static and /templates. The purpose of each should be intuitive. We use Scss for similar reasons to using Flask, but we can always upgrade to TailwindCSS if needed.

All python files are stored in /backend. 