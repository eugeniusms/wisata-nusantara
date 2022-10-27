release: sh -c 'python manage.py migrate && python manage.py loaddata initial_destinasi_data.json'
web: gunicorn wisata_nusantara.wsgi --log-file -