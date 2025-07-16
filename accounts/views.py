from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView


class SignUpView(CreateView):
    form_class = UserCreationForm # {"form": UserCreationForm}
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"  


# {'a': "apple", "b": "banana", "c": True, "d": None, "e": "elderberry"}


# '{"a": "apple", "b": "banana", "c": true, "d": null, "e": "elderberry"}'


# mmt  python
# "http://irctc/train-search?from=delhi&to=mumbai&date=2023-10-01"

# reqests.get("http://irctc/train-search", params={"from": "delhi", "to": "mumbai", "date": "2023-10-01"})



# python
# boto3

