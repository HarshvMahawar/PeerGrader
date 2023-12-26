# views.py

from django.shortcuts import render, redirect
from .models import Assignment, Rubric
from .forms import AssignmentForm

# peer_grading_app/views.py

from django.shortcuts import render, redirect



# peer_grading_app/views.py

from django.shortcuts import render, redirect
from .models import Assignment, Rubric


# peer_grading_app/views.py

from django.shortcuts import render, redirect
from .models import Assignment, Rubric

def create_rubrics(request, assignment_id):
    assignment = Assignment.objects.get(id=assignment_id)

    if request.method == 'POST':
        # Get the submitted values for existing questions
        existing_questions = [key.replace('question_number_', '') for key in request.POST.keys() if key.startswith('question_number_')]

        for existing_question in existing_questions:
            question_number = existing_question
            max_marks = request.POST.get('max_marks_' + question_number)

            # Create a rubric for the assignment
            rubric = Rubric.objects.create(assignment=assignment, question_number=question_number, max_marks=max_marks)

        # Get the submitted values for dynamically added questions
        new_question_number = request.POST.get('new_question_number')
        new_max_marks = request.POST.get('new_max_marks')

        # Create a rubric for the assignment with the new question
        if new_question_number and new_max_marks:
            rubric = Rubric.objects.create(assignment=assignment, question_number=new_question_number, max_marks=new_max_marks)

        # Redirect to instructor_home after submitting the form
        return redirect('instructor_home')

    rubrics = Rubric.objects.filter(assignment=assignment)

    return render(request, 'create_rubrics.html', {'assignment': assignment, 'rubrics': rubrics})




def create_assignment(request):
    new_assignment = None
    if request.method == 'POST':
        # Process the form data directly from request.POST
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')

        # Validate and save the data as needed
        # For simplicity, let's assume direct saving to the Assignment model
        # You might want to add more validation and error handling in a real-world scenario
        new_assignment = Assignment.objects.create(
            title=title,
            description=description,
            due_date=due_date,
            # Add other fields as needed
        )

        # Redirect to create_rubrics after assignment creation
        return redirect('create_rubrics', assignment_id=new_assignment.id)
    else:
        # No form is needed if you are not using Django forms
        pass

    return render(request, 'create_assignment.html', {'new_assignment': new_assignment})




def instructor_view(request, assignment_id):
    assignment = Assignment.objects.get(id=assignment_id)
    questions = Question.objects.filter(assignment=assignment)
    rubrics = Rubric.objects.filter(question__in=questions)

    return render(request, 'instructor_view.html', {'assignment': assignment, 'questions': questions, 'rubrics': rubrics})


def instructor_home_view(request):
    return render(request, 'instructor_home.html')



