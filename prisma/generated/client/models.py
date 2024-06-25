# -*- coding: utf-8 -*-
# code generated by Prisma. DO NOT EDIT.
# pyright: reportUnusedImport=false
# fmt: off

# global imports for type checking
from builtins import bool as _bool
from builtins import int as _int
from builtins import float as _float
from builtins import str as _str
import sys
import decimal
import datetime
from typing import (
    TYPE_CHECKING,
    Optional,
    Iterable,
    Iterator,
    Sequence,
    Callable,
    ClassVar,
    NoReturn,
    TypeVar,
    Generic,
    Mapping,
    Tuple,
    Union,
    List,
    Dict,
    Type,
    Any,
    Set,
    overload,
    cast,
)
from typing_extensions import TypedDict, Literal


LiteralString = str
# -- template models.py.jinja --
import os
import logging
import inspect
import warnings
from collections import OrderedDict

from pydantic import BaseModel, Field

from . import types, enums, errors, fields, bases
from ._types import FuncType
from ._compat import model_rebuild, field_validator
from ._builder import serialize_base64
from .generator import partial_models_ctx, PartialModelField


log: logging.Logger = logging.getLogger(__name__)
_created_partial_types: Set[str] = set()

class User(bases.BaseUser):
    """Represents a User record"""

    id: _str
    bouquets: Optional[List['models.SavedBouquet']] = None

    # take *args and **kwargs so that other metaclasses can define arguments
    def __init_subclass__(
        cls,
        *args: Any,
        warn_subclass: Optional[bool] = None,
        **kwargs: Any,
    ) -> None:
        super().__init_subclass__()
        if warn_subclass is not None:
            warnings.warn(
                'The `warn_subclass` argument is deprecated as it is no longer necessary and will be removed in the next release',
                DeprecationWarning,
                stacklevel=3,
            )


    @staticmethod
    def create_partial(
        name: str,
        include: Optional[Iterable['types.UserKeys']] = None,
        exclude: Optional[Iterable['types.UserKeys']] = None,
        required: Optional[Iterable['types.UserKeys']] = None,
        optional: Optional[Iterable['types.UserKeys']] = None,
        relations: Optional[Mapping['types.UserRelationalFieldKeys', str]] = None,
        exclude_relational_fields: bool = False,
    ) -> None:
        if not os.environ.get('PRISMA_GENERATOR_INVOCATION'):
            raise RuntimeError(
                'Attempted to create a partial type outside of client generation.'
            )

        if name in _created_partial_types:
            raise ValueError(f'Partial type "{name}" has already been created.')

        if include is not None:
            if exclude is not None:
                raise TypeError('Exclude and include are mutually exclusive.')
            if exclude_relational_fields is True:
                raise TypeError('Include and exclude_relational_fields=True are mutually exclusive.')

        if required and optional:
            shared = set(required) & set(optional)
            if shared:
                raise ValueError(f'Cannot make the same field(s) required and optional {shared}')

        if exclude_relational_fields and relations:
            raise ValueError(
                'exclude_relational_fields and relations are mutually exclusive'
            )

        fields: Dict['types.UserKeys', PartialModelField] = OrderedDict()

        try:
            if include:
                for field in include:
                    fields[field] = _User_fields[field].copy()
            elif exclude:
                for field in exclude:
                    if field not in _User_fields:
                        raise KeyError(field)

                fields = {
                    key: data.copy()
                    for key, data in _User_fields.items()
                    if key not in exclude
                }
            else:
                fields = {
                    key: data.copy()
                    for key, data in _User_fields.items()
                }

            if required:
                for field in required:
                    fields[field]['optional'] = False

            if optional:
                for field in optional:
                    fields[field]['optional'] = True

            if exclude_relational_fields:
                fields = {
                    key: data
                    for key, data in fields.items()
                    if key not in _User_relational_fields
                }

            if relations:
                for field, type_ in relations.items():
                    if field not in _User_relational_fields:
                        raise errors.UnknownRelationalFieldError('User', field)

                    # TODO: this method of validating types is not ideal
                    # as it means we cannot two create partial types that
                    # reference each other
                    if type_ not in _created_partial_types:
                        raise ValueError(
                            f'Unknown partial type: "{type_}". '
                            f'Did you remember to generate the {type_} type before this one?'
                        )

                    # TODO: support non prisma.partials models
                    info = fields[field]
                    if info['is_list']:
                        info['type'] = f'List[\'partials.{type_}\']'
                    else:
                        info['type'] = f'\'partials.{type_}\''
        except KeyError as exc:
            raise ValueError(
                f'{exc.args[0]} is not a valid User / {name} field.'
            ) from None

        models = partial_models_ctx.get()
        models.append(
            {
                'name': name,
                'fields': cast(Mapping[str, PartialModelField], fields),
                'from_model': 'User',
            }
        )
        _created_partial_types.add(name)


