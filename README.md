# Dragos Portal Python API

A simple Python wrapper client for the Dragos portal API

(Use at your own risk, not an officially supported project)

## Usage

`dragos_portal.cfg`:
```ini
[dragos portal]
access_token = <Hex token>
access_key = <Base64 key>
```
no quotes in config

```python
import dragos_portal

# read API config from file
dragos_portal_api = dragos_portal.load_api_config("dragos_portal.cfg")

dragos_portal_api.get_intel_reports()
```

## Reference docs

https://portal.dragos.com/api/v1/doc/

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and Floyd Hightower's [Python project template](https://gitlab.com/fhightower-templates/python-project-template).
