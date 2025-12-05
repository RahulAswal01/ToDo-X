from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apiapp.models import user_cred,todo

from django.contrib.auth.hashers import make_password,check_password

# Create your views here.

@api_view(['POST'])
def login(request,format=None):
    username = request.data['username']
    password = request.data['password']
    try:
        get_user = user_cred.objects.get(Username = username)
    except:
        return Response({'message': 'user doesnot exist'})
    # return Response({'s':'s'})
    if(check_password(password,get_user.Password)):
        return Response({"message":"Successfully login"})
    else:
        return Response({'message':'unvaild user credentials'})

@api_view(['POST'])
def create_todo_btn_all(request,format=None):
    title_input = request.data['title']
    desc_input = request.data['desc']
    status_input = 'in progress'
    obj = todo(
        title=title_input,
        desc=desc_input,
        status=status_input
    )
    obj.save()
    all = todo.objects.exclude(status__iexact = 'archived').all().values().count()
    completed = todo.objects.filter(status__iexact = 'completed').values().count()
    in_progress = todo.objects.filter(status__iexact = 'in progress').values().count()
    archived = todo.objects.filter(status__iexact = 'archived').values().count()

    stats = [
        {'label': "all", 'value': all},
        {'label': "completed", 'value': completed},
        {'label': "in progress", 'value': in_progress},
        {'label': "archived", 'value': archived}
    ]
    todo_data = todo.objects.exclude(status__iexact = 'archived').all().values('id','title','desc','status')
    return Response({'message':'success',
                     'stats' : stats,
                     'todo':todo_data}
                    )

@api_view(['POST'])
def create_todo_btn_completed(request,format=None):
    title_input = request.data['title']
    desc_input = request.data['desc']
    status_input = 'in progress'
    obj = todo(
        title=title_input,
        desc=desc_input,
        status=status_input
    )
    obj.save()
    all = todo.objects.exclude(status__iexact = 'archived').all().values().count()
    completed = todo.objects.filter(status__iexact = 'completed').values().count()
    in_progress = todo.objects.filter(status__iexact = 'in progress').values().count()
    archived = todo.objects.filter(status__iexact = 'archived').values().count()

    stats = [
        {'label': "all", 'value': all},
        {'label': "completed", 'value': completed},
        {'label': "in progress", 'value': in_progress},
        {'label': "archived", 'value': archived}
    ]
    todo_data = todo.objects.filter(status__iexact = 'completed').all().values('id','title','desc','status')
    return Response({'message':'success',
                     'stats' : stats,
                     'todo':todo_data}
                    )


@api_view(['POST'])
def create_todo_btn_in_progress(request,format=None):
    title_input = request.data['title']
    desc_input = request.data['desc']
    status_input = 'in progress'
    obj = todo(
        title=title_input,
        desc=desc_input,
        status=status_input
    )
    obj.save()
    all = todo.objects.exclude(status__iexact = 'archived').all().values().count()
    completed = todo.objects.filter(status__iexact = 'completed').values().count()
    in_progress = todo.objects.filter(status__iexact = 'in progress').values().count()
    archived = todo.objects.filter(status__iexact = 'archived').values().count()

    stats = [
        {'label': "all", 'value': all},
        {'label': "completed", 'value': completed},
        {'label': "in progress", 'value': in_progress},
        {'label': "archived", 'value': archived}
    ]
    todo_data = todo.objects.filter(status__iexact = 'in progress').all().values('id','title','desc','status')
    return Response({'message':'success',
                     'stats' : stats,
                     'todo':todo_data}
                    )

@api_view(['POST'])
def create_todo_btn_archived(request,format=None):
    title_input = request.data['title']
    desc_input = request.data['desc']
    status_input = 'in progress'
    obj = todo(
        title=title_input,
        desc=desc_input,
        status=status_input
    )
    obj.save()
    all = todo.objects.exclude(status__iexact = 'archived').all().values().count()
    completed = todo.objects.filter(status__iexact = 'completed').values().count()
    in_progress = todo.objects.filter(status__iexact = 'in progress').values().count()
    archived = todo.objects.filter(status__iexact = 'archived').values().count()

    stats = [
        {'label': "all", 'value': all},
        {'label': "completed", 'value': completed},
        {'label': "in progress", 'value': in_progress},
        {'label': "archived", 'value': archived}
    ]
    todo_data = todo.objects.filter(status__iexact = 'archived').all().values('id','title','desc','status')
    return Response({'message':'success',
                     'stats' : stats,
                     'todo':todo_data}
                    )


