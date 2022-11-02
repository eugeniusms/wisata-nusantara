## APIs

| Feature | Method | Note | Address |
| ------ | ------ | ------ | ------ |
| Authentication | GET | User Logged In | /auth/show-user-loggedin/json |
| Authentication | GET | All User | /auth/show-all-user/json |
| Destination | GET | All Destination | /destination/json/ |
| Destination | GET | All Likes | /destination/suka/json/ |

### ADMINs

`python manage.py dumpdata auth.user --indent 2 > dump.json`

| Username | Password |
| ----- | ----- |
| admin | wisatanusantara1234 |

