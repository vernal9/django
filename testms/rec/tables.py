import django_tables2 as tables
from django_tables2.utils import A
from django.utils.html import format_html
from django.urls import reverse
from .models import RRequest

class RequestTable(tables.Table):
    id_select = tables.CheckBoxColumn(accessor="ID", orderable=False, exclude_from_export=True)
    actions = tables.Column(empty_values=(), verbose_name="操作", orderable=False, exclude_from_export=True)

    #ID = tables.LinkColumn('rec:rec-update', args=[A('pk')])
    #CandidatesName = tables.LinkColumn('rec:rec-del', args=[A('pk')])

    class Meta:
        model = RRequest
        #fields = ['ID']
        #attrs = {'class': 'paleblue'}
        #表格中顯示順序
        #sequence = ['id_select'] + fields + ['actions']

        # 表格样式
        attrs = {"class": "table table-striped table-sm text-nowrap"}

        # 自定義連結
    def render_actions(self, value, record):
        return format_html(
            '<a class="btn btn-sm badge badge-pill badge-warning ml-2" href= "' +
            reverse("rec:rec-update", args=[str(record.pk)]) + '">' + '編輯' + '</a>'
            + '<a class=" btn  btn-sm badge badge-pill badge-danger ml-2" href= "' +
            reverse("rec:rec-del", args=[str(record.pk)]) + '">' + '刪除' + '</a>'
            )
