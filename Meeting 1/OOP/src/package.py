import logging

logger = logging.getLogger(__name__)

def simple_function(x):
    return x * x

def simple_function_2(x):
    return x * x

def register_function(func):
    from .method import SimpleClass 
    student = SimpleClass(func.__name__)
    logger.info(f"Function {func.__name__} registered with student: {student}")
    return student
