# Stubs for tornado_py3.web (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import datetime
import http.cookies
import tornado_py3.locale
from tornado_py3 import httputil, iostream, template
from tornado_py3.concurrent import Future
from tornado_py3.httpserver import HTTPServer
from tornado_py3.routing import ReversibleRouter, ReversibleRuleRouter, Rule, URLSpec, _RuleList
from types import TracebackType
from typing import Any, Awaitable, Callable, Dict, Generator, Iterable, List, Optional, Tuple, Type, Union

url = URLSpec
MIN_SUPPORTED_SIGNED_VALUE_VERSION: int
MAX_SUPPORTED_SIGNED_VALUE_VERSION: int
DEFAULT_SIGNED_VALUE_VERSION: int
DEFAULT_SIGNED_VALUE_MIN_VERSION: int

class _ArgDefaultMarker: ...

class RequestHandler:
    SUPPORTED_METHODS: Any = ...
    path_args: List[str] = ...
    path_kwargs: Dict[str, str] = ...
    application: Any = ...
    request: Any = ...
    ui: Any = ...
    def __init__(self, application: Application, request: httputil.HTTPServerRequest, **kwargs: Any) -> None: ...
    initialize: Callable[..., None] = ...
    @property
    def settings(self) -> Dict[str, Any]: ...
    head: Callable[..., Optional[Awaitable[None]]] = ...
    get: Callable[..., Optional[Awaitable[None]]] = ...
    post: Callable[..., Optional[Awaitable[None]]] = ...
    delete: Callable[..., Optional[Awaitable[None]]] = ...
    patch: Callable[..., Optional[Awaitable[None]]] = ...
    put: Callable[..., Optional[Awaitable[None]]] = ...
    options: Callable[..., Optional[Awaitable[None]]] = ...
    def prepare(self) -> Optional[Awaitable[None]]: ...
    def on_finish(self) -> None: ...
    def on_connection_close(self) -> None: ...
    def clear(self) -> None: ...
    def set_default_headers(self) -> None: ...
    def set_status(self, status_code: int, reason: Optional[str]=...) -> None: ...
    def get_status(self) -> int: ...
    def set_header(self, name: str, value: _HeaderTypes) -> None: ...
    def add_header(self, name: str, value: _HeaderTypes) -> None: ...
    def clear_header(self, name: str) -> None: ...
    def get_argument(self, name: str, default: str, strip: bool=...) -> str: ...
    def get_argument(self, name: str, default: _ArgDefaultMarker=..., strip: bool=...) -> str: ...
    def get_argument(self, name: str, default: None, strip: bool=...) -> Optional[str]: ...
    def get_argument(self, name: str, default: Union[None, str, _ArgDefaultMarker]=..., strip: bool=...) -> Optional[str]: ...
    def get_arguments(self, name: str, strip: bool=...) -> List[str]: ...
    def get_body_argument(self, name: str, default: Union[None, str, _ArgDefaultMarker]=..., strip: bool=...) -> Optional[str]: ...
    def get_body_arguments(self, name: str, strip: bool=...) -> List[str]: ...
    def get_query_argument(self, name: str, default: Union[None, str, _ArgDefaultMarker]=..., strip: bool=...) -> Optional[str]: ...
    def get_query_arguments(self, name: str, strip: bool=...) -> List[str]: ...
    def decode_argument(self, value: bytes, name: Optional[str]=...) -> str: ...
    @property
    def cookies(self) -> Dict[str, http.cookies.Morsel]: ...
    def get_cookie(self, name: str, default: Optional[str]=...) -> Optional[str]: ...
    def set_cookie(self, name: str, value: Union[str, bytes], domain: Optional[str]=..., expires: Optional[Union[float, Tuple, datetime.datetime]]=..., path: str=..., expires_days: Optional[int]=..., **kwargs: Any) -> None: ...
    def clear_cookie(self, name: str, path: str=..., domain: Optional[str]=...) -> None: ...
    def clear_all_cookies(self, path: str=..., domain: Optional[str]=...) -> None: ...
    def set_secure_cookie(self, name: str, value: Union[str, bytes], expires_days: Optional[int]=..., version: Optional[int]=..., **kwargs: Any) -> None: ...
    def create_signed_value(self, name: str, value: Union[str, bytes], version: Optional[int]=...) -> bytes: ...
    def get_secure_cookie(self, name: str, value: Optional[str]=..., max_age_days: int=..., min_version: Optional[int]=...) -> Optional[bytes]: ...
    def get_secure_cookie_key_version(self, name: str, value: Optional[str]=...) -> Optional[int]: ...
    def redirect(self, url: str, permanent: bool=..., status: Optional[int]=...) -> None: ...
    def write(self, chunk: Union[str, bytes, dict]) -> None: ...
    def render(self, template_name: str, **kwargs: Any) -> Future[None]: ...
    def render_linked_js(self, js_files: Iterable[str]) -> str: ...
    def render_embed_js(self, js_embed: Iterable[bytes]) -> bytes: ...
    def render_linked_css(self, css_files: Iterable[str]) -> str: ...
    def render_embed_css(self, css_embed: Iterable[bytes]) -> bytes: ...
    def render_string(self, template_name: str, **kwargs: Any) -> bytes: ...
    def get_template_namespace(self) -> Dict[str, Any]: ...
    def create_template_loader(self, template_path: str) -> template.BaseLoader: ...
    def flush(self, include_footers: bool=...) -> Future[None]: ...
    def finish(self, chunk: Optional[Union[str, bytes, dict]]=...) -> Future[None]: ...
    def detach(self) -> iostream.IOStream: ...
    def send_error(self, status_code: int=..., **kwargs: Any) -> None: ...
    def write_error(self, status_code: int, **kwargs: Any) -> None: ...
    @property
    def locale(self) -> tornado_py3.locale.Locale: ...
    @locale.setter
    def locale(self, value: tornado_py3.locale.Locale) -> None: ...
    def get_user_locale(self) -> Optional[tornado_py3.locale.Locale]: ...
    def get_browser_locale(self, default: str=...) -> tornado_py3.locale.Locale: ...
    @property
    def current_user(self) -> Any: ...
    @current_user.setter
    def current_user(self, value: Any) -> None: ...
    def get_current_user(self) -> Any: ...
    def get_login_url(self) -> str: ...
    def get_template_path(self) -> Optional[str]: ...
    @property
    def xsrf_token(self) -> bytes: ...
    def check_xsrf_cookie(self) -> None: ...
    def xsrf_form_html(self) -> str: ...
    def static_url(self, path: str, include_host: Optional[bool]=..., **kwargs: Any) -> str: ...
    def require_setting(self, name: str, feature: str=...) -> None: ...
    def reverse_url(self, name: str, *args: Any) -> str: ...
    def compute_etag(self) -> Optional[str]: ...
    def set_etag_header(self) -> None: ...
    def check_etag_header(self) -> bool: ...
    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]: ...
    def log_exception(self, typ: Optional[Type[BaseException]], value: Optional[BaseException], tb: Optional[TracebackType]) -> None: ...

