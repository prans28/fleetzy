# Fleetzy Full Project — Final UI

Includes:
- Fleetzy public website with sticky glass header
- Obsidian / forest green / sage / warm-gold palette
- Responsive school mobility landing page
- Request Demo form
- SQLite database
- School Partnerships / School inquiries
- Fully branded Fleetzy Control Center
- Custom Fleetzy admin login
- Django theme toggle hidden
- Public and admin CSS configured through Django static files

## Windows PowerShell — fresh run

Extract the ZIP. Open PowerShell in the `Fleetzy_Django` folder (the folder containing `manage.py`).

```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

If activation is blocked:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\venv\Scripts\Activate.ps1
```

Open:
- Website: http://127.0.0.1:8000/
- Request demo: http://127.0.0.1:8000/request-demo/
- Fleetzy Control Center: http://127.0.0.1:8000/admin/

If old CSS is cached, press `Ctrl + Shift + R`.

Static-file checks:
- http://127.0.0.1:8000/static/inquiries/style.css
- http://127.0.0.1:8000/static/fleetzy_admin/admin.css
