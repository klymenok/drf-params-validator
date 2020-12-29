# drf-params-validator

This is a simple package to validate request params on DRF viewset's actions.

## usage

* Install the package to your project

```
pip install drf-action-params-validator
```

* Use the decorator to return 400 when one of given parameter is missing

```
from drf_action_params_validator import validate_request_params

@action(detail=True, methods=[METHOD_POST])
@validate_request_params(params=['param_name_1', 'param_name_2'])
def test_action(self, request, pk):
    pass
```


## release notes

### v 0.0.1

POST data validation, default error message