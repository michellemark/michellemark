"""
@Copyright Michelle Mark 2018
@author Michelle Mark

Views for the main pages of the site
"""
import json
import requests
from itertools import permutations

from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from michellemark.settings.base import RECAPTCHA_PUBLIC_KEY, RECAPTCHA_PRIVATE_KEY
from .forms import ContactMeForm, PermuteForm


class ContactMeView(TemplateView):
    template_name = 'contact-me-form.html'
    form_class = ContactMeForm
    success_url = 'contact-form-thanks'

    def get_context_data(self, **kwargs):
        context = super(ContactMeView, self).get_context_data(**kwargs)
        context['page_title'] = "Contact Me"
        context['extra_css'] = []
        context['extra_javascript'] = []
        context['recaptcha_key'] = RECAPTCHA_PUBLIC_KEY

        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['form'] = self.form_class()

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['form'] = self.form_class(request.POST)

        if context['form'].is_valid():
            recaptcha_response = request.POST.get('g-recaptcha-response')

            if recaptcha_response:
                url = 'https://www.google.com/recaptcha/api/siteverify'
                recaptcha_values = {
                    'secret': RECAPTCHA_PRIVATE_KEY,
                    'response': recaptcha_response
                }
                result = requests.post(url, data=recaptcha_values)

                if result.ok:
                    response = result.json()

                    if response.get("success"):
                        context['form'].save()

                        return redirect(self.success_url)

                    else:
                        context["captcha_error"] = f"Error processing captcha: {response.get('error-codes')}"
            else:
                context["captcha_error"] = "Please check the box to tell me you are not a robot."

        return render(request, self.template_name, context)


class ContactMeThanksView(TemplateView):
    template_name = 'contact-me-thanks.html'

    def get_context_data(self, **kwargs):
        context = super(ContactMeThanksView, self).get_context_data(**kwargs)
        context['page_title'] = "Thank You"
        context['extra_css'] = []
        context['extra_javascript'] = []

        return context


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['page_title'] = "Home"
        context['extra_css'] = []
        context['extra_javascript'] = []

        return context


class PermuteView(TemplateView):
    template_name = 'permute.html'
    form_class = PermuteForm

    def get_context_data(self, **kwargs):
        context = super(PermuteView, self).get_context_data(**kwargs)
        context['page_title'] = "Permute a Value Exercise"
        context['extra_css'] = []
        context['extra_javascript'] = []

        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['form'] = self.form_class()

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['form'] = self.form_class(request.POST)

        if context['form'].is_valid():
            context['value_mutated'] = context['form'].cleaned_data.get('permute_value')
            all_mutations = list(permutations(context['value_mutated']))

            if all_mutations and len(all_mutations) > 0:
                context['all_permutations'] = []

                for mutation in all_mutations:
                    context['all_permutations'].append("".join(mutation))

        return render(request, self.template_name, context)


class ProjectsView(TemplateView):
    template_name = 'projects_main.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectsView, self).get_context_data(**kwargs)
        context['page_title'] = "A few little projects"
        context['extra_css'] = []
        context['extra_javascript'] = []

        return context


class ResumeView(TemplateView):
    template_name = 'resume.html'

    def get_context_data(self, **kwargs):
        context = super(ResumeView, self).get_context_data(**kwargs)
        context['page_title'] = "My Resume"
        context['extra_css'] = []
        context['extra_javascript'] = []

        return context


class SimpleGroceryListView(TemplateView):
    template_name = 'simple_grocery_list.html'

    def get_context_data(self, **kwargs):
        context = super(SimpleGroceryListView, self).get_context_data(**kwargs)
        context['page_title'] = "Simple Grocery List"
        context['extra_css'] = ["css/simple_grocery_list.css"]
        context['extra_javascript'] = ["js/simple_grocery_list_actions.js"]

        return context
