# -*- coding: utf-8 -*-
"""
Tests for utils/users.py
"""
from typing import NoReturn

from utils.types import ExceptionType
from utils.users import format_failure_msg_from_exception


class TestFormatTraceBackToErrorMessage:
    """
    Tests for format_failure_msg_from_exception
    """

    def test_puts_exception_class_in_msg(self) -> None:
        exc: ExceptionType

        try:
            raise AttributeError("Task has no attribute 'run'")
        except AttributeError as e:
            exc = e

        formatted_message = format_failure_msg_from_exception(exc=exc)

        assert formatted_message.startswith("AttributeError")

    def test_puts_exception_message_in_msg(self) -> None:
        error_text = "Task has no attribute 'run'"

        exc: ExceptionType

        try:
            raise AttributeError("Task has no attribute 'run'")
        except AttributeError as e:
            exc = e

        formatted_message = format_failure_msg_from_exception(exc=exc)

        assert error_text in formatted_message

    def test_puts_traceback_info_in_msg(self) -> None:
        exc: ExceptionType

        try:
            raise AttributeError("Task has no attribute 'run'")
        except AttributeError as e:
            exc = e

        formatted_message = format_failure_msg_from_exception(exc=exc)

        assert formatted_message.count(__file__) == 1
        assert str(exc.__traceback__.tb_lineno) in formatted_message

    def test_puts_nested_traceback_in_msg(self) -> None:
        error_text = "Task has no attribute 'run'"

        def nested_func() -> NoReturn:
            """
            Nested function that just raises an exception.
            """
            raise AttributeError(error_text)

        # Initializing it in this one so that the IDE doesn't think we might reference it before it
        # is set. For some reason, the IDE doesn't know that the nested_func always raises an
        # exception...
        exc: ExceptionType = AttributeError("This should be overwritten by the exception raised later...")

        try:
            nested_func()
        except AttributeError as e:
            exc = e

        formatted_message = format_failure_msg_from_exception(exc=exc)

        # Expect the filename twice because we're running a func in the same file so both the
        assert formatted_message.count(__file__) == 2

        traceback_obj = exc.__traceback__

        assert str(traceback_obj.tb_lineno) in formatted_message
        assert str(traceback_obj.tb_next.tb_lineno) in formatted_message

        # Double check that we are in fact getting the correct message in there
        assert error_text in formatted_message

    def test_puts_some_response_text_in_msg(self) -> None:
        response_text = "Server Error"

        exc: ExceptionType

        try:
            raise AttributeError("Task has no attribute 'run'")
        except AttributeError as e:
            exc = e

        formatted_message = format_failure_msg_from_exception(exc=exc, response_text=response_text)

        assert response_text in formatted_message
