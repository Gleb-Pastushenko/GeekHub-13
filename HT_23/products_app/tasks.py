from celery import shared_task

from products_app.parser import Parser


@shared_task
def start_subprocess(id_list):
    Parser(id_list).run()
