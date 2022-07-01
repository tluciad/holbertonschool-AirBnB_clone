#!/usr/bin/python3
import datetime

import uuid

datetime_object = datetime.datetime.now()
print(datetime_object)
print(uuid.uuid4())
print(type(str(uuid.uuid4())))