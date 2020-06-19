from locust import HttpUser, TaskSet, task, between

class MyTaskSet(HttpUser):
   wait_time = between(3,5)

   @task
   def index(self):
       self.client.get("/")