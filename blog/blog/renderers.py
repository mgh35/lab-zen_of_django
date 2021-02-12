from rest_framework.renderers import TemplateHTMLRenderer


class ModelTemplateHTMLRenderer(TemplateHTMLRenderer):
    def get_template_context(self, data, renderer_context):
        return {"data": data}
