import django_tables2 as tables
from .models import ServerValue

class ServerValueTable(tables.Table):

    class Meta:
        model = ServerValue
        template_name = "django_tables2/bootstrap.html"
        fields = ("StringValue2",)