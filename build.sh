.\.venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
reflex init
reflex export --frontend-only 
Remove-Item -Path public
Expand-Archive -Path "frontend.zip" -DestinationPath "public"
Remove-Item -Path frontend.zip 
deactivate
