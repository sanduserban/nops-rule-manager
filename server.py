import hug
from falcon import HTTP_400, HTTPError
from mako.lookup import TemplateLookup
from mako.template import Template
from plim import preprocessor

import extensions
from mappings.autodiscovery.autodiscovery_mapping import FTR_AUTODISCOVERY
from mappings.rules import CUSTOM_RULE_MAPPINGS, AWS_CONFIG_RULE_MAPPINGS
from mappings.utils import get_full_mappings


templates = TemplateLookup(
    directories=["src"],
    module_directory=".mako_modules",
    collection_size=500,
    preprocessor=preprocessor,
)

html = hug.get(output=hug.output_format.html)
api = hug.get(prefixes=["/api"])


@html
def filter(id: hug.types.text, tag: hug.types.text = ""):
    components_template = templates.get_template("components.plim")
    full_mappings = get_full_mappings()
    filtered_rules = {
        id: {
            rule: full_mappings[id][rule]
            for rule, data in full_mappings[id].items()
            if not tag or tag in data["tags"]
        }
    }
    return components_template.get_def("table").render(id=id, data=filtered_rules, tag=tag)


@html.urls("/")
def root():
    index_template = templates.get_template("index.plim")
    return index_template.render(data=get_full_mappings())


@api
def rules():
    return {}


@api
def workloads():
    return FTR_AUTODISCOVERY
