import inspect
import re
from collections.abc import Callable

from playwright.sync_api import Locator, Page, expect


def _get_assignment_var_name() -> str | None:
    frame = inspect.currentframe()
    try:
        if frame is None:
            return None

        current = frame.f_back
        while current is not None:
            code_context = inspect.getframeinfo(current).code_context
            if code_context:
                match = re.search(r'self\.(\w+)\s*=', code_context[0])
                if match:
                    return match.group(1)
            current = current.f_back
        return None
    finally:
        del frame


def _format_name(raw_name: str) -> str:
    readable = re.sub(r'[\s_\n-]+', ' ', raw_name).strip()
    if not readable:
        return readable
    return readable[0].upper() + readable[1:]


class ElementBase:

    def __init__(self, page: Page, name: str, locator: Locator) -> None:
        self.page = page
        self.name = _format_name(name)
        self.element_name = self.name
        self.locator = locator

    @classmethod
    def _resolve_name(cls, explicit_name: str | None, fallback: str) -> str:
        return explicit_name or _get_assignment_var_name() or fallback

    @classmethod
    def by_test_id(cls, page: Page, test_id: str, name: str | None = None) -> 'ElementBase':
        return cls(page, cls._resolve_name(name, test_id), page.get_by_test_id(test_id))

    @classmethod
    def by_css(cls, page: Page, selector: str, name: str | None = None) -> 'ElementBase':
        return cls(page, cls._resolve_name(name, selector), page.locator(selector))

    @classmethod
    def by_role(
        cls,
        page: Page,
        role: str,
        *,
        element_name: str | None = None,
        **kwargs,
    ) -> 'ElementBase':
        resolved_name = element_name or cls._resolve_name(None, role)
        return cls(page, resolved_name, page.get_by_role(role, **kwargs))

    def child(self, locator: Locator, name: str | None = None) -> 'ElementBase':
        return ElementBase(self.page, self._resolve_name(name, 'child'), locator)

    def click(self) -> None:
        self.locator.click()

    def _run_expect(self, action: str, assertion: Callable[[], None]) -> None:
        try:
            assertion()
        except AssertionError as error:
            raise AssertionError(
                f'The {self.element_name} {action}. Original error: {error}'
            ) from None

    def should_be_visible(self, timeout: float = 5000) -> None:
        self._run_expect(
            'is NOT visible',
            lambda: expect(self.locator).to_be_visible(timeout=timeout),
        )

    def should_have_text(self, text: str, timeout: float = 5000) -> None:
        self._run_expect(
            f'does not have text "{text}"',
            lambda: expect(self.locator).to_have_text(text, timeout=timeout),
        )

    def should_contain_text(self, text: str, timeout: float = 5000) -> None:
        self._run_expect(
            f'does not contain text "{text}"',
            lambda: expect(self.locator).to_contain_text(text, timeout=timeout),
        )
