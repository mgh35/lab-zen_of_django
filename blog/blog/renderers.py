from rest_framework.renderers import TemplateHTMLRenderer


class ModelTemplateHTMLRenderer(TemplateHTMLRenderer):
    exception_template_names = ["blog/%(status_code)s.html"]

    def get_template_context(self, data, renderer_context):
        return {"data": data}