@api_view(['GET'])
def inital_call(request,format=None):
    all = todo.objects.exclude(status__iexact = 'archived').all().values().count()
    completed = todo.objects.filter(status__iexact = 'completed').values().count()
    in_progress = todo.objects.filter(status__iexact = 'in progress').values().count()
    archived = todo.objects.filter(status__iexact = 'archived').values().count()

    stats = [
        {'label': "all", 'value': all},
        {'label': "completed", 'value': completed},
        {'label': "in progress", 'value': in_progress},
        {'label': "archived", 'value': archived}
    ]
    todo_data = todo.objects.exclude(status__iexact = 'archived').all().values('id','title','desc','status')
    return Response([{'message':'success',
                     'stats' : stats,
                     'todo':todo_data}
                    ])


@api_view(['GET'])
def completed(request,format=None):
    all = todo.objects.exclude(status__iexact = 'archived').all().values().count()
    completed = todo.objects.filter(status__iexact = 'completed').values().count()
    in_progress = todo.objects.filter(status__iexact = 'in progress').values().count()
    archived = todo.objects.filter(status__iexact = 'archived').values().count()

    stats = [
        {'label': "all", 'value': all},
        {'label': "completed", 'value': completed},
        {'label': "in progress", 'value': in_progress},
        {'label': "archived", 'value': archived}
    ]

    completed_task = todo.objects.filter(status__iexact='completed').values('id','title','desc','status')
    return Response([{'message':'success',
                     'stats' : stats,
                     'todo':completed_task}
                    ])


@api_view(['GET'])
def in_progress(request,format=None):
    all = todo.objects.exclude(status__iexact = 'archived').all().values().count()
    completed = todo.objects.filter(status__iexact = 'completed').values().count()
    in_progress = todo.objects.filter(status__iexact = 'in progress').values().count()
    archived = todo.objects.filter(status__iexact = 'archived').values().count()

    stats = [
        {'label': "all", 'value': all},
        {'label': "completed", 'value': completed},
        {'label': "in progress", 'value': in_progress},
        {'label': "archived", 'value': archived}
    ]

    in_progress_task = todo.objects.filter(status__iexact='in progress').values('id','title','desc','status')
    return Response([{'message':'success',
                     'stats' : stats,
                     'todo':in_progress_task}
                    ])
                    

@api_view(['GET'])
def archived(request,format=None):
    all = todo.objects.exclude(status__iexact = 'archived').all().values().count()
    completed = todo.objects.filter(status__iexact = 'completed').values().count()
    in_progress = todo.objects.filter(status__iexact = 'in progress').values().count()
    archived = todo.objects.filter(status__iexact = 'archived').values().count()

    stats = [
        {'label': "all", 'value': all},
        {'label': "completed", 'value': completed},
        {'label': "in progress", 'value': in_progress},
        {'label': "archived", 'value': archived}
    ]

    archived = todo.objects.filter(status__iexact='archived').values('id','title','desc','status')
    return Response([{'message':'success',
                     'stats' : stats,
                     'todo':archived}
                    ])


@api_view(['POST'])
def completed_task(request,format=None):
    task_id = request.data['id']
    obj = todo.objects.filter(id=task_id).values().update(status = 'completed')

    all = todo.objects.exclude(status__iexact = 'archived').all().values().count()
    completed = todo.objects.filter(status__iexact = 'completed').values().count()
    in_progress = todo.objects.filter(status__iexact = 'in progress').values().count()
    archived = todo.objects.filter(status__iexact = 'archived').values().count()

    stats = [
        {'label': "all", 'value': all},
        {'label': "completed", 'value': completed},
        {'label': "in progress", 'value': in_progress},
        {'label': "archived", 'value': archived}
    ]
    todo_data = todo.objects.exclude(status__iexact = 'archived').all().values('id','title','desc','status')
    return Response([{'message':'success',
                     'stats' : stats,
                     'todo':todo_data}
                    ])


