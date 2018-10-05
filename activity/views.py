from django.shortcuts import render, get_object_or_404 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .models import Activity 


def activity_list(request):
    object_list = Activity.published.all()
    paginator = Paginator(object_list, 3) # 3 posts in each page
    page = request.GET.get('page')
    try:
        activities = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        activities = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        activities = paginator.page(paginator.num_pages)
    return render(request,
                  'activity/list.html',
                  {'page': page,
                   'posts': activities})


def activity_detail(request, year, month, day, activity):
    activity = get_object_or_404(Activity, slug=activity,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    return render(request,
                  'activity/detail.html',
                  {'activity': activity})


class ActivityListView(ListView):
    queryset = Activity.published.all()
    context_object_name = 'activities'
    paginate_by = 3
    template_name = 'activity/list.html'