#!/usr/bin/env python3

import os
import json
env = {}
for env_key, env_value in os.environ.items():
    env[env_key] = env_value
print("Content-Type: application/json") #let the browser know to expect plain text
print()
print(json.dumps(env))