@api_view(['POST'])
def completed_task_in_progress(request,format=None):
    task_id = request.data['id']
    obj = todo.objects.filter(id=task_id).values().update(status = 'completed')

    all = todo.objects.exclude(status__iexact = 'archived').all().values().count()
    completed = todo.objects.filter(status__iexact = 'completed').values().count()
    in_progress = todo.objects.filter(status__iexact = 'in progress').values().count()
    archived = todo.objects.filter(status__iexact = 'archived').values().count()

    stats = [
        {'label': "all", 'value': all},
        {'label': "completed", 'value': completed},
        {'label': "in progress", 'value': in_progress},
        {'label': "archived", 'value': archived}
    ]
    todo_data = todo.objects.filter(status__iexact = 'in progress').all().values('id','title','desc','status')
    return Response([{'message':'success',
                     'stats' : stats,
                     'todo':todo_data}
                    ])


@api_view(['POST'])
def completed_task_archived(request,format=None):
    task_id = request.data['id']
    obj = todo.objects.filter(id=task_id).values().update(status = 'completed')

    all = todo.objects.exclude(status__iexact = 'archived').all().values().count()
    completed = todo.objects.filter(status__iexact = 'completed').values().count()
    in_progress = todo.objects.filter(status__iexact = 'in progress').values().count()
    archived = todo.objects.filter(status__iexact = 'archived').values().count()

    stats = [
        {'label': "all", 'value': all},
        {'label': "completed", 'value': completed},
        {'label': "in progress", 'value': in_progress},
        {'label': "archived", 'value': archived}
    ]
    todo_data = todo.objects.filter(status__iexact = 'archived').all().values('id','title','desc','status')
    return Response([{'message':'success',
                     'stats' : stats,
                     'todo':todo_data}
                    ])


@api_view(['POST'])
def in_progress_task(request,format=None):
    task_id = request.data['id']
    obj = todo.objects.filter(id=task_id).values().update(status = 'in progress')

    all = todo.objects.exclude(status__iexact = 'archived').all().values().count()
    completed = todo.objects.filter(status__iexact = 'completed').values().count()
    in_progress = todo.objects.filter(status__iexact = 'in progress').values().count()
    archived = todo.objects.filter(status__iexact = 'archived').values().count()

    stats = [
        {'label': "all", 'value': all},
        {'label': "completed", 'value': completed},
        {'label': "in progress", 'value': in_progress},
        {'label': "archived", 'value': archived}
    ]
    todo_data = todo.objects.exclude(status__iexact = 'archived').all().values('id','title','desc','status')
    return Response([{'message':'success',
                     'stats' : stats,
                     'todo':todo_data}
                    ])


@api_view(['POST'])
def in_progress_task_completed(request,format=None):
    task_id = request.data['id']
    obj = todo.objects.filter(id=task_id).values().update(status = 'in progress')

    all = todo.objects.exclude(status__iexact = 'archived').all().values().count()
    completed = todo.objects.filter(status__iexact = 'completed').values().count()
    in_progress = todo.objects.filter(status__iexact = 'in progress').values().count()
    archived = todo.objects.filter(status__iexact = 'archived').values().count()

    stats = [
        {'label': "all", 'value': all},
        {'label': "completed", 'value': completed},
        {'label': "in progress", 'value': in_progress},
        {'label': "archived", 'value': archived}
    ]
    todo_data = todo.objects.filter(status__iexact = 'completed').all().values('id','title','desc','status')
    return Response([{'message':'success',
                     'stats' : stats,
                     'todo':todo_data}
                    ])


@api_view(['POST'])
def archived_task_non_archived(request,format=None):
    task_id = request.data['id']
    obj = todo.objects.filter(id=task_id).values().update(status = 'archived')

    all = todo.objects.exclude(status__iexact = 'archived').all().values().count()
    completed = todo.objects.filter(status__iexact = 'completed').values().count()
    in_progress = todo.objects.filter(status__iexact = 'in progress').values().count()
    archived = todo.objects.filter(status__iexact = 'archived').values().count()

    stats = [
        {'label': "all", 'value': all},
        {'label': "completed", 'value': completed},
        {'label': "in progress", 'value': in_progress},
        {'label': "archived", 'value': archived}
    ]
    todo_data = todo.objects.exclude(status__iexact = 'archived').all().values('id','title','desc','status')
    return Response([{'message':'success',
                     'stats' : stats,
                     'todo':todo_data}
                    ])


