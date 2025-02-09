from django.views.generic import ListView, DetailView
from .models import Member

class MemberListView(ListView):
    model = Member
    template_name = 'member/member_list.html'
    context_object_name = 'members'

    def get_queryset(self):
        # 表示設定が有効な部員のみを取得
        return Member.objects.filter(is_active=True)

class MemberDetailView(DetailView):
    model = Member
    template_name = 'member/member_detail.html'
    context_object_name = 'member'

    def get_queryset(self):
        # 表示設定が有効な部員のみを取得
        return Member.objects.filter(is_active=True)