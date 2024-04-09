import django_tables2 as tables
from .models.Recruit_Request import Recruit_Request

class RRList(tables.Table):
    #TEMPLATE = """<input id="IsFinished" maxlength="100" name="IsFinished" type="text"/>"""
    TEMPLATE = """
    <select>
    <option>0
    <option>1
    </select>
    """
    #ID = tables.Column()
    #IsFinished = tables.TemplateColumn(TEMPLATE)

    class Meta:
        model = Recruit_Request
        attrs = {'class':'paleblue'}
        fields = ("ID","CandidatesName","RecruitStatus","IsFinished")





