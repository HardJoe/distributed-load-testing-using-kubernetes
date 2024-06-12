#!/usr/bin/env python

# Copyright 2015 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import random
import secrets

from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def post_dog(self):
        response = self.client.post("/dogs", json={
            "name": secrets.token_hex(20),
            "breed": f"Mixed {secrets.token_hex(20)}",
            "age": random.randint(1, 20)
        })

        self.response_data = response.json()
        id = self.response_data['id']

        self.client.get("/dogs", params={"id": id}, name="/dogs?id=[id]")
