from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import CourseClass,JoinedClass
from .forms import CourseClassForm, ClassContentForm
from django.contrib import messages
from .models import ClassContent, ContentInteraction
from django.utils import timezone
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .chart import generate_time_chart
# Create your views here.

def home(request):
    return render(request,'base.html')


@login_required
def member_progress(request, studentid):
    # Generate chart and render page
    chart_image = generate_time_chart(request, studentid)
    return render(request, 'member_progress.html', {'chart_image': chart_image})
# @login_required
# def admin(request):
#     return render(request,'classControl.html')




@login_required
def create_class_view(request):
    if request.method == 'POST':
        form = CourseClassForm(request.POST, request.FILES)
        if form.is_valid():
            new_class = form.save(commit=False)
            new_class.teacher = request.user
            new_class.save()
            return redirect('listofclass')
            # Redirect to the new class's detail page
    else:
        form = CourseClassForm()
    return render(request, 'create-class.html', {'form': form})




# @login_required
# def class_detail_view(request, unique_id):
#     course_class = get_object_or_404(CourseClass, unique_id=unique_id)
#     return render(request, 'class-detail.html', {'course_class': course_class})



@login_required
def class_detail_view(request, unique_id):
    course_class = get_object_or_404(CourseClass, unique_id=unique_id)
    contents = course_class.contents.all()  # Fetch related content for the class

    if request.method == 'POST':
        form = ClassContentForm(request.POST, request.FILES)
        if form.is_valid():
            new_content = form.save(commit=False)
            new_content.course_class = course_class
            new_content.save()
            return redirect('class_detail', unique_id=unique_id)
    else:
        form = ClassContentForm()

    return render(request, 'class-detail.html', {
        'course_class': course_class,
        'contents': contents,
        'form': form,
    })


#members view only
@login_required
def class_members_view(request, unique_id):
    course_class = get_object_or_404(CourseClass, unique_id=unique_id)
    joined_users = JoinedClass.objects.filter(course_class=course_class).select_related('user')

    return render(request, 'class-members.html', {
        'course_class': course_class,
        'joined_users': joined_users,
    })

@login_required
def editclasslist(request):
    # Fetch only the classes created by the logged-in user
    user_classes = CourseClass.objects.filter(teacher=request.user)
    return render(request, 'classedit.html', {'user_classes': user_classes})


@login_required
def class_list(request): 
    classes = CourseClass.objects.all()
    # Get classes the user has joined
    joined_classes = JoinedClass.objects.filter(user=request.user).values_list('course_class_id', flat=True)
    return render(request, 'class_list.html', {
        'classes': classes, 
        'joined_classes': joined_classes
    }) 

#join the class with class
@login_required
def join_class(request, class_id):
    course_class = get_object_or_404(CourseClass, id=class_id)

    if request.method == 'POST':
        passkey = request.POST.get('passkey')
        if passkey == course_class.passkey:
            # Check if the user has already joined
            if not JoinedClass.objects.filter(user=request.user, course_class=course_class).exists():
                JoinedClass.objects.create(user=request.user, course_class=course_class)
                messages.success(request, 'You have successfully joined the class!')
            else:
                messages.info(request, 'You have already joined this class.')
            return redirect('class_content', class_id=class_id)  # Redirect to content page after joining
        else:
            messages.error(request, 'Invalid passkey. Please try again.')

    return render(request, 'join_class.html', {'course_class': course_class})


#dislpay the content to show the suer only who joined not log in
@login_required
def class_content(request, class_id):
    course_class = get_object_or_404(CourseClass, id=class_id)
    if not JoinedClass.objects.filter(user=request.user, course_class=course_class).exists():
        messages.error(request, 'You need to join this class to view its content.')
        return redirect('class_list')

    contents = course_class.contents.all()  # Assuming contents is related to CourseClass
    return render(request, 'class_content.html', {'course_class': course_class, 'contents': contents})


@require_POST
@login_required
def start_content_view(request, content_id):
    content = get_object_or_404(ClassContent, id=content_id)
    interaction, created = ContentInteraction.objects.get_or_create(
        user=request.user, content=content
    )
    if created or not interaction.start_time:
        interaction.start_time = timezone.now()
        interaction.save()
    return JsonResponse({'status': 'started'})

@require_POST
@login_required
def end_content_view(request, content_id):
    interaction = get_object_or_404(ContentInteraction, user=request.user, content_id=content_id)
    interaction.end_time = timezone.now()
    interaction.save()
    return JsonResponse({'status': 'ended', 'duration': interaction.duration()})

@require_POST
@login_required
def mark_as_read(request, content_id):
    interaction = get_object_or_404(ContentInteraction, user=request.user, content_id=content_id)
    interaction.is_marked_as_read = True
    interaction.end_time = timezone.now()  # Optionally mark end time here
    interaction.save()
    return JsonResponse({'status': 'marked_as_read'})