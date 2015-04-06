
from django.template import TemplateSyntaxError
from django.template.loader import get_template
from django.test import SimpleTestCase, override_settings

from .forms import TestForm
from .utils import TemplateTestMixin, template_path


@override_settings(
    TEMPLATE_DIRS=[template_path('nested_tag')],
)
class TestNestedTag(TemplateTestMixin, SimpleTestCase):

    def setUp(self):
        super(TestNestedTag, self).setUp()
        self.ctx['form'] = TestForm()

    def test_invalid_noarg(self):
        with self.assertRaises(TemplateSyntaxError):
            tmpl = get_template('invalid')

    def test_invalid_twoarg(self):
        with self.assertRaises(TemplateSyntaxError):
            tmpl = get_template('invalid2')

    def test_empty_nest(self):
        tmpl = get_template('empty')
        output = tmpl.render(self.ctx)

        self.assertEqual(output, '<fieldset><caption></caption></fieldset>\n')

    def test_simple(self):
        tmpl = get_template('simple')
        output = tmpl.render(self.ctx)

        self.assertEqual(output, '<fieldset><caption>Caption</caption>content goes here</fieldset>\n')