class SavedBouquet(bases.BaseSavedBouquet):
    """Represents a SavedBouquet record"""

    id: _int
    bouquet: _str
    userId: _str
    user: Optional['models.User'] = None

    # take *args and **kwargs so that other metaclasses can define arguments
    def __init_subclass__(
        cls,
        *args: Any,
        warn_subclass: Optional[bool] = None,
        **kwargs: Any,
    ) -> None:
        super().__init_subclass__()
        if warn_subclass is not None:
            warnings.warn(
                'The `warn_subclass` argument is deprecated as it is no longer necessary and will be removed in the next release',
                DeprecationWarning,
                stacklevel=3,
            )


    @staticmethod
    def create_partial(
        name: str,
        include: Optional[Iterable['types.SavedBouquetKeys']] = None,
        exclude: Optional[Iterable['types.SavedBouquetKeys']] = None,
        required: Optional[Iterable['types.SavedBouquetKeys']] = None,
        optional: Optional[Iterable['types.SavedBouquetKeys']] = None,
        relations: Optional[Mapping['types.SavedBouquetRelationalFieldKeys', str]] = None,
        exclude_relational_fields: bool = False,
    ) -> None:
        if not os.environ.get('PRISMA_GENERATOR_INVOCATION'):
            raise RuntimeError(
                'Attempted to create a partial type outside of client generation.'
            )

        if name in _created_partial_types:
            raise ValueError(f'Partial type "{name}" has already been created.')

        if include is not None:
            if exclude is not None:
                raise TypeError('Exclude and include are mutually exclusive.')
            if exclude_relational_fields is True:
                raise TypeError('Include and exclude_relational_fields=True are mutually exclusive.')

        if required and optional:
            shared = set(required) & set(optional)
            if shared:
                raise ValueError(f'Cannot make the same field(s) required and optional {shared}')

        if exclude_relational_fields and relations:
            raise ValueError(
                'exclude_relational_fields and relations are mutually exclusive'
            )

        fields: Dict['types.SavedBouquetKeys', PartialModelField] = OrderedDict()

        try:
            if include:
                for field in include:
                    fields[field] = _SavedBouquet_fields[field].copy()
            elif exclude:
                for field in exclude:
                    if field not in _SavedBouquet_fields:
                        raise KeyError(field)

                fields = {
                    key: data.copy()
                    for key, data in _SavedBouquet_fields.items()
                    if key not in exclude
                }
            else:
                fields = {
                    key: data.copy()
                    for key, data in _SavedBouquet_fields.items()
                }

            if required:
                for field in required:
                    fields[field]['optional'] = False

            if optional:
                for field in optional:
                    fields[field]['optional'] = True

            if exclude_relational_fields:
                fields = {
                    key: data
                    for key, data in fields.items()
                    if key not in _SavedBouquet_relational_fields
                }

            if relations:
                for field, type_ in relations.items():
                    if field not in _SavedBouquet_relational_fields:
                        raise errors.UnknownRelationalFieldError('SavedBouquet', field)

                    # TODO: this method of validating types is not ideal
                    # as it means we cannot two create partial types that
                    # reference each other
                    if type_ not in _created_partial_types:
                        raise ValueError(
                            f'Unknown partial type: "{type_}". '
                            f'Did you remember to generate the {type_} type before this one?'
                        )

                    # TODO: support non prisma.partials models
                    info = fields[field]
                    if info['is_list']:
                        info['type'] = f'List[\'partials.{type_}\']'
                    else:
                        info['type'] = f'\'partials.{type_}\''
        except KeyError as exc:
            raise ValueError(
                f'{exc.args[0]} is not a valid SavedBouquet / {name} field.'
            ) from None

        models = partial_models_ctx.get()
        models.append(
            {
                'name': name,
                'fields': cast(Mapping[str, PartialModelField], fields),
                'from_model': 'SavedBouquet',
            }
        )
        _created_partial_types.add(name)



_User_relational_fields: Set[str] = {
        'bouquets',
    }
_User_fields: Dict['types.UserKeys', PartialModelField] = OrderedDict(
    [
        ('id', {
            'name': 'id',
            'is_list': False,
            'optional': False,
            'type': '_str',
            'is_relational': False,
            'documentation': None,
        }),
        ('bouquets', {
            'name': 'bouquets',
            'is_list': True,
            'optional': True,
            'type': 'List[\'models.SavedBouquet\']',
            'is_relational': True,
            'documentation': None,
        }),
    ],
)

_SavedBouquet_relational_fields: Set[str] = {
        'user',
    }
_SavedBouquet_fields: Dict['types.SavedBouquetKeys', PartialModelField] = OrderedDict(
    [
        ('id', {
            'name': 'id',
            'is_list': False,
            'optional': False,
            'type': '_int',
            'is_relational': False,
            'documentation': None,
        }),
        ('bouquet', {
            'name': 'bouquet',
            'is_list': False,
            'optional': False,
            'type': '_str',
            'is_relational': False,
            'documentation': None,
        }),
        ('userId', {
            'name': 'userId',
            'is_list': False,
            'optional': False,
            'type': '_str',
            'is_relational': False,
            'documentation': None,
        }),
        ('user', {
            'name': 'user',
            'is_list': False,
            'optional': True,
            'type': 'models.User',
            'is_relational': True,
            'documentation': None,
        }),
    ],
)



# we have to import ourselves as relation types are namespaced to models
# e.g. models.Post
from . import models, actions

# required to support relationships between models
model_rebuild(User)
model_rebuild(SavedBouquet)
