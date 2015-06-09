#-*- coding: utf-8 -*-
__author__ = 'Alain Ivars'

from django.views import generic


class IndexView(generic.View):
    # pass
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['url'] = 'homepage'
        return context

