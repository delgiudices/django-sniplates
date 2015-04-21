====
Tags
====

The sniplates app consists solely of a custom template tag library.

The `load_widgets` tag
======================

.. code-block:: django

   {% load_widgets alias=template_name ... %}

This tag is used to load widget libraries from templates.  You can load more
than one library, either at a time, or in separate tags.  Because the widgets
are stored in the render context, not the context, they are available in child
templates even when defined in an inherited template.

If you pass `_soft=True` any alias that already exists will be skipped.  This
can be helpful to allow templates to ensure they have the widget sets they need
without causing duplicate loads.


The `widget` tag
================

.. code-block:: django

   {% widget 'alias:block_name' .... %}

Renders the specified widget with the current context.  You can provide extra
values to override, just like with `{% include %}`.  Currently does not support
the `only` argument.

The name is composed of the alias specified in the `load_widgets` tag, and the
name of the block in that template, joined with a ':'.


The `form_field` tag
====================

.. code-block:: django

    {% form_field form.fieldname [widget=] [alias=form] .... %}

.. note::

   This tag is compatible with the `field` tag from ``formulation``, and can
   use the same templates.

Works like the ``widget`` tag, but "explodes" useful attributes of the field
into the context.

Any extra keyword arguments you pass to the field tag will overwrite values of
the same name.

If `widget` is not specified, it will be determined from the first found of any
block matching the following patterns:

- {field}_{widget}_{name}
- {field}_{name}
- {widget}_{name}
- {field}_{widget}
- {name}
- {widget}
- {field}

These will be looked up within the alias block set "form", unless the alias
keyword is passed to override it.

Example:

Your Django View

.. code-block:: django 
   from django import forms

   class SomeForm(forms.Form):

       field_name = forms.CharField(max_length=50)

Values from ``BoundField``
--------------------------

The following values are take from the ``BoundField``:

- css_classes
- errors
- field
- form
- help_text
- html_name
- id_for_label
- label
- name
- value

Values from ``Field``
---------------------

And these from the ``Field`` itself:

- choices
- widget
- required


The `nested_widget` tag
=======================

.. code-block:: django

   {% nested_widget widgetname .... %}
       ...
   {% endnested %}

This tag is a container block that will render its contents, and pass the
output to its widget as 'content'.

An example use of this is for wrapping fields in a fieldset template:

.. code-block:: django

    {% nested_widget 'form:fieldset' caption="About You" %}
        {% form_field form.first_name %} <br>
        {% form_field form.last_name %}
    {% endnested %}


The `reuse` tag
===============

.. code-block:: django

   {% reuse blockname ... %}

Much like the `widget` tag, this re-renders an existing block tag in situ.
However, instead of looking for the block in a loaded widget library, it
searches the current template.  This allows templates extending a base to
define reusable "macro" blocks, without having to load a separate widget set.

As with other tags, you can extend the context by passing keyword arguments.

.. note:: This tag only works in templates that {% extends %} another template.

The `flatattrs` filter
=======================

.. code-block:: django

   {{ attrdict|flatarrs }}

This is simply a wrapper around :func:`django.forms.utils.flatatt`

It converts a dict of attributes into a string, in proper key="value" syntax.
The values will be escaped, but keys will not.
