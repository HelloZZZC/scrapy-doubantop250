#!/usr/bin/python
# -*- coding: utf-8 -*-

from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
import random
from scrapy.utils.project import get_project_settings

class UserAgentPoolMiddleware(UserAgentMiddleware):
    def process_request(self, request, spider):
        settings = get_project_settings()

        agent = random.choice(settings['USER_AGENT'])

        if agent:
            request.headers['User-Agent'] = agent