import hug
from falcon import HTTP_400, HTTPError
from mako.lookup import TemplateLookup
from mako.template import Template
from plim import preprocessor

import extensions
from mappings.autodiscovery.autodiscovery_mapping import FTR_AUTODISCOVERY
from mappings.rule_mappings import RULE_MAPPINGS


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
    rules = {
        id: {
            service: {
                rule: rules[rule]
                for rule, data in rules.items()
                if not tag or tag in data["tags"]
            }
            for service, rules in RULE_MAPPINGS[id].items()
        }
    }
    return components_template.get_def("table").render(id=id, data=rules, tag=tag)


@html.urls("/")
def root():
    index_template = templates.get_template("index.plim")
    return index_template.render(data=RULE_MAPPINGS)


@api
def rules():
    return RULE_MAPPINGS


@api
def workloads():
    return FTR_AUTODISCOVERY