def stream_request_body(cls: Type[RequestHandler]) -> Type[RequestHandler]: ...
def removeslash(method: Callable[..., Optional[Awaitable[None]]]) -> Callable[..., Optional[Awaitable[None]]]: ...
def addslash(method: Callable[..., Optional[Awaitable[None]]]) -> Callable[..., Optional[Awaitable[None]]]: ...

class _ApplicationRouter(ReversibleRuleRouter):
    application: Any = ...
    def __init__(self, application: Application, rules: Optional[_RuleList]=...) -> None: ...
    def process_rule(self, rule: Rule) -> Rule: ...
    def get_target_delegate(self, target: Any, request: httputil.HTTPServerRequest, **target_params: Any) -> Optional[httputil.HTTPMessageDelegate]: ...

class Application(ReversibleRouter):
    transforms: Any = ...
    default_host: Any = ...
    settings: Any = ...
    ui_modules: Any = ...
    ui_methods: Any = ...
    wildcard_router: Any = ...
    default_router: Any = ...
    def __init__(self, handlers: Optional[_RuleList]=..., default_host: Optional[str]=..., transforms: Optional[List[Type[OutputTransform]]]=..., **settings: Any) -> None: ...
    def listen(self, port: int, address: str=..., **kwargs: Any) -> HTTPServer: ...
    def add_handlers(self, host_pattern: str, host_handlers: _RuleList) -> None: ...
    def add_transform(self, transform_class: Type[OutputTransform]) -> None: ...
    def __call__(self, request: httputil.HTTPServerRequest) -> Optional[Awaitable[None]]: ...
    def find_handler(self, request: httputil.HTTPServerRequest, **kwargs: Any) -> _HandlerDelegate: ...
    def get_handler_delegate(self, request: httputil.HTTPServerRequest, target_class: Type[RequestHandler], target_kwargs: Optional[Dict[str, Any]]=..., path_args: Optional[List[bytes]]=..., path_kwargs: Optional[Dict[str, bytes]]=...) -> _HandlerDelegate: ...
    def reverse_url(self, name: str, *args: Any) -> str: ...
    def log_request(self, handler: RequestHandler) -> None: ...

