# DjTranslation
Django Multi Language (Translation)
## First Step
- You need to install gettext on your system
 ```bash
sudo apt-get update
sudo apt-get install gettext
```

## Second Step
- Add to your settings.py
```python
# add this line in MIDDLEWARE
MIDDLEWARE = [
    # ...
"django.middleware.locale.LocaleMiddleware",
    # ...
]
# add LOCALE_PATHS and LANGUAGES
LOCALE_PATHS=[
    os.path.join(BASE_DIR, 'locale'),
]

LANGUAGES = [
    ("en", "English"),
    ("ar", "Arabic"),
]


LANGUAGE_CODE = "en"
```
## Third Step
- You need to specify the words and sentences that you will translate
- In Views.py
```python
from django.utils.translation import gettext as _
def home(request):
    books_title = _('Books')
    description = _('A list of our available books.')
    return render(request, "home.html", {"title": _("Home")})
```
- In Models.py
```python
from django.utils.translation import gettext as _
class Book(models.Model):
    title = models.CharField(_("Title"), max_length=255)
    description = models.TextField(_("Description"))
```
- In Templates
```python
{% load i18n %}
{% trans "Title" %}
```
## Fourth Step
- Run this command to create the locale folder
```python
django-admin makemessages -l ar
```
- You will find a folder called locale and inside it a folder called ar
- Open the file django.po and add your translation
- Run this command to compile the translation
```python
django-admin compilemessages
```
## Fifth Step
- create a middleware.py file and add this code
```python
from django.utils import translation


class LanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if "lang" in request.GET:
            lang = request.GET["lang"]
            translation.activate(lang)

        response = self.get_response(request)

        return response

```
- This middleware will change the language according to the lang parameter in the url
- Add this line in MIDDLEWARE
```python
MIDDLEWARE = [
    # ...
    "your_app_name.middleware.LanguageMiddleware",
    # ...
]
```

# An example of how to use it
- ```http://127.0.0.1:8000/?lang=ar```
- ```http://127.0.0.1:8000/book_list/?lang=ar```
- ```http://127.0.0.1:8000/1/?lang=ar```
- ```http://127.0.0.1:8000/admin/?lang=ar```
- ```http://127.0.0.1:8000/<any-endpoint>/?lang=ar```
