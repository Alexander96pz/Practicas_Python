from django.shortcuts import get_object_or_404, redirect, render
from courses.forms import CoursesForm
from courses.models import Course
from django.views import View
# Create your views here.
# modelo caracteristico de View para 
# neccesary methond name get y post 
class courses_view_list(View):
    template_name = 'courses/courses_list.html'
    queryset=Course.objects.all()

    def getqueryset(self):
        return self.queryset
        
    def get(self,request):
        context = {
            'object_list': self.getqueryset()
        }
        return render(request, self.template_name,context)
class courses_view_create(View):
    template_name='courses/courses_create.html'
    def get(self, request, *args, **kwargs):
        form=CoursesForm()
        context={
            'form': form
        }
        return render(request,self.template_name,context)

    def post(self, request, *args, **kwargs):
        form = CoursesForm(request.POST)
        if form.is_valid():
            # guarda en la BD
            form.save()
            # obtiene el formulario para presentarlo 
            form=CoursesForm()
        context = {'form': form}
        return render(request,self.template_name,context)
class courses_view_detail(View):
    template_name="courses/courses_details.html"
    def get(self, request, id, *args, **kwargs):
        try:
            obj=get_object_or_404(Course,id=id)
            context = {'object':obj}
            return render(request,self.template_name,context)
        except:    
            return render(request,'templates/nofound.html')
class CourseObjectMixin(object):
    model = Course
    def get_object(self):
        id=self.kwargs.get('id')
        obj=None
        if id is not None:
            obj = get_object_or_404(self.model,id=id)
        return obj
class courses_view_delete(CourseObjectMixin,View):
    template_name = "courses/courses_delete.html"
    # def get(self, request, id=None, *args, **kwargs):
    def get(self, request, *args, **kwargs):
        # kwargs nos ayuda a obtener los parametros de la url
        print(self.kwargs)
        obj = self.get_object()
        context ={}
        if obj is not None:
            context['object'] = obj
        return render(request,self.template_name,context)

    def post(self, request, *args, **kwargs):
        context ={}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context['object'] = obj
            return redirect('../')
        return render(request, self.template_name, context)
class courses_view_update(CourseObjectMixin,View):
    template_name = "courses/courses_update.html"
    # def get(self, request, id=None, *args, **kwargs):
    def get(self, request, *args, **kwargs):
        # kwargs nos ayuda a obtener los parametros de la url
        print(self.kwargs)
        obj = self.get_object()
        context ={}
        if obj is not None:
            form=CoursesForm(instance=obj)
            context['object'] = obj
            context['form'] = form
        return render(request,self.template_name,context)

    def post(self, request, *args, **kwargs):
        context ={}
        obj = self.get_object()
        if obj is not None:
            form=CoursesForm(request.POST,instance=obj)
            if form.is_valid():
                obj.save()
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)