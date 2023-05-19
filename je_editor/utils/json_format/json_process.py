import json.decoder
import sys
from json import dumps
from json import loads

from je_editor.utils.exception.exception_tags import cant_reformat_json_error
from je_editor.utils.exception.exception_tags import wrong_json_data_error
from je_editor.utils.exception.exceptions import JEditorJsonException


def __process_json(json_string: str, **kwargs):
    try:
        return dumps(loads(json_string), indent=4, sort_keys=True, **kwargs)
    except json.JSONDecodeError as error:
        print(wrong_json_data_error, file=sys.stderr)
        raise error
    except TypeError:
        try:
            return dumps(json_string, indent=4, sort_keys=True, **kwargs)
        except TypeError:
            raise JEditorJsonException(wrong_json_data_error)


def reformat_json(json_string: str, **kwargs):
    # Make json pretty
    try:
        return __process_json(json_string, **kwargs)
    except JEditorJsonException:
        raise JEditorJsonException(cant_reformat_json_error)
