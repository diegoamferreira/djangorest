# API com Django 3: Django Rest Framework

https://cursos.alura.com.br/course/api-django-3-rest-framework

## Learning the basics of Django Rest Framework

* [Python 3.9.13](https://www.python.org/)
* [Django 4.1.5](https://www.djangoproject.com/)

## How to run the project?

* clone this repository.
* Create a virtualenv with Python 3.
* Active virtualenv.
* install dependencies.
* Run migrations.

```
git clone https://github.com/diegoamferreira/djangorest.git
cd djangorest
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Django
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Django Rest Framework

[Django REST framework](https://www.django-rest-framework.org/) is a powerful and flexible toolkit for building Web
APIs.

* The Web browsable API is a huge usability win for your developers.
* Authentication policies including packages for OAuth1a and OAuth2.
* Serialization that supports both ORM and non-ORM data sources.
* Customizable all the way down - just use regular function-based views if you don't need the more powerful features.
* Extensive documentation, and great community support.
* Used and trusted by internationally recognised companies including Mozilla, Red Hat, Heroku, and Eventbrite.

## What did I learn here??

The Django Rest Framework makes it easy to create a RESTful API, with many tools that will do the work for us.
___

### Serializers

Serializers prepare the data for display in a **VIEW**, similar to an admin class. We can define the fields that will be
shown and, like in an admin class, we can use functions to help present the data.

```
class AlunoSerializer(serializers.ModelSerializer):
    """
    prepare aluno date to show as json in a view
    """
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']
```

___

### ModelViewSet

We extend this class in our view and it will provide all common methods of a REST API. We only need to provide the
queryset and the serializer_class.

```
class AlunosViewSet(viewsets.ModelViewSet):
    """
    Listing all 'alunos'.
    """
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
```

___

### DefaultRouter

A router is an object that allows for the automatic generation of URL patterns for viewsets. The router is used to route
requests to the appropriate viewset, based on the URL pattern and HTTP method.

```
router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename='Alunos')

path('', include(router.urls))
```

With this router and view above we can already access the specifics endpoits:

|          URL Style          |                HTTP Method                 |                  Action                  |       URL Name        |     |
|:---------------------------:|:------------------------------------------:|:----------------------------------------:|:---------------------:|-----|
|           alunos/           |                    GET                     |                   list                   |    {basename}-list    |     |
|           alunos/           |                    POST                    |                  create                  |                       |     |
|     alunos/{url_path}/      | GET, or as specified by `methods` argument | `@action(detail=False)` decorated method | {basename}-{url_name} |     |
|      alunos/{lookup}/       |                    GET                     |                 retrieve                 |   {basename}-detail   |     |
|      alunos/{lookup}/       |                    PUT                     |                  update                  |                       |     |
|      alunos/{lookup}/       |                   PATCH                    |              partial_update              |                       |     |
|      alunos/{lookup}/       |                   DELETE                   |                 destroy                  |                       |     |
| alunos/{lookup}/{url_path}/ | GET, or as specified by `methods` argument | `@action(detail=True)` decorated method  | {basename}-{url_name} |     |

___

### generics.ListAPIView

We can use ListAPIView to create a view that only displays a list of data. This view will only accept GET requests and
will not support any other methods. We can filter the queryset and use the **PK** from the kwargs, just like a Django
view.

```
    #VIEWS
class ListaMatriculasAluno(generics.ListAPIView):
    """
    Listando os cursos que um aluno está matriculado
    """

    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListMatriculasAlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    # URLS
    path('alunos/<int:pk>/matriculas/', ListaMatriculasAluno.as_view()),
```

In this case we are using ListAPIView to show a sub resource of a **studant**(aluno), his **courses**(cursos).
___

### Authentication Classes & Permission Classes

We can provide one or more authentication classes to a DRF view, which will define the authentication for access to a
specific endpoint. We need to specify both the authentication classes and the permission classes for each view that we
want to protect access to.

```
class AlunosViewSet(viewsets.ModelViewSet):
    """
    Exibindo todos os alunos e alunas.
    """
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
```

In the code above, we set `BasicAuthentication`, meaning that the user will need to `authenticate` with a username and
password. The `IsAuthenticated` permission class ensures that all access to that view requires authentication.
