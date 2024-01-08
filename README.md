# signal-async-actions

This sample uses Celery to retrieve blog thumbnail images from an external source asynchronously after the blog is created.

![](https://raw.githubusercontent.com/EveSquare/signal-async-actions/main/admin_screenshot.png)

*redis
`redis-server`

*celery worker
`celery -A config worker -l INFO`

*django
`pipenv run start`

flower
`celery -A config flower --address=0.0.0.0 --port=5555`

*:required