@api_view(['POST'])
def archived_task_completed(request,format=None):
    task_id = request.data['id']
    obj = todo.objects.filter(id=task_id).values().update(status = 'archived')

    all = todo.objects.exclude(status__iexact = 'archived').all().values().count()
    completed = todo.objects.filter(status__iexact = 'completed').values().count()
    in_progress = todo.objects.filter(status__iexact = 'in progress').values().count()
    archived = todo.objects.filter(status__iexact = 'archived').values().count()

    stats = [
        {'label': "all", 'value': all},
        {'label': "completed", 'value': completed},
        {'label': "in progress", 'value': in_progress},
        {'label': "archived", 'value': archived}
    ]
    todo_data = todo.objects.filter(status__iexact = 'completed').all().values('id','title','desc','status')
    return Response([{'message':'success',
                     'stats' : stats,
                     'todo':todo_data}
                    ])

@api_view(['POST'])
def archived_task_all(request,format=None):
    task_id = request.data['id']
    obj = todo.objects.filter(id=task_id).values().update(status = 'archived')

    all = todo.objects.exclude(status__iexact = 'archived').all().values().count()
    completed = todo.objects.filter(status__iexact = 'completed').values().count()
    in_progress = todo.objects.filter(status__iexact = 'in progress').values().count()
    archived = todo.objects.filter(status__iexact = 'archived').values().count()

    stats = [
        {'label': "all", 'value': all},
        {'label': "completed", 'value': completed},
        {'label': "in progress", 'value': in_progress},
        {'label': "archived", 'value': archived}
    ]
    todo_data = todo.objects.exclude(status__iexact = 'archived').all().values('id','title','desc','status')
    return Response([{'message':'success',
                     'stats' : stats,
                     'todo':todo_data}
                    ])


@api_view(['POST'])
def archived_task_in_progress(request,format=None):
    task_id = request.data['id']
    obj = todo.objects.filter(id=task_id).values().update(status = 'archived')

    all = todo.objects.exclude(status__iexact = 'archived').all().values().count()
    completed = todo.objects.filter(status__iexact = 'completed').values().count()
    in_progress = todo.objects.filter(status__iexact = 'in progress').values().count()
    archived = todo.objects.filter(status__iexact = 'archived').values().count()

    stats = [
        {'label': "all", 'value': all},
        {'label': "completed", 'value': completed},
        {'label': "in progress", 'value': in_progress},
        {'label': "archived", 'value': archived}
    ]
    todo_data = todo.objects.filter(status__iexact = 'in progress').all().values('id','title','desc','status')
    return Response([{'message':'success',
                     'stats' : stats,
                     'todo':todo_data}
                    ])

@api_view(['POST'])      
def archived_task_archived(request,format=None):
    task_id = request.data['id']
    obj = todo.objects.filter(id=task_id).values().update(status = 'in progress')

    all = todo.objects.exclude(status__iexact = 'archived').all().values().count()
    completed = todo.objects.filter(status__iexact = 'completed').values().count()
    in_progress = todo.objects.filter(status__iexact = 'in progress').values().count()
    archived = todo.objects.filter(status__iexact = 'archived').values().count()

    stats = [
        {'label': "all", 'value': all},
        {'label': "completed", 'value': completed},
        {'label': "in progress", 'value': in_progress},
        {'label': "archived", 'value': archived}
    ]
    todo_data = todo.objects.filter(status__iexact = 'archived').all().values('id','title','desc','status')
    return Response([{'message':'success',
                     'stats' : stats,
                     'todo':todo_data}
                    ])

