from django.shortcuts import render
from django.views.generic import ListView, FormView
from . import models, forms

class ParserView(ListView):
    model = models.PGParser
    template_name = 'games_list.html'

    def get_queryset(self):
        return models.PGParser.objects.all()


class ParserFormView(FormView):
    template_name = 'parser_games.html'
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return render(request, 'lifehack.html', {'form': form})
        else:
            return super(ParserFormView, self).post(request, *args, **kwargs)
