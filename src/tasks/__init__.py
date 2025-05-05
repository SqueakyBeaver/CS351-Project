# This file makes the tasks directory a module,
# So we can import tasks and then use tasks.ExampleTask
__all__ = [
    "BaseTask",
    "CustomerReport",
    "CreditLimitUpdate",
    "Login",
    "Logout",
    "RepresentativeReport",
]

from .BaseTask import BaseTask
from .CreditLimitUpdate import CreditLimitUpdate
from .CustomerReport import CustomerReport
from .LoginLogOut import Login, Logout
from .RepresentativeReport import RepresentativeReport
