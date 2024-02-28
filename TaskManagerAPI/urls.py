from django.urls import path
from .import views

urlpatterns=[
    path("", views.create_user_view, name="create_user"),
    path("login/", views.login_view, name="login"),
    path("mylogin/", views.login_template, name="mylogin"),
    path("logout/", views.logout_view, name="logout"),
    path("editprofile/<int:upk>", views.edit_profile_view, name="editprofile"),
    path("createproject/", views.create_project_view, name="createproject"),
    path("editproject/<int:ppk>", views.edit_project_view, name="editproject"),
    path("createtask/", views.create_task_view, name="createtask"),
    path("edittask/<int:tpk>", views.edit_task, name="edittask"),
    path("createuseronproject/<int:upk>/<int:ppk>", views.create_user_on_project, name="createuseronproject"),
    path("createcommentontask/<int:upk>/<int:tpk>", views.create_comment_on_task, name="createcommentontask"),
    path("getallusers/", views.get_all_users, name="getallusers"),
    path("getallprojects/", views.get_all_projects, name="getallprojects"),
    path("getallprojectsofuser/<int:upk>", views.get_all_projects_of_user, name="getallprojectsofuser"),
    path("getalltasksofproject/<int:ppk>", views.get_all_tasks_of_project, name="getalltasksofproject"),
    path("getalltasksofuser/<int:upk>", views.get_all_tasks_of_user, name="getalltasksofuser"),
    path("getallcomments/", views.get_all_comments, name="getallcomments" ),
    path("getallcommentsoftask/<int:tpk>", views.get_all_comments_of_task, name="getallcommentsoftask"),
    path("changetaskstatus/<int:tpk>", views.change_task_status, name="changetaskstatus"),
    path("deleteproject/<int:ppk>", views.delete_project, name="deleteproject"),
    path("deletetask/<int:tpk>", views.delete_task, name="deletetask"),
    path("deleteuser/<int:upk>", views.delete_user, name="deleteuser")
]