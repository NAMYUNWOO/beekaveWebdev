from django.contrib import admin
from reviewPage.models import reviewMovie,reviewGame,reviewTV
# Register your models here.
admin.site.register(reviewMovie)
admin.site.register(reviewGame)
admin.site.register(reviewTV)
