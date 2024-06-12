from locust import HttpLocust, TaskSet, task
import random
import secrets


class UserTasks(TaskSet):

    @task
    def post_dog(self):
        self.client.post("/dogs", json={
            "name": secrets.token_hex(20),
            "breed": f"Mixed {secrets.token_hex(20)}",
            "age": random.randint(1, 20)
        })

    @task
    def get_dogs(self):
        self.client.get("/dogs")


class WebsiteUser(HttpLocust):
    task_set = UserTasks
