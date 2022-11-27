
from django.shortcuts import render
from django.views import View
from datetime import date, datetime
from dashboard.models import CONTACTED, PENDING, UNSEEN, ApplyForThisPosition, Blog, BlogCategory, CurrentOpportunities, LetsTalk, Subscribe, TeamMembers
from utils.datetime_utils import DateOperationMixin
from django.db.models import Count


class DashboardView(View, DateOperationMixin):
   
    @staticmethod
    def get_context(request, start, end):
        let_talk = LetsTalk.objects.filter(created_at__date__range=[start, end]).values('status').annotate(count=Count('status'))
        
        for item in let_talk:
            if item['status'] == PENDING:
                pending = item['count']
            else:
                pending = 0
            if item['status'] == CONTACTED:
               contacted = item['count']
            else:
                contacted = 0
        application = ApplyForThisPosition.objects.values('status').annotate(count = Count('status'))
        unseen = 0
        seen = 0
        pendings = 0
        selected = 0
        rejected = 0
        for item in application:
            if item['status'] == 1:
                unseen = item['count']
            if item['status'] == 2:
                seen = item['count']
            if item['status'] == 3:
                pendings = item['count']
            if item['status'] == 4:
                selected = item['count']
            if item['status'] == 5:
                rejected = item['count']
      
        context = {
            "pending": pending,
            "contacted": contacted,
            "total_blog": Blog.objects.all().count(),
            "total_subscribe":  Subscribe.objects.all().count(),
            "total_teammembers": TeamMembers.objects.all().count(),
            "total_blog_category": BlogCategory.objects.all().count(),
            "total_opportunities": CurrentOpportunities.objects.all().count(),
            "unseen": unseen,
            "seen": seen,
            "pendings": pendings,
            "selected": selected,
            "rejected": rejected

        }
        return context
    def get(self, request):
        data = request.GET
        today = date.today().strftime("%Y-%m-%d")
        date_range = data.get('selected_range')
        if date_range:
            if date_range == 'last_seven_days':
                data = self.get_context(request,self.last_seven_days(), today)
            if date_range == 'last_fifteen_days':
                data = self.get_context(request,self.last_fifteen_days(), today)
            if date_range == 'last_thirty_days':
                data = self.get_context(request,self.last_thirty_days(), today)
            if date_range == 'last_six_months':
                print(self.six_month_previous_date())
                data = self.get_context(request,self.six_month_previous_date(), today)
            if date_range == 'last_year':
                data = self.get_context(request,self.last_year(), today)
        else:
            data = self.get_context(request,self.last_thirty_days(), today)
            

        return render(request, 'dashboard.html',data)