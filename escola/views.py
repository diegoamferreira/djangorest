from django.http import JsonResponse
from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from escola.models import Aluno, Curso, Matricula
from .serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListMatriculasAlunoSerializer, \
    ListAlunosMatriculadosCursoSerializer


def alunos(request):
    if request.method == 'GET':
        aluno = {'alunos': [
            {'id': 1, 'nome': 'Diego'},
            {'id': 2, 'nome': 'Diego'}
        ]}
        return JsonResponse(aluno)


class AlunosViewSet(viewsets.ModelViewSet):
    """
    Exibindo todos os alunos e alunas.
    """
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CursosViewSet(viewsets.ModelViewSet):
    """
    Exibindo todos os cursos.
    """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class MatriculasViewSet(viewsets.ModelViewSet):
    """
    Exibindo todos as Matriculas.
    """
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


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


class ListaAlunoMatriculasCurso(generics.ListAPIView):
    """
    Listando os alunos matriculados em um curso
    """

    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListAlunosMatriculadosCursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