@api_view(['DELETE'])
def delete_task_non_archived(request,format=None):
    task_id = request.data['id']
    obj = todo.objects.filter(id=task_id).delete()

    all = todo.objects.exclude(status__iexact = 'archived').all().values().count()
    completed = todo.objects.filter(status__iexact = 'completed').values().count()
    in_progress = todo.objects.filter(status__iexact = 'in progress').values().count()
    archived = todo.objects.filter(status__iexact = 'archived').values().count()

    stats = [
        {'label': "all", 'value': all},
        {'label': "completed", 'value': completed},
        {'label': "in progress", 'value': in_progress},
        {'label': "archived", 'value': archived}
    ]
    todo_data = todo.objects.exclude(status__iexact = 'archived').all().values('id','title','desc','status')
    return Response([{'message':'success',
                     'stats' : stats,
                     'todo':todo_data}
                    ])


@api_view(['DELETE'])
def delete_task_in_progress(request,format=None):
    task_id = request.data['id']
    obj = todo.objects.filter(id=task_id).delete()

    all = todo.objects.exclude(status__iexact = 'archived').all().values().count()
    completed = todo.objects.filter(status__iexact = 'completed').values().count()
    in_progress = todo.objects.filter(status__iexact = 'in progress').values().count()
    archived = todo.objects.filter(status__iexact = 'archived').values().count()

    stats = [
        {'label': "all", 'value': all},
        {'label': "completed", 'value': completed},
        {'label': "in progress", 'value': in_progress},
        {'label': "archived", 'value': archived}
    ]
    todo_data = todo.objects.filter(status__iexact = 'in progress').all().values('id','title','desc','status')
    return Response([{'message':'success',
                     'stats' : stats,
                     'todo':todo_data}
                    ])


@api_view(['DELETE'])
def delete_task_all(request,format=None):
    task_id = request.data['id']
    obj = todo.objects.filter(id=task_id).delete()

    all = todo.objects.exclude(status__iexact = 'archived').all().values().count()
    completed = todo.objects.filter(status__iexact = 'completed').values().count()
    in_progress = todo.objects.filter(status__iexact = 'in progress').values().count()
    archived = todo.objects.filter(status__iexact = 'archived').values().count()

    stats = [
        {'label': "all", 'value': all},
        {'label': "completed", 'value': completed},
        {'label': "in progress", 'value': in_progress},
        {'label': "archived", 'value': archived}
    ]
    todo_data = todo.objects.exclude(status__iexact = 'archived').all().values('id','title','desc','status')
    return Response([{'message':'success',
                     'stats' : stats,
                     'todo':todo_data}
                    ])


@api_view(['DELETE'])
def delete_task_archived(request,format=None):
    task_id = request.data['id']
    obj = todo.objects.filter(id=task_id).delete()

    all = todo.objects.exclude(status__iexact = 'archived').all().values().count()
    completed = todo.objects.filter(status__iexact = 'completed').values().count()
    in_progress = todo.objects.filter(status__iexact = 'in progress').values().count()
    archived = todo.objects.filter(status__iexact = 'archived').values().count()

    stats = [
        {'label': "all", 'value': all},
        {'label': "completed", 'value': completed},
        {'label': "in progress", 'value': in_progress},
        {'label': "archived", 'value': archived}
    ]
    todo_data = todo.objects.filter(status__iexact = 'archived').all().values('id','title','desc','status')
    return Response([{'message':'success',
                     'stats' : stats,
                     'todo':todo_data}
                    ])


@api_view(['DELETE'])
def delete_task_completed(request,format=None):
    task_id = request.data['id']
    obj = todo.objects.filter(id=task_id).delete()

    all = todo.objects.exclude(status__iexact = 'archived').all().values().count()
    completed = todo.objects.filter(status__iexact = 'completed').values().count()
    in_progress = todo.objects.filter(status__iexact = 'in progress').values().count()
    archived = todo.objects.filter(status__iexact = 'archived').values().count()

    stats = [
        {'label': "all", 'value': all},
        {'label': "completed", 'value': completed},
        {'label': "in progress", 'value': in_progress},
        {'label': "archived", 'value': archived}
    ]
    todo_data = todo.objects.filter(status__iexact = 'completed').all().values('id','title','desc','status')
    return Response([{'message':'success',
                     'stats' : stats,
                     'todo':todo_data}
                    ])

                    


