import traceback

from langchain.tools import StructuredTool
from langchain_core.pydantic_v1 import BaseModel
from langchain_core.pydantic_v1 import Field

from aiuda.core.globals import Globals


class SpaiderInputs(BaseModel):
    """Inputs for using spaider tool."""

    object_name: str = Field(
        description="The object/class to analyze in python. Must match the exact "
        "name/class of the variable. This will be evaluated with eval()"
    )


def spaider_function(object_name: str) -> str:

    globals = Globals.globals
    assert globals is not None, (
        "Globals must be defined before using spider, "
        "please import Globals from aiuda.core.globals and define its property to globals():"
        "\n Globals.globals = globals()"
    )

    try:
        obj = eval(object_name, globals)
        cls = obj.__class__
        try:
            annotations = str(cls.__annotations__)
        except Exception:
            annotations = ""
        doc = obj.__doc__

        result = {
            "object": object_name,
            "class": cls.__name__,
            "annotations": annotations,
            "dir": dir(obj),
            "doc": doc,
        }
        return str(result)

    except Exception:
        return f"spaider cannot extract information from {object_name}. Exception: {traceback.format_exc()}"


spaider_tool = StructuredTool.from_function(
    func=spaider_function,
    name="spaider",
    description="Obtain information about one object, such as its class, some annotations and docs. "
    "You must pass an exact name of the variable and ensure it is an object.",
)
