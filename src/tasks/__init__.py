# This file makes the tasks directory a module,
# So we can import tasks and then use tasks.ExampleTask
__all__ = ["BaseTask", "ExampleTask"]

from . import BaseTask, ExampleTask
