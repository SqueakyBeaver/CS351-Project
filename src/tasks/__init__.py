# This file makes the tasks directory a module,
# So we can import tasks and then use tasks.ExampleTask
__all__ = ["BaseTask", "CustomerReport", "CreditLimitUpdate", "Login", "RepresentativeReport"]

from .BaseTask import BaseTask
from .CustomerReport import CustomerReport
from .CreditLimitUpdate import CreditLimitUpdate
from .LoginLogOut import Login
from .RepresentativeReport import RepresentativeReport