@api_view(['PUT'])
def update_task_all(request,format=None):
    task_id = request.data['id']
    task_title = request.data['title']
    task_desc = request.data['desc']

    obj = todo.objects.filter(id=task_id).values().update(title=task_title,desc=task_desc)
    all = todo.objects.all().values().count() 
    completed = todo.objects.filter(status__iexact = 'completed').values().count()
    in_progress = todo.objects.filter(status__iexact = 'in progress').values().count()
    archived = todo.objects.filter(status__iexact = 'archived').values().count()

    stats = [
        {'label': "all", 'value': all},
        {'label': "completed", 'value': completed},
        {'label': "in progress", 'value': in_progress},
        {'label': "archived", 'value': archived}
    ]
    todo_data = todo.objects.exclude(status__iexact = 'archived').all().values('id','title','desc','status')
    return Response([{'message':'success',
                     'stats' : stats,
                     'todo':todo_data}
                    ])

@api_view(['PUT'])
def update_task_completed(request,format=None):
    task_id = request.data['id']
    task_title = request.data['title']
    task_desc = request.data['desc']

    obj = todo.objects.filter(id=task_id).values().update(title=task_title,desc=task_desc)
    all = todo.objects.all().values().count() 
    completed = todo.objects.filter(status__iexact = 'completed').values().count()
    in_progress = todo.objects.filter(status__iexact = 'in progress').values().count()
    archived = todo.objects.filter(status__iexact = 'archived').values().count()

    stats = [
        {'label': "all", 'value': all},
        {'label': "completed", 'value': completed},
        {'label': "in progress", 'value': in_progress},
        {'label': "archived", 'value': archived}
    ]
    todo_data = todo.objects.filter(status__iexact = 'completed').all().values('id','title','desc','status')
    return Response([{'message':'success',
                     'stats' : stats,
                     'todo':todo_data}
                    ])

@api_view(['PUT'])
def update_task_in_progress(request,format=None):
    task_id = request.data['id']
    task_title = request.data['title']
    task_desc = request.data['desc']

    obj = todo.objects.filter(id=task_id).values().update(title=task_title,desc=task_desc)
    all = todo.objects.all().values().count() 
    completed = todo.objects.filter(status__iexact = 'completed').values().count()
    in_progress = todo.objects.filter(status__iexact = 'in progress').values().count()
    archived = todo.objects.filter(status__iexact = 'archived').values().count()

    stats = [
        {'label': "all", 'value': all},
        {'label': "completed", 'value': completed},
        {'label': "in progress", 'value': in_progress},
        {'label': "archived", 'value': archived}
    ]
    todo_data = todo.objects.filter(status__iexact = 'in progress').all().values('id','title','desc','status')
    return Response([{'message':'success',
                     'stats' : stats,
                     'todo':todo_data}
                    ])

@api_view(['PUT'])
def update_task_archived(request,format=None):
    task_id = request.data['id']
    task_title = request.data['title']
    task_desc = request.data['desc']

    obj = todo.objects.filter(id=task_id).values().update(title=task_title,desc=task_desc)
    all = todo.objects.all().values().count() 
    completed = todo.objects.filter(status__iexact = 'completed').values().count()
    in_progress = todo.objects.filter(status__iexact = 'in progress').values().count()
    archived = todo.objects.filter(status__iexact = 'archived').values().count()

    stats = [
        {'label': "all", 'value': all},
        {'label': "completed", 'value': completed},
        {'label': "in progress", 'value': in_progress},
        {'label': "archived", 'value': archived}
    ]
    todo_data = todo.objects.filter(status__iexact = 'archived').all().values('id','title','desc','status')
    return Response([{'message':'success',
                     'stats' : stats,
                     'todo':todo_data}
                    ])



# code for create user

# @api_view(['POST'])
# def create_user(request,format=None):
#     username = request.data['username']
#     password = request.data['password']
#     if not username or not password:
#         return Response({'error': 'username and password are required'}, status=400)
#     enc_passcode = make_password(password)
#     obj = user_cred (Username = username,
#                     Password = enc_passcode)
#     obj.save()
#     return Response({'Message':'user created'})
   