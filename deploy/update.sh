# create file: deploy/update.sh
#!/bin/bash

echo "🎮 Updating TiltPenguin GameDev PM..."

cd /home/pi/gamedev-pm
source venv/bin/activate

git pull origin main
pip install -r requirements.txt
python manage.py migrate --settings=config.settings_production
python manage.py collectstatic --noinput --settings=config.settings_production

sudo supervisorctl restart gamedev-pm

echo "✅ Update complete!"