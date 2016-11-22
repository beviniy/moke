#-*- coding:utf-8 -*-
"""
Created on 2016-11-22
@author: bevin
"""

import os
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'clear *.pyc file from the root directory'

    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            '-s',
            action='store_true',
            dest='show',
            default=False,
            help='show pyc files instead of deleting them',
            )

    def handle(self, *args, **options):
        root = settings.PROJECT_ROOT
        for files in os.walk(root):
            for each_file in files[2]:
                if each_file.endswith('.pyc') or each_file.endswith('.pyo'):
                    pycfile = os.path.join(files[0], each_file)
                    if options['show']:
                        os.sys.stdout.write('%s...\n' % (pycfile))
                    else:
                        os.remove(pycfile)
                        os.sys.stdout.write('del %s...\n' % (pycfile))