class _HandlerDelegate(httputil.HTTPMessageDelegate):
    application: Any = ...
    connection: Any = ...
    request: Any = ...
    handler_class: Any = ...
    handler_kwargs: Any = ...
    path_args: Any = ...
    path_kwargs: Any = ...
    chunks: Any = ...
    stream_request_body: Any = ...
    def __init__(self, application: Application, request: httputil.HTTPServerRequest, handler_class: Type[RequestHandler], handler_kwargs: Optional[Dict[str, Any]], path_args: Optional[List[bytes]], path_kwargs: Optional[Dict[str, bytes]]) -> None: ...
    def headers_received(self, start_line: Union[httputil.RequestStartLine, httputil.ResponseStartLine], headers: httputil.HTTPHeaders) -> Optional[Awaitable[None]]: ...
    def data_received(self, data: bytes) -> Optional[Awaitable[None]]: ...
    def finish(self) -> None: ...
    def on_connection_close(self) -> None: ...
    handler: Any = ...
    def execute(self) -> Optional[Awaitable[None]]: ...

class HTTPError(Exception):
    status_code: Any = ...
    log_message: Any = ...
    args: Any = ...
    reason: Any = ...
    def __init__(self, status_code: int=..., log_message: Optional[str]=..., *args: Any, **kwargs: Any) -> None: ...

class Finish(Exception): ...

class MissingArgumentError(HTTPError):
    arg_name: Any = ...
    def __init__(self, arg_name: str) -> None: ...

class ErrorHandler(RequestHandler):
    def initialize(self, status_code: int) -> None: ...
    def prepare(self) -> None: ...
    def check_xsrf_cookie(self) -> None: ...

class RedirectHandler(RequestHandler):
    def initialize(self, url: str, permanent: bool=...) -> None: ...
    def get(self, *args: Any, **kwargs: Any) -> None: ...

class StaticFileHandler(RequestHandler):
    CACHE_MAX_AGE: Any = ...
    root: Any = ...
    default_filename: Any = ...
    def initialize(self, path: str, default_filename: Optional[str]=...) -> None: ...
    @classmethod
    def reset(cls: Any) -> None: ...
    def head(self, path: str) -> Awaitable[None]: ...
    path: Any = ...
    absolute_path: Any = ...
    modified: Any = ...
    async def get(self, path: str, include_body: bool=...) -> None: ...
    def compute_etag(self) -> Optional[str]: ...
    def set_headers(self) -> None: ...
    def should_return_304(self) -> bool: ...
    @classmethod
    def get_absolute_path(cls: Any, root: str, path: str) -> str: ...
    def validate_absolute_path(self, root: str, absolute_path: str) -> Optional[str]: ...
    @classmethod
    def get_content(cls: Any, abspath: str, start: Optional[int]=..., end: Optional[int]=...) -> Generator[bytes, None, None]: ...
    @classmethod
    def get_content_version(cls: Any, abspath: str) -> str: ...
    def get_content_size(self) -> int: ...
    def get_modified_time(self) -> Optional[datetime.datetime]: ...
    def get_content_type(self) -> str: ...
    def set_extra_headers(self, path: str) -> None: ...
    def get_cache_time(self, path: str, modified: Optional[datetime.datetime], mime_type: str) -> int: ...
    @classmethod
    def make_static_url(cls: Any, settings: Dict[str, Any], path: str, include_version: bool=...) -> str: ...
    def parse_url_path(self, url_path: str) -> str: ...
    @classmethod
    def get_version(cls: Any, settings: Dict[str, Any], path: str) -> Optional[str]: ...

