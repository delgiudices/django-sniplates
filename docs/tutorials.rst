==============================
Tutorials
==============================


Rendering bootstrap input field
===============================

In this tutorial we will create a sniplate template that renders twitter bootstrap's input field.

This is an example of a bootstrap text input.

.. code-block:: html

   <input type="text" name="some_name" class="form-control" />


Here we have a simple form with a field_name which is a CharField.

.. code-block:: python

   from django import forms
   from django.shortcuts import render

   class SomeForm(forms.Form):
       field_name = forms.CharField(max_length=25)

   def some_view(request):
       context = {
           'form' : SomeForm()
       }

       return render(request, 'template.html', context)


Django's CharField's default widget is TextInput, so let's create a template for a TextInput

`templates/widgets/bootstrap.html`

.. code-block:: django

   {% load sniplates %}
   {% block input %}
   <input type="{{ input_type }}"
       name="{{ html_name }}"
       class="form-control" />
    {% endblock %}

    {% block TextInput %}{% reuse "input" %}{% endblock %}


And finally to render it

`templates/template.html`

.. code-block:: django

   {% load sniplates %}
   {% load_widgets form="widgets/bootstrap.html" %}

   {% form_field form.field_name %}