class FallbackHandler(RequestHandler):
    fallback: Any = ...
    def initialize(self, fallback: Callable[[httputil.HTTPServerRequest], None]) -> None: ...
    def prepare(self) -> None: ...

class OutputTransform:
    def __init__(self, request: httputil.HTTPServerRequest) -> None: ...
    def transform_first_chunk(self, status_code: int, headers: httputil.HTTPHeaders, chunk: bytes, finishing: bool) -> Tuple[int, httputil.HTTPHeaders, bytes]: ...
    def transform_chunk(self, chunk: bytes, finishing: bool) -> bytes: ...

class GZipContentEncoding(OutputTransform):
    CONTENT_TYPES: Any = ...
    GZIP_LEVEL: int = ...
    MIN_LENGTH: int = ...
    def __init__(self, request: httputil.HTTPServerRequest) -> None: ...
    def transform_first_chunk(self, status_code: int, headers: httputil.HTTPHeaders, chunk: bytes, finishing: bool) -> Tuple[int, httputil.HTTPHeaders, bytes]: ...
    def transform_chunk(self, chunk: bytes, finishing: bool) -> bytes: ...

def authenticated(method: Callable[..., Optional[Awaitable[None]]]) -> Callable[..., Optional[Awaitable[None]]]: ...

class UIModule:
    handler: Any = ...
    request: Any = ...
    ui: Any = ...
    locale: Any = ...
    def __init__(self, handler: RequestHandler) -> None: ...
    @property
    def current_user(self) -> Any: ...
    def render(self, *args: Any, **kwargs: Any) -> str: ...
    def embedded_javascript(self) -> Optional[str]: ...
    def javascript_files(self) -> Optional[Iterable[str]]: ...
    def embedded_css(self) -> Optional[str]: ...
    def css_files(self) -> Optional[Iterable[str]]: ...
    def html_head(self) -> Optional[str]: ...
    def html_body(self) -> Optional[str]: ...
    def render_string(self, path: str, **kwargs: Any) -> bytes: ...

class _linkify(UIModule):
    def render(self, text: str, **kwargs: Any) -> str: ...

class _xsrf_form_html(UIModule):
    def render(self) -> str: ...

class TemplateModule(UIModule):
    def __init__(self, handler: RequestHandler) -> None: ...
    def render(self, path: str, **kwargs: Any) -> bytes: ...
    def embedded_javascript(self) -> str: ...
    def javascript_files(self) -> Iterable[str]: ...
    def embedded_css(self) -> str: ...
    def css_files(self) -> Iterable[str]: ...
    def html_head(self) -> str: ...
    def html_body(self) -> str: ...

class _UIModuleNamespace:
    handler: Any = ...
    ui_modules: Any = ...
    def __init__(self, handler: RequestHandler, ui_modules: Dict[str, Type[UIModule]]) -> None: ...
    def __getitem__(self, key: str) -> Callable[..., str]: ...
    def __getattr__(self, key: str) -> Callable[..., str]: ...

def create_signed_value(secret: _CookieSecretTypes, name: str, value: Union[str, bytes], version: Optional[int]=..., clock: Optional[Callable[[], float]]=..., key_version: Optional[int]=...) -> bytes: ...
def decode_signed_value(secret: _CookieSecretTypes, name: str, value: Union[None, str, bytes], max_age_days: int=..., clock: Optional[Callable[[], float]]=..., min_version: Optional[int]=...) -> Optional[bytes]: ...
def get_signature_key_version(value: Union[str, bytes]) -> Optional[int]: ...
def is_absolute(path: str) -> bool: ...
